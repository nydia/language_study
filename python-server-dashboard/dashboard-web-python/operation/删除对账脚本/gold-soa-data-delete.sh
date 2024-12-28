#!/bin/bash

: "
对账数据删除脚本：根据日期删除已经入库的对账数据

执行命令：
dev环境执行命令：bash gold-soa-data-delete.sh dev 18301866076 Aa111111 20230605 CHANNEL_1001_MOBAOPAY
sit环境执行命令：bash gold-soa-data-delete.sh sit 18301866076 Aa111111 20230605 CHANNEL_1001_MOBAOPAY
pit环境执行命令：bash gold-soa-data-delete.sh pit 18301866076 Aa111111 20230605 CHANNEL_1001_MOBAOPAY

参数说明：
gold-soa-data-delete.sh 脚本
dev/sit/pit 环境变量
18301866076 用户系统用户名
Aa111111 用户系统密码
20230605 对账日期
CHANNEL_1001_MOBAOPAY 支付渠道

安装jq:
1. yum install epel-release
2. yum list jq
3. yum install jq

影响表：
tbl_soa_channel_trade_info、tbl_soa_diff、tbl_order_pay_diff

授予执行权限：
chmod +x gold-soa-data-delete.sh

如果将脚本移动到服务出现命令没有的情况：
yum install dos2unix
然后执行命令: dos2unix ./gold-soa-data-delete.sh
重新执行命令

"

env=$1
user_name=$2
user_passwd=$3
check_date=$4
channel_no=$5

function delete_soa() {
    echo "用户登录:"
    echo "地址：$1"
    result=$(curl $1/gold-user-api/user/login -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic sdfsdsdgdfgdfgdfgfdg" -d "data={\"loginName\":\"${user_name}\",\"password\":\"${user_passwd}\",\"smsCode\":\"\",\"businessType\":1}")
    echo "登录返回结果: $result"

    user_token=$(echo ${result} | jq -r '.data.token')
    echo "登录返回token: $user_token"

    echo "对账数据删除 start>>>>>>"
    execute_result=$(curl $1/gold-user-api/manage/deleteSoaData -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: ${user_token}" -d "data={\"channelNo\":\"${channel_no}\",\"dateTm\":\"${check_date}\"}&token=${user_token}")
    
    # shell的function只能返回整数值，下面的就是错误的
    #return "$execute_result"

    # function最后一句作为返回值
    echo "execute_result:$execute_result"
}

if [ "$env" ==  "dev" ] ; then
    #dev
    delete_soa http://10.200.200.145:8080
    echo $?
elif [ "$env" ==  "sit" ] ; then
    #sit
    delete_soa http://172.30.42.12:8080
    echo $?
elif [ "$env" ==  "pit" ] ; then
    #pit
    delete_soa https://gold.yufugold.com
    # $?取的是function的执行结果，是个整数
    echo $?
else
    echo "{\"code\":\"1001\",\"message\":\"env参数不正确\"}"
fi
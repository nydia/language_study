# 项目结构

- dashboard-java 后端管理
- dashboard-web-python 各种运维操作：jenkins，系统信息获取，常用运维工具（使用python3.11.3）
  - main_v3.py 启动入口/路由模块（python3 启用）
  - main_v2.py 启动入口/路由模块（python2 未启用）
  - bak 文件备份
  - config 配置
  - db 和mysql的交互 && 类
  - jenkins_api jenkins的交互
  - machine 和发布环境的交互
  - task 定时任务
  - utils 工具类
    - cache.py 缓存工具类
    - log_utils.py 日志工具类
  - gitlab_api gitlab模块
  - static 静态资源
  - templates 页面模板
  - requirements python模块
  - cache 缓存模块
  - backends 实际内存实现
  - auth 权限模块
  - module 分模块路由（暂未启用）
  - operation 常用运维模块
  - tests 单元测试
- dashboard-web-python2 主要是结合ansible操作服务器（使用python2.7）
- deploy 发布文件
- docs 文档
- venv311 虚拟环境（python3.11.4）
- venv3 虚拟环境（python3.11.3)

# python组件
web: flask
mysql: pymysql

# dashboard-web-python 的自动化发布

## 使用脚本发布
1. 配置Jenkinfile文件：deploy/Jenkinsfile_web
2. 将deploy_web_docker.sh 放到目标服务器的 /opt/appl/spring-cloud/ 目录下面

## 使用ansible的ansible-playbook发布


# 入口

## local
- 首页
http://127.0.0.1:8088/index
- 启动任务
http://127.0.0.1:8088/task/start

## dev
http://172.30.41.15:8088/index  admin/Aa111111



# 运维操作

## 获取内存信息
cat /proc/meminfo

MemTotal:       15215624 kB
MemFree:          159908 kB
MemAvailable:    2070728 kB
Buffers:              52 kB
Cached:          2677116 kB
SwapCached:        69616 kB
Active:          9968304 kB
Inactive:        4506128 kB
Active(anon):    8901336 kB
Inactive(anon):  3543960 kB
Active(file):    1066968 kB
Inactive(file):   962168 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:       4194300 kB
SwapFree:         278196 kB
Dirty:               220 kB
Writeback:             0 kB
AnonPages:      11727752 kB
Mapped:           103576 kB
Shmem:            648028 kB
Slab:             315408 kB
SReclaimable:     215888 kB
SUnreclaim:        99520 kB
KernelStack:       21136 kB
PageTables:        42584 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    11802112 kB
Committed_AS:   19393112 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      205756 kB
VmallocChunk:   34359310332 kB
HardwareCorrupted:     0 kB
AnonHugePages:   1314816 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      132928 kB
DirectMap2M:     5109760 kB
DirectMap1G:    12582912 kB
package com.mengxiu.dashboard.service.impl;

import com.jcraft.jsch.JSchException;
import com.mengxiu.dashboard.service.SSHClient;
import com.mengxiu.dashboard.service.SshService;
import com.mengxiu.dashboard.utils.StringUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@Service
public class SshServiceImpl implements SshService {

    @Value("${servers.server1.server-id:}")
    private String serverId;
    @Value("${servers.server1.host-ip:}")
    private String serviceIp;
    @Value("${servers.server1.pub-key-path:}")
    private String pubKeyPath;
    @Value("${servers.server1.username:}")
    private String serverUsername;

    //定义一个连接池，session作用域的
    private Map<String, SSHClient> sshPool;

    /**
     * 获取或者设置 SSHClient
     * @param clientId
     * @return
     */
    private SSHClient getOrSetClient(String clientId){
        log.info("获取ssh连接客户端>>>>>>");
        if(sshPool.get(clientId) != null){
            return sshPool.get(clientId);
        }
        SSHClient sshClient = null;
        try {
            //获取服务的信息
            sshClient = new SSHClient(pubKeyPath);
            sshClient.setHost(serviceIp)
                    .setPort(22)
                    .setUsername(serverUsername);
            sshClient.login();
            sshPool.put(serverId, sshClient);
        } catch (JSchException e) {
            e.printStackTrace();
        }
        return sshClient;
    }

    /**
     * 查询各个服务状态
     */
    @Override
    public Map dynamicInfo(String clientId) throws JSchException {
        //返回结果
        Map<String, Object> map = new HashMap<>();
        //根据code查询服务信息
        SSHClient sshClient = getOrSetClient(clientId);

        if (!sshClient.getSession().isConnected()) {
            sshClient.login();
            sshPool.put(clientId, sshClient);
        }
        //执行命令
        //系统CPU情况
        String commond5 = "sar 1 1";
        String ret5 = sshClient.sendCmd(commond5).trim();
        ret5 = ret5.replaceAll("\n", ",");
        String[] split5 = ret5.split(",");
        if (split5.length > 0) {
            ret5 = split5[split5.length - 1];
            ret5 = ret5.replaceAll("[平均时间:|Average:|all]", "").trim();
            ret5 = ret5.replaceAll("\\s{1,}", ",");
            String[] split6 = ret5.split(",");
            map.put("cpuUserUsage", split6[0]);
            map.put("cpuSysUsage", split6[2]);
            map.put("cpuIdleUsage", split6[5]);
        } else {
            map.put("cpuUserUsage", 0);
            map.put("cpuSysUsage", 0);
            map.put("cpuIdleUsage", 0);
        }

        //系统内存情况
        double memtotal = 1.0;
        double memfree = 0.0;
        String commond6 = "cat /proc/meminfo | awk '$1 ~/MemTotal/' |awk '{print $2}'";
        String ret6 = sshClient.sendCmd(commond6).trim();
        if (StringUtils.isNotEmpty(ret6)) {
            memtotal = Double.valueOf(ret6);
        }
        String commond7 = "cat /proc/meminfo | awk '$1 ~/MemFree/' |awk '{print $2}'";
        String ret7 = sshClient.sendCmd(commond7).trim();
        if (StringUtils.isNotEmpty(ret7)) {
            memfree = Double.valueOf(ret7);
        }

        if (memtotal > 0 && memfree > 0 && (memtotal - memfree) > 0) {
            map.put("memUsage", (memtotal - memfree) / memtotal * 100);
        } else {
            map.put("memUsage", 0.0);
        }

        //应用信息
        // TODO

        //应用服务状态和启动时间
        List<Map<String, Object>> list = new ArrayList<>();
        String retc = sshClient.sendCmd("ps aux|grep" + " " + clientId + " " + "|grep -v \"grep\"|awk '{print $2,$9,$10,$8}'");
        if (StringUtils.isNotEmpty(retc)) {
            retc = retc.replaceAll("\n", ",");
            String[] split = retc.split(",");
            for (String s : split) {
                Map<String, Object> mp = new HashMap<>();
                String[] sp = s.split("\\s{1,1}");
                mp.put("appPid", sp[0]);
                mp.put("appStartTime", sp[1] + " " + sp[2]);
                mp.put("appStatus", sp[3]);
                list.add(mp);
            }
        }

        map.put("appProcess", list);

        //应用服务CPU占用率
        double appCpuUsage = 0.0;
        String commond8 = "ps aux|grep" + " " + clientId + " " + "|grep -v \"grep\"|awk '{print $3}'";
        String ret8 = sshClient.sendCmd(commond8);
        ret8 = ret8.replaceAll("\n", ",");
        ret8 = ret8 + "0";
        String[] split1 = ret8.split(",");
        for (String s : split1) {
            appCpuUsage += Double.valueOf(s);
        }
        map.put("appCpuUsage", appCpuUsage);

        //应用服务内存占用率
        double memoryUsage = 0.0;
        String commond9 = "ps aux|grep" + " " + clientId + " " + "|grep -v \"grep\"|awk '{print $4}'";
        String ret9 = sshClient.sendCmd(commond9);
        ret9 = ret9.replaceAll("\n", ",");
        ret9 = ret9 + "0";
        String[] split9 = ret9.split(",");
        for (String s : split9) {
            memoryUsage += Double.valueOf(s);
        }
        map.put("appMemoryUsage", memoryUsage);

        return map;
    }

    /**
     * 查询各个服务状态
     */
    @Override
    public Map sysInfo(String clientId) throws JSchException {
        //返回结果
        Map<String, Object> map = new HashMap<>();
        //根据code查询服务信息
        SSHClient sshClient = sshPool.get(clientId);

        if (!sshClient.getSession().isConnected()) {
            sshClient.login();
        }
        //执行命令
        //服务器名称
        String commond1 = "hostname";
        String ret1 = sshClient.sendCmd(commond1).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("hostName", ret1);
        //操纵系统
        String commond2 = "cat /etc/redhat-release";
        String ret2 = sshClient.sendCmd(commond2).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("operSystem", ret2);
        //服务器IP
        String commond3 = "ifconfig |head -2 |grep inet |awk '{print $2}'";
        String ret3 = sshClient.sendCmd(commond3).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("serviceIp", ret3);
        //系统架构
        String commond4 = "arch";
        String ret4 = sshClient.sendCmd(commond4).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("systemArch", ret4);
        //物理cpu个数
        String cmdPhysicalNum = "cat /proc/cpuinfo |grep \"physical id\"|sort|uniq|wc -l";
        String physicalNum = sshClient.sendCmd(cmdPhysicalNum).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("physicalNum", physicalNum);
        //每个物理cpu核数
        String cmdCoresNUm = "cat /proc/cpuinfo |grep \"cpu cores\"|wc -l";
        String coresNUm = sshClient.sendCmd(cmdCoresNUm).replaceAll("[\\s*\\t\\n\\r]", "");
        map.put("coresNUm", coresNUm);

        return map;
    }
}

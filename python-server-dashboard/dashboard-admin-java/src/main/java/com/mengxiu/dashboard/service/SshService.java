package com.mengxiu.dashboard.service;

import com.jcraft.jsch.JSchException;

import java.util.Map;

public interface SshService {

    /**
     * 查询各个服务状态
     */
    Map dynamicInfo(String clientId) throws JSchException;


    /**
     * 查询各个服务状态
     */
    Map sysInfo(String clientId) throws JSchException;

}

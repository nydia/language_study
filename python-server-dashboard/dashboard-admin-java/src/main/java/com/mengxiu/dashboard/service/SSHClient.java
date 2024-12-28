package com.mengxiu.dashboard.service;

import com.jcraft.jsch.*;
import org.springframework.stereotype.Component;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//@Component
public class SSHClient {
    /**
     * Server Host IP Address，default value is localhost
     */
    private String host = "localhost";

    /**
     * Server SSH Port，default value is 22
     */
    private Integer port = 22;

    /**
     * SSH Login Username
     */
    private String username = "";

    /**
     * SSH Login Password
     */
    private String password = "";

    /**
     * SSH Login pubKeyPath，这里如果要用密钥登录的话，是你本机的或者项目所在服务器的私钥地址
     */

    private String pubKeyPath = "C:/Users/zhangyanhe/.ssh/id_rsa";
    //private String pubKeyPath = "/root/.ssh/id_rsa";

    /**
     * JSch
     */
    private JSch jsch = null;

    /**
     * ssh session
     */
    private Session session = null;

    /**
     * ssh channel
     */
    private Channel channel = null;

    /**
     * timeout for session connection
     */
    private final Integer SESSION_TIMEOUT = 60000;

    /**
     * timeout for channel connection
     */
    private final Integer CHANNEL_TIMEOUT = 60000;

    /**
     * the interval for acquiring ret
     */
    private final Integer CYCLE_TIME = 100;

    public SSHClient() throws JSchException {
        // initialize
        jsch = new JSch();
        jsch.addIdentity(pubKeyPath);
    }
    public SSHClient(String pubKeyPath) throws JSchException {
        // initialize
        this.pubKeyPath = pubKeyPath;
        jsch = new JSch();
        jsch.addIdentity(pubKeyPath);
    }

    public SSHClient setHost(String host) {
        this.host = host;
        return this;
    }

    public SSHClient setPort(Integer port) {
        this.port = port;
        return this;
    }

    public SSHClient setUsername(String username) {
        this.username = username;
        return this;
    }

    public SSHClient setPassword(String password) {
        this.password = password;
        return this;
    }

    public SSHClient setPubKeyPath(String pubKeyPath) {
        this.pubKeyPath = pubKeyPath;
        return this;
    }

    public Session getSession() {
        return this.session;
    }

    public Channel getChannel() {
        return this.channel;
    }

    /**
     * login to server
     */
    public void login(String username, String host, Integer port) {
        this.username = username;
        this.host = host;
        this.port = port;
        //我的是免密登录，所以不用密码
        //this.password = password;

        try {
            if (null == session) {
                session = jsch.getSession(this.username, this.host, this.port);

                // It must not be recommended, but if you want to skip host-key check,
                // invoke following,
                session.setConfig("StrictHostKeyChecking", "no");
            }
            session.connect(SESSION_TIMEOUT);
        } catch (JSchException e) {
            this.logout();
        }
    }

    /**
     * login to server
     */
    public void login() {
        this.login(this.username, this.host, this.port);
    }

    /**
     * logout of server
     */
    public void logout() {
        this.session.disconnect();
    }

    /**
     * send command through the ssh session,return the ret of the channel
     *
     * @return
     */
    public synchronized String sendCmd(String command) {

        // judge whether the session or channel is connected
        if (!session.isConnected()) {
            this.login();
        }
        if (this.session == null)
            return null;
        Channel channel = null;
        //InputStream input = null;
        BufferedReader bufferedReader = null;
        String resp = "";
        try {
            channel = this.session.openChannel("exec");
            ((ChannelExec) channel).setCommand(command);

            channel.setInputStream(null);
            ((ChannelExec) channel).setErrStream(System.err);
            channel.connect();

            bufferedReader = new BufferedReader(new InputStreamReader(channel.getInputStream()));

            String line = null;
            while ((line = bufferedReader.readLine()) != null) {
                resp += line + "\n";
            }
            if (resp != null && !resp.equals("")) {
                resp = resp.substring(0, resp.length() - 1);
            }
        } catch (JSchException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (bufferedReader != null) {
                try {
                    bufferedReader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (channel != null) {
                channel.disconnect();
            }
        }
        return resp;
    }

    //写个main方法测试一下效果
    public static void main(String[] args) throws JSchException {
        SSHClient sshClient = new SSHClient();
        sshClient.setHost("192.168.31.250").setPort(22).setUsername("root");
        sshClient.login();
        String commond5 = "sar 1 1";
        String ret5 = sshClient.sendCmd(commond5).trim();
        ret5 = ret5.replaceAll("\n", ",");
        String[] split5 = ret5.split(",");
        if (split5.length > 0) {
            ret5 = split5[split5.length - 1];
            ret5 = ret5.replaceAll("[平均时间:|Average:|all]", "").trim();
            ret5 = ret5.replaceAll("\\s{1,}", ",");
            String[] split6 = ret5.split(",");
            System.out.println(Arrays.toString(split6));
        }
        System.out.println("******************************");
        System.out.println(ret5);
        System.out.println("******************************");
        sshClient.logout();
    }
}
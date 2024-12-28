package com.mengxiu.dashboard.contorller;

import com.jcraft.jsch.JSchException;
import com.mengxiu.dashboard.service.SshService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@Scope("session")
@RestController
@RequestMapping("/tool/ssh")
public class SSHController extends BaseController {

    @Autowired
    private SshService sshService;

    /**
     * 查询各个服务状态
     */
    @GetMapping("/dynamicInfo/{code}")
    public Map dynamicInfo(@PathVariable("code") String code) throws JSchException {
        return sshService.dynamicInfo(code);
    }

    /**
     * 查询各个服务状态
     */
    @GetMapping("/sysInfo/{code}")
    public Map sysInfo(@PathVariable("code") String code) throws JSchException {
        return sshService.sysInfo(code);
    }

}

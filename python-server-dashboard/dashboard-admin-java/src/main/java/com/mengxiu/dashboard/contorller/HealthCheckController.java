package com.mengxiu.dashboard.contorller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;

/**
 * @Description HealthCheck
 * @Date 2023/4/13 16:50
 * @Created by <a href="mailto:nydia_lhq@hotmail.com">lvhuaqiang</a>
 */
@RestController
@RequestMapping(value = "/")
public class HealthCheckController {
    Logger logger = LoggerFactory.getLogger(HealthCheckController.class);

    @RequestMapping(value = "/healthCheck")
    public String healthCheck(HttpServletRequest request) {
        logger.info(">>> 进入healthCheck");
        String v = "no version";
        String vesion = request.getHeader("version");
        if (vesion != null) {
            v = vesion;
        }
        return "{success:" + v + "}";
    }


}

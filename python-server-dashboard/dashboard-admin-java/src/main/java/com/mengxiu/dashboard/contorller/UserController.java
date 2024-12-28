package com.mengxiu.dashboard.contorller;

import com.mengxiu.dashboard.entity.User;
import com.mengxiu.dashboard.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/user")
public class UserController extends BaseController {

    @Autowired
    private UserService userService;

    @PostMapping("/add")
    public ResponseEntity<User> add(@RequestBody User user) {
        userService.add(user);
        return ResponseEntity.ok(user);
    }

    @PostMapping("/selectByUsername")
    public ResponseEntity<User> selectByUsername(@RequestBody Map map) {
        User user = userService.selectByUsername((String) map.get("username"));
        return ResponseEntity.ok(user);
    }

}

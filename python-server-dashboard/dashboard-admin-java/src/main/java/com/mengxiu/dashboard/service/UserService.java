package com.mengxiu.dashboard.service;

import com.mengxiu.dashboard.entity.User;

public interface UserService {

    int add(User user);

    User selectByUsername(String username);

    User selectById(Integer userId);


}

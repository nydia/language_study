package com.mengxiu.dashboard.service.impl;

import com.mengxiu.dashboard.entity.User;
import com.mengxiu.dashboard.mapper.UserMapper;
import com.mengxiu.dashboard.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper userMapper;

    @Override
    public int add(User user) {
        return userMapper.insert(user);
    }

    @Override
    public User selectByUsername(String username) {
        return userMapper.selectByName(username);
    }

    @Override
    public User selectById(Integer userId) {
        return userMapper.selectById(userId);
    }
}

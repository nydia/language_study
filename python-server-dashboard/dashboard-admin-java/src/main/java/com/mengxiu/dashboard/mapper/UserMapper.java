package com.mengxiu.dashboard.mapper;

import com.mengxiu.dashboard.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Component;

@Component
@Mapper
public interface UserMapper {

    int insert(User user);

    int update(User user);

    User selectById(Integer id);

    User selectByName(String username);

}

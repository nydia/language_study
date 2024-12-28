package com.mengxiu.dashboard.utils;

import java.util.Random;

/**
 * @Description: StringUtils
 * @ClassName: StringUtils
 * @Auther: Nydia.LHQ
 */
public class StringUtils extends org.apache.commons.lang3.StringUtils {

    //获取指定长度随机字符串
    public static String getRandomString(int length) {
        String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random random = new Random();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < length; i++) {
            int number = random.nextInt(62);
            sb.append(str.charAt(number));
        }
        return sb.toString();
    }

    public static String toString(Object obj){
        return obj.toString();
    }


}

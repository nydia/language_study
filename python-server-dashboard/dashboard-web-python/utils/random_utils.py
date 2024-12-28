# _*_ coding:utf-8 _*_

import random
import string

def generate_random_string(length):
    # 定义包含所有可能字符的字符集合
    characters = string.ascii_letters + string.digits + string.punctuation
    # 从字符集合中随机选择字符，重复 length 次，然后将它们连接起来
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
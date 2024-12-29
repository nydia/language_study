#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FileUtil:
    def __init__(self) -> None:
        pass
    def file_create(self,filepath):
        f = open(filepath, 'w+')
        f.close()
    def file_create_batch(self,filepath):
        f = open(filepath, 'w+')
        f.close()
    def file_write(self,filepath,content):
        f = open(filepath, 'w+')
        f.write(content)
        f.close()
    def file_read_content(self,filepath): # 使用 with 语句来安全地打开和关闭文件
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    def file_read_line(self,filepath): # 使用列表读取所有行， 使用 strip() 去除每行末尾的换行符
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
        return lines
    def file_read_all_line(self,filepath): # 使用列表读取所有行
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return lines
    def file_read_all_line(self,filepath):  # 读取前10行
        with open('example.txt', 'r') as file:
            lines = [next(file) for _ in range(10)]
        return lines
    
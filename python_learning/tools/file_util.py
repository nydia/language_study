#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import threading

class FileUtil:
    def __init__(self) -> None:
        pass
    def file_create(self,filepath): # 创建文件
        f = open(filepath, 'w+')
        f.close()
    def file_create_batch(self,filelist): # 批量创建文件
        for filepath in filelist:
            f = open(filepath, 'w+')
            f.close()
    def file_write(self,filepath,content): # 写入文件，文件不存在就创建文件
        f = open(filepath, 'w+')
        f.write(content)
        f.close()
    def file_write_batch(self,filedict): # 使用多线程，批量对多个文件写入不同内容，参数为字典
        threads = []
        for filepath in filedict:
            content = filedict[filepath]
            #_thread.start_new_thread(self.file_write,('thread-1',filepath,content))
            t = threading.Thread(target=self.file_write,args=(filepath,content))
            threads.append(t)
            t.start()
        for t in threads: # 等待所有线程都执行完成
            t.join()    
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
    
import os
from file_util import FileUtil

# dirs  = 'C:/temp/吕思源/10/'
# for i in range(1,10):
#     path = dirs + str(i) + '.txt'
#     f = open(path, 'w+')
#     f.write("你好" + str(i))
#     f.close()
    
# dirs  = 'C:/temp/吕思源/10/'
# fileutil = FileUtil()
# for i in range(1,10):
#     path = dirs + str(i) + '.txt'
#     content = "你好" + str(i)
#     fileutil.file_write(path, content)
    
dirs  = 'C:/temp/吕思源/10/'
fileutil = FileUtil()
list = []
for i in range(1,10):
    path = dirs + str(i) + '.txt'
    content = "你好" + str(i)
    fileutil.file_write(path, content)
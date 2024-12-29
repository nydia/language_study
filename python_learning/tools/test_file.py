# 使用 with 语句来安全地打开和关闭文件
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
    
    
# 逐行读取文件
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # 使用 strip() 去除每行末尾的换行符
        
with open('C:/temp/redisdata/redisdata.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
print(lines)
    
    
    
 # 读取文件的特定部分
with open('example.txt', 'r') as file:
    lines = [next(file) for _ in range(10)]  # 读取前10行
    print(lines)           



# 使用列表读取所有行
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


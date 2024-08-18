import redis

# 连接到 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)

# 清空数据库
r.flushall()

# 测试数据
with open('C:/temp/redisdata/redisdata.txt', 'r') as file:
    content = file.read()

# 字符串存储
for n in range(1, 600):
    key = "key-{}".format('str')
    r.set(key, n)
memory_strings = r.memory_usage(key)
# 字符串存储-编码
strings_encoding = r.execute_command('OBJECT', 'ENCODING', key)

# 输出结果
print("Memory usage for Strings:", memory_strings)
print("Encoding for Strings:", strings_encoding)
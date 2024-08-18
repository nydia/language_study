import redis

# 连接到 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)

# 清空数据库
r.flushall()

# 测试数据
with open('C:/temp/redisdata/redisdata.txt', 'r') as file:
    content = file.read()

# 列表存储
for key, value in 100:
    r.delete(key)
    r.rpush(key, content)
memory_lists = r.memory_usage(key)

# 列表存储-编码
lists_encoding = r.execute_command('OBJECT', 'ENCODING', key)

print("Memory usage for Lists:", memory_lists)
print("Encoding usage for Lists:", lists_encoding)
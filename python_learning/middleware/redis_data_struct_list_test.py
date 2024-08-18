import redis
import chardet

# 连接到 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)

# 清空数据库
r.flushall()

# 测试数据
# 检测文件编码
with open('C:/temp/redisdata/redisdata.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding_file = result['encoding']
with open('C:/temp/redisdata/redisdata.txt', 'r', encoding=encoding_file) as file:
    content = file.read()

# 列表存储
key = 'k'
r.delete(key)
for n in range(0, 10):
    r.rpush(key, n)
    #r.rpush(key, content)
memory_lists = r.memory_usage(key) # 单位字节

# 列表存储-编码
lists_encoding = r.execute_command('OBJECT', 'ENCODING', key)

print("Memory usage for Lists:", memory_lists)
print("Encoding usage for Lists:", lists_encoding)
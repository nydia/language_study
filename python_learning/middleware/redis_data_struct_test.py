import redis
import random

# 连接到 Redis 服务器
r = redis.Redis(host='localhost', port=6379, db=0)

# 清空数据库
r.flushall()

# 测试数据
data = {
    'key': ['value{}'.format(i) for i in range(100)]
}

# 字符串存储
for key, value in data.items():
    r.set(key, value[0])
memory_strings = r.memory_usage(key)
# 字符串存储-编码
strings_encoding = r.execute_command('OBJECT', 'ENCODING', key)



# 列表存储
for key, value in data.items():
    r.delete(key)
    r.rpush(key, *value)
memory_lists = r.memory_usage(key)
# 列表存储-编码
lists_encoding = r.execute_command('OBJECT', 'ENCODING', key)



# 集合存储
for key, value in data.items():
    r.delete(key)
    r.sadd(key, *value)
memory_sets = r.memory_usage(key)
# 集合存储-编码
sets_encoding = r.execute_command('OBJECT', 'ENCODING', key)



# 有序集合存储
for key, value in data.items():
    r.delete(key)
    for v in value:
        r.zadd(key, {v: random.random()})
memory_sorted_sets = r.memory_usage(key)
# 有序集合存储-编码
sorted_sets_encoding = r.execute_command('OBJECT', 'ENCODING', key)



# 哈希表存储
for key, value in data.items():
    r.delete(key)
    r.hset(key, mapping={str(i): v for i, v in enumerate(value)})
memory_hashes = r.memory_usage(key)
# 哈希表存储-编码
hashes_encoding = r.execute_command('OBJECT', 'ENCODING', key)


# 输出结果
print("Memory usage for Strings:", memory_strings)
print("Memory usage for Lists:", memory_lists)
print("Memory usage for Sets:", memory_sets)
print("Memory usage for Sorted Sets:", memory_sorted_sets)
print("Memory usage for Hashes:", memory_hashes)

print("Encoding for Strings:", strings_encoding)
print("Encoding usage for Lists:", lists_encoding)
print("Encoding usage for Sets:", sets_encoding)
print("Encoding usage for Sorted Sets:", sorted_sets_encoding)
print("Encoding usage for Hashes:", hashes_encoding)
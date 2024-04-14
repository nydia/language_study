import uuid

# 随机字符串
def get_random_str(): 
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    return hex_id
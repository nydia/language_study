import uuid

# 随机字符串
def get_random_str(): 
    unique_id = uuid.uuid4()
    hex_id = unique_id.hex
    return hex_id

# 判断字符串是否为空
def str_is_not_blank(param_str):
    if param_str and len(param_str) > 0:
        return True
    return False
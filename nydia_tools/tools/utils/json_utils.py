
def serialize(obj):
    """
    将对象转换为可以序列化为JSON的数据类型
    :param obj: 待转换的对象
    :return: 转换后的数据类型
    """
    if obj is None:
        return None
    try:
        # 如果对象本身就是可以序列化为JSON的类型，则直接返回
        if isinstance(obj, (str, int, float, bool, list, tuple, dict)):
            return obj
        # 如果对象实现了__dict__方法，则将其转换为字典并返回
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        # 如果对象是其他类型，则抛出异常
        else:
            raise SerializationError(code=500, message='Cannot serialize object')
    except Exception as e:
        raise SerializationError(code=500, message=str(e))


class SerializationError(Exception):
    """
    自定义的异常类，用于处理序列化错误
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message
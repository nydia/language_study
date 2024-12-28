# _*_ coding:utf-8 _*_

class LogUtils:
    def __init__(self) -> None:
        pass
    def info(self,msg,*params): # 非固定位置参数传参(*args) / 非固定关键字传参(**kwargs)
        if msg is None:
            return None
        if msg is not None and params is None:
            print(str(msg))
        if msg is not None and params is not None:
            list_params = list(params) # 元组参数转为数组参数
            print(str(msg).format(*list_params))
            
    def error(self,msg,*params): # 非固定位置参数传参(*args) / 非固定关键字传参(**kwargs)
        if msg is None:
            return None
        if msg is not None and params is None:
            print(str(msg))
        if msg is not None and params is not None:
            list_params = list(params) # 元组参数转为数组参数
            print(str(msg).format(*list_params))        

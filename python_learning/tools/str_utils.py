# _*_ coding:utf-8 _*_

"""
字符串工具类
"""
class StrUtils:
    def __init__(self) -> None:
        pass

    @classmethod
    def is_blank(cls,strs): # 字符串为空
        if strs is None:
            return True
        if len(strs.strip()) <= 0:
            return True
        return False

    @classmethod
    def is_not_blank(cls,strs): # 字符串不为空
        if strs is None:
            return False
        if len(strs.strip()) <= 0:
            return False
        return True

    @classmethod
    def to_str(cls,strs): # 转为str
        if strs is None:
            return ""
        if len(strs.strip()) <= 0:
            return ""
        return str(strs)

    @classmethod
    def substr(cls,strs,startIndex,endIndex=None): # 截取字符串
        if strs is None:
            return ""
        if len(strs.strip()) <= 0:
            return ""
        if startIndex is not None and endIndex is not None:
            return str(strs)[startIndex:endIndex]
        if startIndex is not None and endIndex is None:
            return str(strs)[startIndex:]
    @classmethod
    def equals(cls,source,dest): # 字符串对比
        if source is None and dest is not None:
            return False
        if source is not None and dest is None:
            return False
        if source is None and dest is None:
            return True
        return source == dest            

# -- coding: utf-8 --
from data_base import BytesObject
import struct


class BaseItem(BytesObject):
    """
    基类，所有dex的section中各个子项的结构类都继承这个类
    """

    def __init__(self, bytes=None):
        """
        bytes: 原始字节数组
        """
        if bytes is not None:
            self.setBytes(bytes)

    def decode_bytes(self, bytes=None, offset=0):
        if bytes is None:
            bytes = self.original_bytes
            offset = self.offset
        else:
            self.original_bytes = bytes
            self.offset = offset
        self.decode(bytes, offset)
        return self.item_size

    def convertOffToId(self, context):
        """ 转换文件偏移量到相关的id """
        pass

    def convertIdToOff(self, context):
        """ 转换id到相关的文件偏移量 """
        pass

    def convertIdToItem(self, context):
        """ 转换id到item对象 """
        pass

    def convertItemToId(self, context):
        """ 转换item对象到id """
        pass

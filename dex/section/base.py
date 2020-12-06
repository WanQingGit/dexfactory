# -- coding: utf-8 --
from common_tool import convertBytesToHexStr
from odex.section.tool import createBytes
import struct
import numpy as np


class BytesObject(object):
    item_size = None
    bytes = None

    @classmethod
    def create(cls):
        """
        创建项
        """
        if cls.item_size:
            return cls(createBytes(cls.item_size))
        return cls()

    """
    字节数组对象，该对象包含一段字节数组，主要用于字节数组的解析和压缩
    """

    def __init__(self, bytes, off=0):
        """
        bytes: 原始字节数组
        """
        self.original_bytes = bytes
        self.offset = off
        # self.setBytes(np.array(bytes).astype(np.ubyte))

    def copyFrom(self, bytes):
        """
        bytes: 原始字节数组，从该数组拷贝到Item项的字节数组中
        """
        self.bytes[0:self.bytes_size] = bytes[0:self.bytes_size]

    def setBytes(self, bytes):
        """
        设置字节数组
        bytes: 新的字节数组
        """
        self.bytes = bytes
        if self.item_size is None:
            self.item_size = len(bytes)
        else:
            assert self.item_size == len(bytes)

    def getOrginalBytes(self):
        return self.original_bytes

    def getBytes(self):
        """
        返回字节数组
        """
        if self.bytes is not None:
            return self.bytes
        if self.item_size:
            self.setBytes(createBytes(self.item_size))
            return self.bytes
        raise Exception('can not create bytes without size info')

    def getBytesSize(self):
        """
        返回字节数组大小
        """
        return self.bytes_size

    def decode(self):
        """
        从字节数组中解析变量
        """
        pass

    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        pass

    def tostring(self):
        """
        转换为可打印的字符串
        """
        pass

    def tohexstring(self):
        """
        转换为十六进制字符串
        """
        return convertBytesToHexStr(self.bytes)

    def __repr__(self):
        return self.__class__.__name__


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


class BaseData(BaseItem):
    pass

# -- coding: utf-8 --

from base import *
from common_tool import *


class TypeIdItem(BaseItem):
    """
    section子结构: 类型ID项
    """
    item_size = 0x04


    def decode(self,bytes,offset):
        """
        从字节数组中解析变量
        """

        self.string_id = convertBytesToInt(bytes[offset:offset+0x04])

        # 调整字节数组尺寸
        # self.setBytes(bytes[0x00:0x04])

    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        bytes = self.getBytes()

        bytes[0x00:0x04] = convertIntToBytes(self.string_id)

    def tostring(self):
        """
        转化为可打印的字符串
        """
        string = '%.4d' % self.string_id
        return string

# -- coding: utf-8 --

from base import *


class EncodedArrayItem(BaseItem):
    """
    section子结构: encoded_array_item
    """
    item_size = 0x04


    def decode(self):
        """
        从字节数组中解析变量
        """
        bytes = self.getBytes()

        from data_encoded_value import EncodedArrayData
        self.value = EncodedArrayData(bytes)

        # 调整字节数组尺寸
        self.setBytes(bytes[0x00:self.value.getBytesSize()])

    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        bytes = self.getBytes()

        # 调整尺寸
        new_size = self.value.getBytesSize()
        if self.getBytesSize != new_size:
            self.setBytes(createBytes(new_size))

        # 编码
        bytes = self.getBytes()

        bytes[0x00:self.value.getBytesSize()] = self.value.getBytes()

    def tostring(self):
        """
        转换为可打印的字符串
        """
        string = ''
        string += self.value.tostring()
        return string

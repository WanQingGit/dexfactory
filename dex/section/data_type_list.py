# -- coding: utf-8 --

from base import *
from odex.section.tool import *


class TypeListItemData(BaseData):
    """
    类型列表中的子类型结构数据
    """
    item_size = 0x02


    def decode(self,bytes,off):

        self.type_id = convertBytesToShort(bytes[off:off+0x02])

    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        bytes = self.bytes

        bytes[0x00:0x02] = convertShortToBytes(self.type_id)

    def getTypeId(self):
        """
        获取类型id
        """
        return self.type_id

    def setTypeId(self, type_id):
        """
        设置类型id
        type_id:    类型id
        """
        self.type_id = type_id
        self.encode()

    def tostring(self):
        """
        转换为可打印的字符串
        """
        return 'type: %.4x' % self.type_id

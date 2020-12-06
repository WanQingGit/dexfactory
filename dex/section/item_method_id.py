# -- coding: utf-8 --

from base import *
from common_tool import convertBytesToShort, convertShortToBytes, convertIntToBytes


class MethodIdItem(BaseItem):
    """
    属性项
    """
    item_size = 0x08

    Struct = struct.Struct('<HHL')

    def decode(self,bytes,off):

        # self.class_id = convertBytesToShort(bytes[0x00:0x02])
        # self.proto_id = convertBytesToShort(bytes[0x02:0x04])
        # self.name_id = convertBytesToInt(bytes[0x04:0x08])
        self.class_id,self.proto_id,self.name_id=self.Struct.unpack(bytes[off:off+self.item_size])


    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        bytes = self.getBytes()

        bytes[0x00:0x02] = convertShortToBytes(self.class_id)
        bytes[0x02:0x04] = convertShortToBytes(self.proto_id)
        bytes[0x04:0x08] = convertIntToBytes(self.name_id)

    def getClassId(self):
        """
        获取类id
        """
        return self.class_id

    def getProtoId(self):
        """
        获取原型id
        """
        return self.proto_id

    def getNameId(self):
        """
        获取名称id
        """
        return self.name_id

    def setClassId(self, class_id):
        """
        设置类id
        class_id: 类id
        """
        self.class_id = class_id
        self.encode()

    def setProtoId(self, proto_id):
        """
        设置原型id
        type_id: 类型id
        """
        self.proto_id = proto_id
        self.encode()

    def setNameId(self, name_id):
        """
        设置名称id
        name_id: 名称id
        """
        self.name_id = name_id
        self.encode()

    def tostring(self):
        """
        转换为可打印的字符串
        """
        return 'class: %.4d, proto: %.4d, name: %.4d' % (self.class_id, self.proto_id, self.name_id)

# -- coding: utf-8 --
from common_tool import convertBytesToHexStr, convertBytesToInt
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
        return self.item_size

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
    align = 0

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

    def align_off(self, off):
        return off


class BaseData(BaseItem):
    pass


class BaseSectionItem(BaseItem):
    ItemData = None

    def decode(self, bytes, off):
        """
        解码字节数组
        """

        self.item_count = convertBytesToInt(bytes[off:off + 0x04])
        self.item_list = []

        off += 0x04
        for i in range(self.item_count):
            item = self.ItemData()
            off += item.decode_bytes(bytes, off)
            # 解码子项数据
            # from data_annotation_set_item import AnnotationSetItemItemOffData
            # item = AnnotationSetItemItemOffData(bytes[off:off + 0x04])
            # 添加数据列表
            self.item_list.append(item)

        self.item_size = self.align_off(off) - self.offset


class BaseSection(BytesObject):
    """
    section的基类
    """

    def __init__(self, context, bytes, item_count, off):
        """
        初始化
        context:         上下文信息
        section_type:    section的类型
        bytes:           原始字节数组
        item_count:       子项个数
        """
        super(BaseSection, self).__init__(bytes, off)

        # 基础变量
        # self.section_name = type_desc_map[section_type]
        self.item_count = item_count

        # 关联context
        self.context = context
        self.context.setSection(self.section_type, self)

        # 解码
        self.decode()

    @property
    def section_type(self):
        raise NotImplemented

    def decode(self):
        """
        解码字节数组
        """
        bytes = self.getOrginalBytes()

        self.item_list = []

        off = self.offset
        for i in range(self.item_count):
            # 解码子项
            item = self.section_type.baseitem()
            # item = self.createItem()
            # item.setBytes(bytes[off:])
            item_bytes_size = item.decode_bytes(bytes, off)
            # item_bytes_size = item.getBytesSize()

            # 添加子项
            self.item_list.append(item)

            # 偏移量更改
            off += item_bytes_size

        # 重新调整字节数组大小
        trim_bytes_size = off - self.offset
        if trim_bytes_size != self.item_size:
            assert self.item_size is None
            self.item_size = trim_bytes_size

            # self.setBytes(bytes[0x00:trim_bytes_size])

    def encode(self):
        """
        编码字节数组
        """
        # 重新计算大小，调整字节数组和子项数目
        new_size = 0
        for item in self.item_list:
            new_size += item.getBytesSize()
        new_size = self.trimBytesSize(new_size)

        if self.getBytesSize() != new_size:
            self.setBytes(createBytes(new_size))

        self.item_count = len(self.item_list)

        # 编码
        bytes = self.getBytes()

        off = 0
        for item in self.item_list:
            # 编码子项
            item.encode()
            item_bytes_size = item.getBytesSize()

            # 拷贝子项的字节数组
            # print item
            bytes[off:off + item_bytes_size] = item.getBytes()

            # 偏移量更改
            off += item_bytes_size

    def trimBytesSize(self, bytes_size):
        """ 重新调整字节数组大小 """
        return bytes_size

    def convertOffToId(self):
        """ 转换文件偏移量到相关的id """
        for item in self.item_list:
            item.convertOffToId(self.context)

    def convertIdToOff(self):
        """ 转换id到相关的文件偏移量 """
        for item in self.item_list:
            item.convertIdToOff(self.context)

    def convertIdToItem(self):
        """ 转换id到item对象 """
        for item in self.item_list:
            item.convertIdToItem(self.context)

    def convertItemToId(self):
        """ 转换item对象到id """
        for item in self.item_list:
            item.convertItemToId(self.context)

    # 重新排序
    # self.sortItemList()

    def sortItemList(self):
        self.item_list.sort(self.cmpItem)

    def cmpItem(self, item1, item2):
        return 0

    def getIdByOff(self, off):
        cur_off = 0
        for i in range(self.item_count):
            if cur_off == off:
                return i
            cur_off += self.item_list[i].getBytesSize()
        return -1

    def getOffById(self, id):
        if id >= self.item_count:
            return -1

        cur_off = 0
        for i in range(id):
            cur_off += self.item_list[i].getBytesSize()
        return cur_off

    def getItemById(self, id):
        if id >= 0 and id < len(self.item_list):
            return self.item_list[id]
        return None

    def getIdByItem(self, item):
        if not item is None:
            return self.item_list.index(item)
        return -1

    def getContextIdByOff(self, section_type, off):
        if self.context:
            return self.context.getSectionItemIdByOff(section_type, off)
        return -1

    def getContextOffById(self, section_type, id):
        if self.context:
            return self.context.getSectionItemOffById(section_type, id)
        return -1

    def createItem(self):
        """
        创建子项
        """
        return self.section_type.baseitem.create()
        # return item_class_map[self.section_type].create()

    def addItem(self, item):
        """
        增加子项
        """
        if not item in self.item_list:
            self.item_list.append(item)
            self.encode()

    def modify(self, item):
        """
        修改子项
        """
        if item in self.item_list:
            self.encode()

    def removeItem(self, item):
        """
        移除子项
        """
        if item in self.item_list:
            self.item_list.remove(item)
            self.encode()

    def getItemSize(self):
        """
        获取列表长度
        """
        return self.item_count

    def getItem(self, index):
        """
        获取子项
        index:    索引
        """
        if index < self.item_count:
            return self.item_list[index]

        return None

    def getItemDesc(self, index):
        """
        获取子项的字符串描述
        index: 索引
        """
        if index < self.item_count:
            item = self.item_list[index]
            return item.tostring()

        return '%.4d' % index

    def getItemString(self, index):
        """
        获取子项的字符串描述
        index: 索引
        """
        if index < len(self.item_list):
            item = self.item_list[index]
            return item.tostring()

        return '%.4d' % index

    def getContextDesc(self, section_type, index):
        """
        获取上下文的描述
        section_type:    section的类型
        index:           section中子项列表的索引
        """
        if self.context:
            return self.context.getSectionItemDesc(section_type, index)

        return '%.4d' % index

    def tostring(self):
        """
        转化为可打印的字符串
        """
        string = '-*-' * 30 + '\n'

        string += '%s ---> [%d]\n' % (self.section_type.strval, self.item_count)
        for i in range(self.item_count):
            # 使用item描述
            string += '%.4d: %s\n' % (i, self.getItemDesc(i))
        # 使用item自身的tostring()
        # string += '%.4d: %s\n' % (i, self.getItemString(i))

        string += '-*-' * 30 + '\n'

        return string

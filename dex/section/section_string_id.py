# -- coding: utf-8 --

from base import *


class StringIdListSection(BaseSection):
    """
    section: 字符串ids
    """

    @property
    def section_type(self):
        from common_type import TYPE_STRING_ID_ITEM
        return TYPE_STRING_ID_ITEM

    @property
    def bytes_size(self):
        return self.item_size*0x4

    # def __init__(self, context, bytes, size, off):
    #     """
    #     初始化
    #     context:    上下文信息
    #     bytes:      原始字节数组
    #     size:       项列表的总个数
    #     off:        字节数组偏移
    #     """
    #     super(StringIdListSection, self).__init__(context, bytes[off:off + size * 0x04], size)

    def cmpItem(self, item1, item2):
        if item1.string_data_id < item2.string_data_id:
            return -1
        elif item1.string_data_id > item2.string_data_id:
            return 1
        else:
            return 0

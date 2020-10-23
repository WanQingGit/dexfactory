# -- coding: utf-8 --

from section_base import *


class TypeIdListSection(BaseSection):
    """
    section: 类型id列表
    """
    @property
    def section_type(self):
        from common_type import TYPE_TYPE_ID_ITEM
        return TYPE_TYPE_ID_ITEM


    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:    上下文信息
        bytes:      原始字节数组
        size:       项列表的总个数
        off:        字节数组偏移
        """

        super(TypeIdListSection, self).__init__(context, bytes[off:], size)

    def getItemDesc(self, index):
        """
        获取类型字符串
        index:  索引
        """
        if index < self.item_size:
            from common_type import TYPE_STRING_DATA_ITEM
            return self.getContextDesc(TYPE_STRING_DATA_ITEM, self.item_list[index].string_id)

        return '%.4d' % index

    def cmpItem(self, item1, item2):
        if item1.string_id < item2.string_id:
            return -1
        elif item1.string_id > item2.string_id:
            return 1
        else:
            return 0

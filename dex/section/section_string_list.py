# -- coding: utf-8 --

from section_base import *


class StringListSection(BaseSection):
    """
    section: 字符串列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_STRING_DATA_ITEM
        return TYPE_STRING_DATA_ITEM

    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:    上下文信息
        bytes:      原始字节数组
        size:       总个数
        off:        字节数组偏移
        """

        super(StringListSection, self).__init__(context, bytes[off:], size)

    def cmpItem(self, item1, item2):
        if item1.string_data < item2.string_data:
            return -1
        elif item1.string_data > item2.string_data:
            return 1
        else:
            return 0

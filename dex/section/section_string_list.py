# -- coding: utf-8 --

from base import *


class StringListSection(BaseSection):
    """
    section: 字符串列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_STRING_DATA_ITEM
        return TYPE_STRING_DATA_ITEM


    def cmpItem(self, item1, item2):
        if item1.string_data < item2.string_data:
            return -1
        elif item1.string_data > item2.string_data:
            return 1
        else:
            return 0

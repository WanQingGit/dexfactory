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

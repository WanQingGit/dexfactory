# -- coding: utf-8 --

from section_base import *


class FieldIdListSection(BaseSection):
    """
    section: field ids列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_FIELD_ID_ITEM
        return TYPE_FIELD_ID_ITEM


    def getItemDesc(self, index):
        """
        获取proto id的字符串描述
        index: 索引
        """
        if index >= self.item_size:
            return ''

        item = self.item_list[index]

        from common_type import TYPE_TYPE_ID_ITEM
        class_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getClassId())
        type_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getTypeId())
        from common_type import TYPE_STRING_DATA_ITEM
        name_string = self.getContextDesc(TYPE_STRING_DATA_ITEM, item.getNameId())

        return '%s -> %s { %s }' % (class_string, name_string, type_string)

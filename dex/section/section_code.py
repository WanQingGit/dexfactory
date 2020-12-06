# -- coding: utf-8 --

from section_base import *


class CodeSection(BaseSection):
    """
    section: code_item
    """

    @property
    def section_type(self):
        from common_type import TYPE_CODE_ITEM
        return TYPE_CODE_ITEM


    def getItemDesc(self, index):
        """
        获取子项的字符串描述
        index: 索引
        """
        if index < self.item_size:
            item = self.item_list[index]
            return item.tostring(self.context)

        return '%.4d' % index

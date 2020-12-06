# -- coding: utf-8 --

from section_base import *


class MapItemListSection(BaseSection):
    """
    section: map 项列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_MAP_LIST
        return TYPE_MAP_LIST



    def getItemDataList(self):
        """
        获取子项的数据列表，每一项代表一个section的信息
        """
        return self.getItem(0).getItemDataList()

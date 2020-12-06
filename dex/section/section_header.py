# -- coding: utf-8 --

from section_base import *


class HeaderSection(BaseSection):
    """
    头部信息
    """
    item_size = 0x70

    @property
    def section_type(self):
        from common_type import TYPE_HEADER_ITEM
        return TYPE_HEADER_ITEM

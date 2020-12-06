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

    def check_head(self, header: 'common_type.HeaderItem'):
        self.item_count = self.context.header.string_ids_size
        self.offset = self.context.header.string_ids_off

    @property
    def bytes_size(self):
        return self.item_size * 0x4

    def cmpItem(self, item1, item2):
        if item1.string_data_id < item2.string_data_id:
            return -1
        elif item1.string_data_id > item2.string_data_id:
            return 1
        else:
            return 0

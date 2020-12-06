# -- coding: utf-8 --

from base import *


class ClassDefListSection(BaseSection):
    """
    section: class def列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_CLASS_DEF_ITEM
        return TYPE_CLASS_DEF_ITEM

    def check_head(self, header):
        assert self.offset == header.class_defs_off
        assert self.item_count == header.class_defs_size

    def getItemDesc(self, index):
        from common_type import TYPE_TYPE_ID_ITEM
        """
        获取proto id的字符串描述
        index: 索引
        """
        if index >= self.item_size:
            return ''

        item = self.item_list[index]

        class_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getClassId())
        super_class_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getSuperClassId())
        from common_type import TYPE_STRING_DATA_ITEM
        source_file_string = self.getContextDesc(TYPE_STRING_DATA_ITEM, item.getSourceFileId())

        string = ''

        # string += 'access: %.4x\n' % item.access_flags
        string += '[%s] extends [%s] in [%s]' % (class_string, super_class_string, source_file_string)
        from common_type import TYPE_CLASS_DATA_ITEM
        string += ' %s' % self.getContextDesc(TYPE_CLASS_DATA_ITEM, item.class_data_id)

        return string

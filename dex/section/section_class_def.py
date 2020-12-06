# -- coding: utf-8 --

from section_base import *


class ClassDefListSection(BaseSection):
    """
    section: class def列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_CLASS_DEF_ITEM
        return TYPE_CLASS_DEF_ITEM


    def getItemDesc(self, index):
        """
        获取proto id的字符串描述
        index: 索引
        """
        if index >= self.item_size:
            return ''

        item = self.item_list[index]

        class_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getClassId())
        super_class_string = self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getSuperClassId())
        source_file_string = self.getContextDesc(TYPE_STRING_DATA_ITEM, item.getSourceFileId())

        string = ''

        # string += 'access: %.4x\n' % item.access_flags
        string += '[%s] extends [%s] in [%s]' % (class_string, super_class_string, source_file_string)
        string += ' %s' % self.getContextDesc(TYPE_CLASS_DATA_ITEM, item.class_data_id)

        return string

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

    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:   上下文信息
        bytes:     原始字节数组
        size:      子项总个数
        off:       字节数组偏移
        """

        super(CodeSection, self).__init__(context, bytes[off:], size)

    def getItemDesc(self, index):
        """
        获取子项的字符串描述
        index: 索引
        """
        if index < self.item_size:
            item = self.item_list[index]
            return item.tostring(self.context)

        return '%.4d' % index

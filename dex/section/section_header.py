# -- coding: utf-8 --

from section_base import *


class HeaderSection(BaseSection):
    """
    头部信息
    """

    @property
    def section_type(self):
        from common_type import TYPE_HEADER_ITEM
        return TYPE_HEADER_ITEM

    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:   上下文信息
        bytes:     原始字节数组
        size:      子项总个数
        off:       字节数组偏移
        """

        super(HeaderSection, self).__init__(context, bytes[off:off + 0x70], size)

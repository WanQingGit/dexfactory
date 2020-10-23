# -- coding: utf-8 --

from section_base import *


class AnnotationSetRefListSection(BaseSection):
    """
    section: 注解引用列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_ANNOTATION_SET_REF_LIST
        return TYPE_ANNOTATION_SET_REF_LIST

    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:    上下文信息
        bytes:      原始字节数组
        size:       子项总个数
        off:        字节数组偏移
        """

        super(AnnotationSetRefListSection, self).__init__(context, bytes[off:], size)

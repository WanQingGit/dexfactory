# -- coding: utf-8 --

from base import *


class AnnotationSetRefListSection(BaseSection):
    """
    section: 注解引用列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_ANNOTATION_SET_REF_LIST
        return TYPE_ANNOTATION_SET_REF_LIST


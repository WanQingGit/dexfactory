# -- coding: utf-8 --

from section_base import *


class AnnotationSetItemSection(BaseSection):
    """
    section: annotation_set_item
    """

    @property
    def section_type(self):
        from common_type import TYPE_ANNOTATION_SET_ITEM
        return TYPE_ANNOTATION_SET_ITEM


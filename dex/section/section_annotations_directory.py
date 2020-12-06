# -- coding: utf-8 --

from section_base import *


class AnnotationsDirectorySection(BaseSection):
    """
    section: annotations_directory_item
    """

    @property
    def section_type(self):
        from common_type import TYPE_ANNOTATIONS_DIRECTORY_ITEM
        return TYPE_ANNOTATIONS_DIRECTORY_ITEM


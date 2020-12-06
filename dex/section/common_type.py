# -- coding: utf-8 --

"""
定义section的类型
"""
from item_map_list import *
from item_header import *
from item_string_id import *
from item_type_id import *
from item_proto_id import *
from item_field_id import *
from item_method_id import *
from item_class_def import *
from item_type_list import *
from item_string_data import *
from item_class_data import *
from item_annotation_set_ref_list import *
from item_annotation_set_item import *
from item_annotation_item import *
from item_encoded_array import *
from item_annotations_directory import *
from item_code import *
from item_debug_info import *

from section_map_item import *
from section_header import *
from section_string_id import *
from section_type_id import *
from section_proto_id import *
from section_field_id import *
from section_method_id import *
from section_class_def import *
from section_type_list import *
from section_class_data import *
from section_annotation_set_ref_list import *
from section_annotation_set_item import *
from section_annotation_item import *
from section_string_list import *
from section_encoded_array import *
from section_annotations_directory import *
from section_code import *
from section_debug_info import *

type_desc_map = {}


class SectionType(object):
    def __init__(self, val, strval, baseitem:BaseItem, section):
        self.val = val
        self.strval = strval
        self.baseitem = baseitem
        type_desc_map[val] = self
        self.section = section

    def __repr__(self):
        return self.strval

    def __hash__(self):
        return self.val.__hash__()

    def __eq__(self, other):
        if hasattr(other, 'val'):
            return self.val.__eq__(other.val)
        return self.val.__eq__(other)


TYPE_HEADER_ITEM = SectionType(0x0000, 'HeaderSection', HeaderItem, HeaderSection)
TYPE_STRING_ID_ITEM = SectionType(0x0001, 'StringIdListSection', StringIdItem, StringIdListSection)
TYPE_TYPE_ID_ITEM = SectionType(0x0002, 'TypeIdListSection', TypeIdItem, TypeIdListSection)
TYPE_PROTO_ID_ITEM = SectionType(0x0003, 'ProtoIdListSection', ProtoIdItem, ProtoIdListSection)
TYPE_FIELD_ID_ITEM = SectionType(0x0004, 'FieldIdListSection', FieldIdItem, FieldIdListSection)
TYPE_METHOD_ID_ITEM = SectionType(0x0005, 'MethodIdListSection', MethodIdItem, MethodIdListSection)
TYPE_CLASS_DEF_ITEM = SectionType(0x0006, 'ClassDefListSection', ClassDefItem, ClassDefListSection)
TYPE_MAP_LIST = SectionType(0x1000, 'MapItemListSection', MapListItem, MapItemListSection)
TYPE_TYPE_LIST = SectionType(0x1001, 'TypeListSection', TypeListItem, TypeListSection)
TYPE_ANNOTATION_SET_REF_LIST = SectionType(0x1002, 'AnnotationSetRefListSection', AnnotationSefRefListItem,
                                           AnnotationSetRefListSection)
TYPE_ANNOTATION_SET_ITEM = SectionType(0x1003, 'AnnotationSetItemSection', AnnotationSetItemItem,
                                       AnnotationSetItemSection)
TYPE_CLASS_DATA_ITEM = SectionType(0x2000, 'ClassDataListSection', ClassDataItem, ClassDataListSection)
TYPE_CODE_ITEM = SectionType(0x2001, 'CodeSection', CodeItem, CodeSection)
TYPE_STRING_DATA_ITEM = SectionType(0x2002, 'StringListSection', StringDataItem, StringListSection)
TYPE_DEBUG_INFO_ITEM = SectionType(0x2003, 'DebugInfoSection', DebugInfoItem, DebugInfoSection)
TYPE_ANNOTATION_ITEM = SectionType(0x2004, 'AnnotationItemSection', AnnotationItemItem, AnnotationItemSection)
TYPE_ENCODED_ARRAY_ITEM = SectionType(0x2005, 'EncodedArraySection', EncodedArrayItem, EncodedArraySection)
TYPE_ANNOTATIONS_DIRECTORY_ITEM = SectionType(0x2006, 'AnnotationsDirectorySection', AnnotationsDirectoryItem,
                                              AnnotationsDirectorySection)

"""
类型列表
"""
# type_list = [
#
#     TYPE_HEADER_ITEM,
#     TYPE_STRING_ID_ITEM,
#     TYPE_TYPE_ID_ITEM,
#     TYPE_PROTO_ID_ITEM,
#     TYPE_FIELD_ID_ITEM,
#     TYPE_METHOD_ID_ITEM,
#     TYPE_CLASS_DEF_ITEM,
#     TYPE_MAP_LIST,
#     TYPE_TYPE_LIST,
#     TYPE_ANNOTATION_SET_REF_LIST,
#     TYPE_ANNOTATION_SET_ITEM,
#     TYPE_CLASS_DATA_ITEM,
#     TYPE_CODE_ITEM,
#     TYPE_STRING_DATA_ITEM,
#     TYPE_DEBUG_INFO_ITEM,
#     TYPE_ANNOTATION_ITEM,
#     TYPE_ENCODED_ARRAY_ITEM,
#     TYPE_ANNOTATIONS_DIRECTORY_ITEM,
#
# ]

"""
类型的描述表:  (类型， 类型描述)
"""
# type_desc_map = {
#
#     TYPE_HEADER_ITEM: 'HeaderSection',
#     TYPE_STRING_ID_ITEM: 'StringIdListSection',
#     TYPE_TYPE_ID_ITEM: 'TypeIdListSection',
#     TYPE_PROTO_ID_ITEM: 'ProtoIdListSection',
#     TYPE_FIELD_ID_ITEM: 'FieldIdListSection',
#     TYPE_METHOD_ID_ITEM: 'MethodIdListSection',
#     TYPE_CLASS_DEF_ITEM: 'ClassDefListSection',
#     TYPE_MAP_LIST: 'MapItemListSection',
#     TYPE_TYPE_LIST: 'TypeListSection',
#     TYPE_ANNOTATION_SET_REF_LIST: 'AnnotationSetRefListSection',
#     TYPE_ANNOTATION_SET_ITEM: 'AnnotationSetItemSection',
#     TYPE_CLASS_DATA_ITEM: 'ClassDataListSection',
#     TYPE_CODE_ITEM: 'CodeSection',
#     TYPE_STRING_DATA_ITEM: 'StringListSection',
#     TYPE_DEBUG_INFO_ITEM: 'DebugInfoSection',
#     TYPE_ANNOTATION_ITEM: 'AnnotationItemSection',
#     TYPE_ENCODED_ARRAY_ITEM: 'EncodedArraySection',
#     TYPE_ANNOTATIONS_DIRECTORY_ITEM: 'AnnotationsDirectorySection',
#
# }

"""
section中子项类的映射表: (类型，Item类)
"""
# item_class_map = {
#
# 	TYPE_HEADER_ITEM                   :    HeaderItem,
# 	TYPE_STRING_ID_ITEM                :    StringIdItem,
# 	TYPE_TYPE_ID_ITEM                  :    TypeIdItem,
# 	TYPE_PROTO_ID_ITEM                 :    ProtoIdItem,
# 	TYPE_FIELD_ID_ITEM                 :    FieldIdItem,
# 	TYPE_METHOD_ID_ITEM                :    MethodIdItem,
# 	TYPE_CLASS_DEF_ITEM                :    ClassDefItem,
# 	TYPE_MAP_LIST                      :    MapListItem,
# 	TYPE_TYPE_LIST                     :    TypeListItem,
# 	TYPE_ANNOTATION_SET_REF_LIST       :    AnnotationSefRefListItem,
# 	TYPE_ANNOTATION_SET_ITEM           :    AnnotationSetItemItem,
# 	TYPE_CLASS_DATA_ITEM               :    ClassDataItem,
# 	TYPE_CODE_ITEM                     :    CodeItem,
# 	TYPE_STRING_DATA_ITEM              :    StringDataItem,
# 	TYPE_DEBUG_INFO_ITEM               :    DebugInfoItem,
# 	TYPE_ANNOTATION_ITEM               :    AnnotationItemItem,
# 	TYPE_ENCODED_ARRAY_ITEM            :    EncodedArrayItem,
# 	TYPE_ANNOTATIONS_DIRECTORY_ITEM    :    AnnotationsDirectoryItem,
#
# }
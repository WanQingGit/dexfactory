# -- coding: utf-8 --

from base import *


class DebugInfoSection(BaseSection):
    """
    section: debug_info_item
    """

    @property
    def section_type(self):
        from common_type import TYPE_DEBUG_INFO_ITEM
        return TYPE_DEBUG_INFO_ITEM


# def decode(self):
# 	"""
# 	解码字节数组
# 	"""
# 	bytes = self.getBytes()

# 	self.item_list = []

# def encode(self):
# 	"""
# 	编码字节数组
# 	"""
# 	pass

# def getItemDesc(self, index):
# 	"""
# 	获取子项的字符串描述
# 	index: 索引
# 	"""
# 	return '%.4d' % index

# def tostring(self):
# 	return 'TYPE_DEBUG_INFO_ITEM: %.4x' % TYPE_DEBUG_INFO_ITEM, self.tohexstring()

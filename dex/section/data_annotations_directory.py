# -- coding: utf-8 --

from base import *
from common_tool import convertIntToBytes


class FieldAnnotationData(BaseData):
	item_size = 0x8

	def decode(self, bytes, off):
		"""
		解码字节数组
		"""
		bytes = bytes[0:self.item_size]
		self.field_id = convertBytesToInt(bytes[0x00:0x04])

		# 指向annotation_set_item
		self.annotations_off = convertBytesToInt(bytes[0x04:0x08])
		self.annotations_id = -1
		self.annotations_item = None

	# 重新调整字节数组大小
	# self.setBytes(bytes[0x00:0x08])

	def encode(self):
		"""
		将变量重新写入到字节数组中
		"""
		bytes = self.bytes

		bytes[0x00:0x04] = convertIntToBytes(self.field_id)
		bytes[0x04:0x08] = convertIntToBytes(self.annotations_off)

	def convertOffToId(self, context):
		""" 转换文件偏移量到相关的id """
		self.annotations_id = context.getSectionItemIdByOff(TYPE_ANNOTATION_SET_ITEM, self.annotations_off)

	def convertIdToOff(self, context):
		""" 转换id到相关的文件偏移量 """
		self.annotations_off = context.getSectionItemOffById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertIdToItem(self, context):
		""" 转换id到item对象 """
		self.annotations_item = context.getSectionItemById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertItemToId(self, context):
		""" 转换item对象到id """
		self.annotations_id = context.getSectionIdByItem(TYPE_ANNOTATION_SET_ITEM, self.annotations_item)

	def tostring(self):
		"""
		转换为可打印的字符串
		"""
		string = ''

		string += 'field_id: %.4d' % self.field_id
		string += 'annotations: [%.4x %.4d]' % (self.annotations_off, self.annotations_id)

		return string


class MethodAnnotationData(BaseData):
	item_size = 0x08
	"""
	data: method_annotation
	"""

	def decode(self,bytes,off):
		"""
		解码字节数组
		"""
		bytes=bytes[:self.item_size]
		self.method_id = convertBytesToInt(bytes[0x00:0x04])

		# 指向annotation_set_item
		self.annotations_off = convertBytesToInt(bytes[0x04:0x08])
		self.annotations_id = -1
		self.annotations_item = None

		# 重新调整字节数组大小
		self.setBytes(bytes[0x00:0x08])

	def encode(self):
		"""
		将变量重新写入到字节数组中
		"""
		bytes = self.bytes

		bytes[0x00:0x04] = convertIntToBytes(self.method_id)
		bytes[0x04:0x08] = convertIntToBytes(self.annotations_off)

	def convertOffToId(self, context):
		""" 转换文件偏移量到相关的id """
		self.annotations_id = context.getSectionItemIdByOff(TYPE_ANNOTATION_SET_ITEM, self.annotations_off)

	def convertIdToOff(self, context):
		""" 转换id到相关的文件偏移量 """
		self.annotations_off = context.getSectionItemOffById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertIdToItem(self, context):
		""" 转换id到item对象 """
		self.annotations_item = context.getSectionItemById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertItemToId(self, context):
		""" 转换item对象到id """
		self.annotations_id = context.getSectionIdByItem(TYPE_ANNOTATION_SET_ITEM, self.annotations_item)

	def tostring(self):
		"""
		转换为可打印的字符串
		"""
		string = ''

		string += 'field_id: %.4d' % self.method_id
		string += 'annotations: [%.4x %.4d]' % (self.annotations_off, self.annotations_id)

		return string


class ParameterAnnotationData(BaseData):
	"""
	data: parameter_annotation
	"""
	item_size = 0x08

	def decode(self,bytes,off):
		"""
		解码字节数组
		"""
		bytes = bytes[:self.item_size]

		self.method_id = convertBytesToInt(bytes[0x00:0x04])

		# 指向annotation_set_ref_list
		self.annotations_off = convertBytesToInt(bytes[0x04:0x08])
		self.annotations_id = -1
		self.annotations_item = None


	def encode(self):
		"""
		将变量重新写入到字节数组中
		"""
		bytes = self.bytes

		bytes[0x00:0x04] = convertIntToBytes(self.method_id)
		bytes[0x04:0x08] = convertIntToBytes(self.annotations_off)

	def convertOffToId(self, context):
		""" 转换文件偏移量到相关的id """
		self.annotations_id = context.getSectionItemIdByOff(TYPE_ANNOTATION_SET_ITEM, self.annotations_off)

	def convertIdToOff(self, context):
		""" 转换id到相关的文件偏移量 """
		self.annotations_off = context.getSectionItemOffById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertIdToItem(self, context):
		""" 转换id到item对象 """
		self.annotations_item = context.getSectionItemById(TYPE_ANNOTATION_SET_ITEM, self.annotations_id)

	def convertItemToId(self, context):
		""" 转换item对象到id """
		self.annotations_id = context.getSectionIdByItem(TYPE_ANNOTATION_SET_ITEM, self.annotations_item)

	def tostring(self):
		"""
		转换为可打印的字符串
		"""
		string = ''

		string += 'field_id: %.4d' % self.method_id
		string += 'annotations: [%.4x %.4d]' % (self.annotations_off, self.annotations_id)

		return string

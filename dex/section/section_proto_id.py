# -- coding: utf-8 --

from section_base import *


class ProtoIdListSection(BaseSection):
    """
    section: proto ids列表
    """

    @property
    def section_type(self):
        from common_type import TYPE_PROTO_ID_ITEM
        return TYPE_PROTO_ID_ITEM

    def __init__(self, context, bytes, size, off):
        """
        初始化
        context:    上下文信息
        bytes:      原始字节数组
        size:       项列表的总个数
        off:        字节数组偏移
        """

        super(ProtoIdListSection, self).__init__(context, bytes[off:], size)

    def getItemDesc(self, index):
        """
        获取proto id的字符串描述
        index: 索引
        """
        if index >= self.item_size:
            return ''

        item = self.item_list[index]

        string = ''

        from common_type import TYPE_TYPE_ID_ITEM
        string += '%s' % self.getContextDesc(TYPE_TYPE_ID_ITEM, item.getReturnTypeId())
        from common_type import TYPE_STRING_DATA_ITEM
        string += ' %s' % self.getContextDesc(TYPE_STRING_DATA_ITEM, item.getNameId())
        if item.param_id >= 0:
            from common_type import TYPE_TYPE_LIST
            string += '(%s)' % self.getContextDesc(TYPE_TYPE_LIST, item.param_id)
        else:
            string += '()'

        return string

# -- coding: utf-8 --

from base import *


class ClassDataListSection(BaseSection):
    """
    section: class data列表
    """
    @property
    def section_type(self):
        from common_type import TYPE_CLASS_DATA_ITEM
        return TYPE_CLASS_DATA_ITEM


    def trimBytesSize(self, bytes_size):
        """ 重新调整字节数组大小 """
        if bytes_size % 0x04 != 0:
            bytes_size += 0x04 - (bytes_size % 0x04)

        return bytes_size

    def getItemDesc(self, index):
        """
        获取class data的字符串描述
        index: 索引
        """
        # 获取属性和方法的列表
        if index >= self.item_size:
            return ''

        item = self.item_list[index]

        static_field_list = item.getStaticFieldList()
        instance_field_list = item.getInstanceFieldList()
        direct_method_list = item.getDirectMethodList()
        virtual_method_list = item.getVirtualMethodList()

        # 字符串描述
        string = '{\n'

        string += 'static_field_size: %.4d\n' % len(static_field_list)
        if len(static_field_list) > 0:
            string += '    [\n'
            for item in static_field_list:
                string += ' ' * 8 + self.getContextDesc(TYPE_FIELD_ID_ITEM, item.getFieldId()) + '\n'
            string += '    ]\n'

        string += 'instance_field_size: %.4d\n' % len(instance_field_list)
        if len(instance_field_list) > 0:
            string += '    [\n'
            for item in instance_field_list:
                string += ' ' * 8 + self.getContextDesc(TYPE_FIELD_ID_ITEM, item.getFieldId()) + '\n'
            string += '    ]\n'

        string += 'direct_method_size: %.4d\n' % len(direct_method_list)
        if len(direct_method_list) > 0:
            string += '    [\n'
            for item in direct_method_list:
                string += ' ' * 8 + self.getContextDesc(TYPE_METHOD_ID_ITEM, item.getMethodId()) + '\n'
            string += '    ]\n'

        string += 'virtual_method_size: %.4d\n' % len(virtual_method_list)
        if len(virtual_method_list) > 0:
            string += '    [\n'
            for item in virtual_method_list:
                string += ' ' * 8 + self.getContextDesc(TYPE_METHOD_ID_ITEM, item.getMethodId()) + '\n'
            string += '    ]\n'

        string += '}\n'

        return string

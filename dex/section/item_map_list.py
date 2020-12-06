# -- coding: utf-8 --
from data_map_list import MapListItemData
from base import *
from odex.section.tool import convertIntToBytes, convertBytesToInt


class MapListItem(BaseSectionItem):
    ItemData = MapListItemData
    """
    section子结构: 映射项信息
    """


    # def decode(self, bytes=None, off=None):
    #     """
    #     解码字节数组
    #     """
    #
    #     self.item_count = convertBytesToInt(bytes[off:off + 0x04])
    #     self.item_list = []
    #
    #     off += 0x04
    #     for i in range(self.item_count):
    #         # 解码子项数据
    #         item = MapListItemData()  # bytes[off:off + 0x0c]
    #         assert item.decode_bytes(bytes, off) == 0xc
    #         # 添加数据列表
    #         self.item_list.append(item)
    #         # 偏移量增加（往前移动12个字节）
    #         off += 0x0c
    #     self.item_size = off - self.offset

    def encode(self):
        """
        将变量重新写入到字节数组中
        """
        # 检测尺寸变化
        new_size = 0x04 + len(self.item_list) * 0x0c
        if self.getBytesSize() != new_size:
            self.setBytes(createBytes(new_size))

        bytes = self.getBytes()

        # 记录尺寸
        bytes[0x00:0x04] = convertIntToBytes(self.item_size)

        # 循环拷贝列表数据
        off = 0x04
        for item in self.item_list:
            bytes[off:off + 0x0c] = item.bytes
            off += 0x0c

    def getItemDataList(self):
        """
        获取子项的数据列表，每一项代表一个section的信息
        """
        return self.item_list

    def tostring(self):
        """
        转换为可打印的字符串
        """
        string = 'map_list_item_size: %d\n' % self.item_size
        for item in self.item_list:
            string += item.tostring() + '\n'

        return string

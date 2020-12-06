# -- coding: utf-8 --

from dex.dexinfo import DexInfo, TYPE_CODE_ITEM, TYPE_CLASS_DEF_ITEM, ClassDefListSection, ClassDefItem
from disassemble.insns import Insns
from odex.section.tool import convertBytesToHexStr

dex_path = './data/classes.dex'
context = DexInfo(dex_path)

class_item_section: ClassDefListSection = context.getSection(TYPE_CLASS_DEF_ITEM)
for i in range(class_item_section.item_count):
    class_item_section.getItemDesc(i)
    class_item: ClassDefItem = class_item_section.getItem(i)
    # class_item.get

######################################################################
"""
反汇编
"""
code_item_section = context.getSection(TYPE_CODE_ITEM)

# 反汇编
for item in code_item_section.item_list:
    print('[', convertBytesToHexStr(item.insns), ']')
    insns = Insns(item.insns)
    print(insns.tostring(context))

# 将反汇编解析类挂接到context中
context.setInsnsClass(Insns)
print(code_item_section.tostring())

######################################################################

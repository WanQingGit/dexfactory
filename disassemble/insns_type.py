# -- coding: utf-8 --

"""
该文件定义反汇编相关的各种类型
"""

"""
指令码映射集合
"""

"""
常量池类型定义
"""
# 空类型
KIND_NONE = ''
# 字符串池索引
KIND_STRING = 'string'
# 类型池索引
KIND_TYPE = 'type'
# 字段池索引
KIND_FIELD = 'field'
# 方法池索引
KIND_METHOD = 'meth'
# 调用点索引
KIND_SITE = 'site'
# 原型池索引
KIND_PROTO = 'proto'
# vtable 偏移
KIND_VTABLE = 'vtaboff'
# 字段偏移
KIND_FIELDOFF = 'fieldoff'
op_map = {}


class Op(object):
    def __init__(self, val, format, strval, kind):
        self.val = val
        self.strval = strval
        self.kind = kind
        self.format = format
        op_map[val] = self

    def __repr__(self):
        return self.strval

    def __hash__(self):
        return self.val.__hash__()

    def __eq__(self, val):
        return self.val.__eq__(val)

    def formatOp(self):
        return '%-24s' % self.strval


Op(0x00, '10x', 'nop', KIND_NONE)
Op(0x01, '12x', 'move', KIND_NONE)
Op(0x02, '22x', 'move/from16', KIND_NONE)
Op(0x03, '32x', 'move/16', KIND_NONE)
Op(0x04, '12x', 'move-wide', KIND_NONE)
Op(0x05, '22x', 'move-wide/from16', KIND_NONE)
Op(0x06, '32x', 'move-wide/16', KIND_NONE)
Op(0x07, '12x', 'move-object', KIND_NONE)
Op(0x08, '22x', 'move-object/from16', KIND_NONE)
Op(0x09, '32x', 'move-object/16', KIND_NONE)
Op(0x0A, '11x', 'move-result', KIND_NONE)
Op(0x0B, '11x', 'move-result-wide', KIND_NONE)
Op(0x0C, '11x', 'move-result-object', KIND_NONE)
Op(0x0D, '11x', 'move-exception', KIND_NONE)
Op(0x0E, '10x', 'return-void', KIND_NONE)
Op(0x0F, '11x', 'return', KIND_NONE)

Op(0x10, '11x', 'return-wide', KIND_NONE)
Op(0x11, '11x', 'return-object', KIND_NONE)
Op(0x12, '11n', 'const/4', KIND_NONE)
Op(0x13, '21s', 'const/16', KIND_NONE)
Op(0x14, '31i', 'const', KIND_NONE)
Op(0x15, '21h', 'const/high16', KIND_NONE)
Op(0x16, '21s', 'const-wide/16', KIND_NONE)
Op(0x17, '31i', 'const-wide/32', KIND_NONE)
Op(0x18, '51l', 'const-wide', KIND_NONE)
Op(0x19, '21h', 'const-wide/high16', KIND_NONE)
Op(0x1A, '21c', 'const-string', KIND_STRING)
Op(0x1B, '31c', 'const-string-jumbo', KIND_STRING)
Op(0x1C, '21c', 'const-class', KIND_TYPE)
Op(0x1D, '11x', 'monitor-enter', KIND_NONE)
Op(0x1E, '11x', 'monitor-exit', KIND_NONE)
Op(0x1F, '21c', 'check-cast', KIND_TYPE)

Op(0x20, '22c', 'instance-of', KIND_TYPE)
Op(0x21, '12x', 'array-length', KIND_NONE)
Op(0x22, '21c', 'new-instance', KIND_TYPE)
Op(0x23, '22c', 'new-array', KIND_TYPE)
Op(0x24, '35c', 'filled-new-array', KIND_TYPE)
Op(0x25, '3rc', 'filled-new-array-range', KIND_TYPE)
Op(0x26, '31t', 'fill-array-data', KIND_NONE)
Op(0x27, '11x', 'throw', KIND_NONE)
Op(0x28, '10t', 'goto', KIND_NONE)
Op(0x29, '20t', 'goto/16', KIND_NONE)
Op(0x2A, '30t', 'goto/32', KIND_NONE)
Op(0x2B, '31t', 'packed-switch', KIND_NONE)
Op(0x2C, '31t', 'sparse-switch', KIND_NONE)
Op(0x2D, '23x', 'cmpl-float', KIND_NONE)
Op(0x2E, '23x', 'cmpg-float', KIND_NONE)
Op(0x2F, '23x', 'cmpl-double', KIND_NONE)

Op(0x30, '23x', 'cmpg-double', KIND_NONE)
Op(0x31, '23x', 'cmp-long', KIND_NONE)
Op(0x32, '22t', 'if-eq', KIND_NONE)
Op(0x33, '22t', 'if-ne', KIND_NONE)
Op(0x34, '22t', 'if-lt', KIND_NONE)
Op(0x35, '22t', 'if-ge', KIND_NONE)
Op(0x36, '22t', 'if-gt', KIND_NONE)
Op(0x37, '22t', 'if-le', KIND_NONE)
Op(0x38, '21t', 'if-eqz', KIND_NONE)
Op(0x39, '21t', 'if-nez', KIND_NONE)
Op(0x3A, '21t', 'if-ltz', KIND_NONE)
Op(0x3B, '21t', 'if-gez', KIND_NONE)
Op(0x3C, '21t', 'if-gtz', KIND_NONE)
Op(0x3D, '21t', 'if-lez', KIND_NONE)
Op(0x3E, '', 'unused', KIND_NONE)
Op(0x3F, '', 'unused', 'unused')

Op(0x40, '', 'unused', KIND_NONE)
Op(0x41, '', 'unused', KIND_NONE)
Op(0x42, '', 'unused', KIND_NONE)
Op(0x43, '', 'unused', KIND_NONE)
Op(0x44, '23x', 'aget', KIND_NONE)
Op(0x45, '23x', 'aget-wide', KIND_NONE)
Op(0x46, '23x', 'aget-object', KIND_NONE)
Op(0x47, '23x', 'aget-boolean', KIND_NONE)
Op(0x48, '23x', 'aget-byte', KIND_NONE)
Op(0x49, '23x', 'aget-char', KIND_NONE)
Op(0x4A, '23x', 'aget-short', KIND_NONE)
Op(0x4B, '23x', 'aput', KIND_NONE)
Op(0x4C, '23x', 'aput-wide', KIND_NONE)
Op(0x4D, '23x', 'aput-object', KIND_NONE)
Op(0x4E, '23x', 'aput-boolean', KIND_NONE)
Op(0x4F, '23x', 'aput-byte', KIND_NONE)

Op(0x50, '23x', 'aput-char', KIND_NONE)
Op(0x51, '23x', 'aput-short', KIND_NONE)
Op(0x52, '22c', 'iget', KIND_FIELD)
Op(0x53, '22c', 'iget-wide', KIND_FIELD)
Op(0x54, '22c', 'iget-object', KIND_FIELD)
Op(0x55, '22c', 'iget-boolean', KIND_FIELD)
Op(0x56, '22c', 'iget-byte', KIND_FIELD)
Op(0x57, '22c', 'iget-char', KIND_FIELD)
Op(0x58, '22c', 'iget-short', KIND_FIELD)
Op(0x59, '22c', 'iput', KIND_FIELD)
Op(0x5A, '22c', 'iput-wide', KIND_FIELD)
Op(0x5B, '22c', 'iput-object', KIND_FIELD)
Op(0x5C, '22c', 'iput-boolean', KIND_FIELD)
Op(0x5D, '22c', 'iput-byte', KIND_FIELD)
Op(0x5E, '22c', 'iput-char', KIND_FIELD)
Op(0x5F, '22c', 'iput-short', KIND_FIELD)

Op(0x60, '21c', 'sget', KIND_FIELD)
Op(0x61, '21c', 'sget-wide', KIND_FIELD)
Op(0x62, '21c', 'sget-object', KIND_FIELD)
Op(0x63, '21c', 'sget-boolean', KIND_FIELD)
Op(0x64, '21c', 'sget-byte', KIND_FIELD)
Op(0x65, '21c', 'sget-char', KIND_FIELD)
Op(0x66, '21c', 'sget-short', KIND_FIELD)
Op(0x67, '21c', 'sput', KIND_FIELD)
Op(0x68, '21c', 'sput-wide', KIND_FIELD)
Op(0x69, '21c', 'sput-object', KIND_FIELD)
Op(0x6A, '21c', 'sput-boolean', KIND_FIELD)
Op(0x6B, '21c', 'sput-byte', KIND_FIELD)
Op(0x6C, '21c', 'sput-char', KIND_FIELD)
Op(0x6D, '21c', 'sput-short', KIND_FIELD)
Op(0x6E, '35c', 'invoke-virtual', KIND_METHOD)
Op(0x6F, '35c', 'invoke-super', KIND_METHOD)

Op(0x70, '35c', 'invoke-direct', KIND_METHOD)
Op(0x71, '35c', 'invoke-static', KIND_METHOD)
Op(0x72, '35c', 'invoke-interface', KIND_METHOD)
Op(0x73, '10x', 'unused', KIND_NONE)
Op(0x74, '3rc', 'invoke-virtual/range', KIND_METHOD)
Op(0x75, '3rc', 'invoke-super/range', KIND_METHOD)
Op(0x76, '3rc', 'invoke-direct/range', KIND_METHOD)
Op(0x77, '3rc', 'invoke-static/range', KIND_METHOD)
Op(0x78, '3rc', 'invoke-interface-range', KIND_METHOD)
Op(0x79, '', 'unused', KIND_NONE)
Op(0x7A, '', 'unused', KIND_NONE)
Op(0x7B, '12x', 'neg-int', KIND_NONE)
Op(0x7C, '12x', 'not-long', KIND_NONE)
Op(0x7D, '12x', 'neg-long', KIND_NONE)
Op(0x7E, '12x', 'not-long', KIND_NONE)
Op(0x7F, '12x', 'neg-float', KIND_NONE)

Op(0x80, '12x', 'neg-double', KIND_NONE)
Op(0x81, '12x', 'int-to-long', KIND_NONE)
Op(0x82, '12x', 'int-to-float', KIND_NONE)
Op(0x83, '12x', 'int-to-double', KIND_NONE)
Op(0x84, '12x', 'long-to-int', KIND_NONE)
Op(0x85, '12x', 'long-to-float', KIND_NONE)
Op(0x86, '12x', 'long-to-double', KIND_NONE)
Op(0x87, '12x', 'float-to-int', KIND_NONE)
Op(0x88, '12x', 'float-to-long', KIND_NONE)
Op(0x89, '12x', 'float-to-double', KIND_NONE)
Op(0x8A, '12x', 'double-to-int', KIND_NONE)
Op(0x8B, '12x', 'double-to-long', KIND_NONE)
Op(0x8C, '12x', 'double-to-float', KIND_NONE)
Op(0x8D, '12x', 'int-to-byte', KIND_NONE)
Op(0x8E, '12x', 'int-to-char', KIND_NONE)
Op(0x8F, '12x', 'int-to-short', KIND_NONE)

Op(0x90, '23x', 'add-int', KIND_NONE)
Op(0x91, '23x', 'sub-int', KIND_NONE)
Op(0x92, '23x', 'mul-int', KIND_NONE)
Op(0x93, '23x', 'div-int', KIND_NONE)
Op(0x94, '23x', 'rem-int', KIND_NONE)
Op(0x95, '23x', 'and-int', KIND_NONE)
Op(0x96, '23x', 'or-int', KIND_NONE)
Op(0x97, '23x', 'xor-int', KIND_NONE)
Op(0x98, '23x', 'shl-int', KIND_NONE)
Op(0x99, '23x', 'shr-int', KIND_NONE)
Op(0x9A, '23x', 'ushr-int', KIND_NONE)
Op(0x9B, '23x', 'add-long', KIND_NONE)
Op(0x9C, '23x', 'sub-long', KIND_NONE)
Op(0x9D, '23x', 'mul-long', KIND_NONE)
Op(0x9E, '23x', 'div-long', KIND_NONE)
Op(0x9F, '23x', 'rem-long', KIND_NONE)

Op(0xA0, '23x', 'and-long', KIND_NONE)
Op(0xA1, '23x', 'or-long', KIND_NONE)
Op(0xA2, '23x', 'xor-long', KIND_NONE)
Op(0xA3, '23x', 'shl-long', KIND_NONE)
Op(0xA4, '23x', 'shr-long', KIND_NONE)
Op(0xA5, '23x', 'ushr-long', KIND_NONE)
Op(0xA6, '23x', 'add-float', KIND_NONE)
Op(0xA7, '23x', 'sub-float', KIND_NONE)
Op(0xA8, '23x', 'mul-float', KIND_NONE)
Op(0xA9, '23x', 'div-float', KIND_NONE)
Op(0xAA, '23x', 'rem-float', KIND_NONE)
Op(0xAB, '23x', 'add-double', KIND_NONE)
Op(0xAC, '23x', 'sub-double', KIND_NONE)
Op(0xAD, '23x', 'mul-double', KIND_NONE)
Op(0xAE, '23x', 'div-double', KIND_NONE)
Op(0xAF, '23x', 'rem-double', KIND_NONE)

Op(0xB0, '12x', 'add-int/2addr', KIND_NONE)
Op(0xB1, '12x', 'sub-int/2addr', KIND_NONE)
Op(0xB2, '12x', 'mul-int/2addr', KIND_NONE)
Op(0xB3, '12x', 'div-int/2addr', KIND_NONE)
Op(0xB4, '12x', 'rem-int/2addr', KIND_NONE)
Op(0xB5, '12x', 'and-int/2addr', KIND_NONE)
Op(0xB6, '12x', 'or-int/2addr', KIND_NONE)
Op(0xB7, '12x', 'xor-int/2addr', KIND_NONE)
Op(0xB8, '12x', 'shl-int/2addr', KIND_NONE)
Op(0xB9, '12x', 'shr-int/2addr', KIND_NONE)
Op(0xBA, '12x', 'ushr-int/2addr', KIND_NONE)
Op(0xBB, '12x', 'add-long/2addr', KIND_NONE)
Op(0xBC, '12x', 'sub-long/2addr', KIND_NONE)
Op(0xBD, '12x', 'mul-long/2addr', KIND_NONE)
Op(0xBE, '12x', 'div-long/2addr', KIND_NONE)
Op(0xBF, '12x', 'rem-long/2addr', KIND_NONE)

Op(0xC0, '12x', 'and-long/2addr', KIND_NONE)
Op(0xC1, '12x', 'or-long/2addr', KIND_NONE)
Op(0xC2, '12x', 'xor-long/2addr', KIND_NONE)
Op(0xC3, '12x', 'shl-long/2addr', KIND_NONE)
Op(0xC4, '12x', 'shr-long/2addr', KIND_NONE)
Op(0xC5, '12x', 'ushr-long/2addr', KIND_NONE)
Op(0xC6, '12x', 'add-float/2addr', KIND_NONE)
Op(0xC7, '12x', 'sub-float/2addr', KIND_NONE)
Op(0xC8, '12x', 'mul-float/2addr', KIND_NONE)
Op(0xC9, '12x', 'div-float/2addr', KIND_NONE)
Op(0xCA, '12x', 'rem-float/2addr', KIND_NONE)
Op(0xCB, '12x', 'add-double/2addr', KIND_NONE)
Op(0xCC, '12x', 'sub-double/2addr', KIND_NONE)
Op(0xCD, '12x', 'mul-double/2addr', KIND_NONE)
Op(0xCE, '12x', 'div-double/2addr', KIND_NONE)
Op(0xCF, '12x', 'rem-double/2addr', KIND_NONE)

Op(0xD0, '22s', 'add-int/lit16', KIND_NONE)
Op(0xD1, '22s', 'sub-int/lit16', KIND_NONE)
Op(0xD2, '22s', 'mul-int/lit16', KIND_NONE)
Op(0xD3, '22s', 'div-int/lit16', KIND_NONE)
Op(0xD4, '22s', 'rem-int/lit16', KIND_NONE)
Op(0xD5, '22s', 'and-int/lit16', KIND_NONE)
Op(0xD6, '22s', 'or-int/lit16', KIND_NONE)
Op(0xD7, '22s', 'xor-int/lit16', KIND_NONE)
Op(0xD8, '22b', 'add-int/lit8', KIND_NONE)
Op(0xD9, '22b', 'sub-int/lit8', KIND_NONE)
Op(0xDA, '22b', 'mul-int/lit8', KIND_NONE)
Op(0xDB, '22b', 'div-int/lit8', KIND_NONE)
Op(0xDC, '22b', 'rem-int/lit8', KIND_NONE)
Op(0xDD, '22b', 'and-int/lit8', KIND_NONE)
Op(0xDE, '22b', 'or-int/lit8', KIND_NONE)
Op(0xDF, '22b', 'xor-int/lit8', KIND_NONE)

Op(0xE0, '22b', 'shl-int/lit8', KIND_NONE)
Op(0xE1, '22b', 'shr-int/lit8', KIND_NONE)
Op(0xE2, '22b', 'ushr-int/lit8', KIND_NONE)
Op(0xE3, '', 'unused', KIND_NONE)
Op(0xE4, '', 'unused', KIND_NONE)
Op(0xE5, '', 'unused', KIND_NONE)
Op(0xE6, '', 'unused', KIND_NONE)
Op(0xE7, '', 'unused', KIND_NONE)
Op(0xE8, '', 'unused', KIND_NONE)
Op(0xE9, '', 'unused', KIND_NONE)
Op(0xEA, '', 'unused', KIND_NONE)
Op(0xEB, '', 'unused', KIND_NONE)
Op(0xEC, '', 'unused', KIND_NONE)
Op(0xED, '', 'unused', KIND_NONE)
Op(0xEE, '', 'execute-inline', KIND_NONE)
Op(0xEF, '', 'unused', KIND_NONE)

Op(0xF0, '', 'invoke-direct-empty', KIND_NONE)
Op(0xF1, '', 'unused', KIND_NONE)
Op(0xF2, '', 'iget-quick', KIND_NONE)
Op(0xF3, '', 'iget-wide-quick', KIND_NONE)
Op(0xF4, '', 'iget-object-quick', KIND_NONE)
Op(0xF5, '', 'iput-quick', KIND_NONE)
Op(0xF6, '', 'iput-wide-quick', KIND_NONE)
Op(0xF7, '', 'iput-object-quick', KIND_NONE)
Op(0xF8, '', 'invoke-virtual-quick', KIND_NONE)
Op(0xF9, '', 'invoke-virtual-quick/range', KIND_NONE)
Op(0xFA, '45cc', 'invoke-super-quick', KIND_METHOD)
Op(0xFB, '4rcc', 'invoke-super-quick/range', KIND_METHOD)
Op(0xFC, '35c', 'unused', KIND_NONE)
Op(0xFD, '3rc', 'unused', KIND_NONE)
Op(0xFE, '10x', 'unused', KIND_NONE)
Op(0xFF, '10x', 'unused', KIND_NONE)

# op_map = {
#
#     0x00: 'nop',
#     0x01: 'move',
#     0x02: 'move/from16',
#     0x03: 'move/16',
#     0x04: 'move-wide',
#     0x05: 'move-wide/from16',
#     0x06: 'move-wide/16',
#     0x07: 'move-object',
#     0x08: 'move-object/from16',
#     0x09: 'move-object/16',
#     0x0A: 'move-result',
#     0x0B: 'move-result-wide',
#     0x0C: 'move-result-object',
#     0x0D: 'move-exception',
#     0x0E: 'return-void',
#     0x0F: 'return',
#
#     0x10: 'return-wide',
#     0x11: 'return-object',
#     0x12: 'const/4',
#     0x13: 'const/16',
#     0x14: 'const',
#     0x15: 'const/high16',
#     0x16: 'const-wide/16',
#     0x17: 'const-wide/32',
#     0x18: 'const-wide',
#     0x19: 'const-wide/high16',
#     0x1A: 'const-string',
#     0x1B: 'const-string-jumbo',
#     0x1C: 'const-class',
#     0x1D: 'monitor-enter',
#     0x1E: 'monitor-exit',
#     0x1F: 'check-cast',
#
#     0x20: 'instance-of',
#     0x21: 'array-length',
#     0x22: 'new-instance',
#     0x23: 'new-array',
#     0x24: 'filled-new-array',
#     0x25: 'filled-new-array-range',
#     0x26: 'fill-array-data',
#     0x27: 'throw',
#     0x28: 'goto',
#     0x29: 'goto/16',
#     0x2A: 'goto/32',
#     0x2B: 'packed-switch',
#     0x2C: 'sparse-switch',
#     0x2D: 'cmpl-float',
#     0x2E: 'cmpg-float',
#     0x2F: 'cmpl-double',
#
#     0x30: 'cmpg-double',
#     0x31: 'cmp-long',
#     0x32: 'if-eq',
#     0x33: 'if-ne',
#     0x34: 'if-lt',
#     0x35: 'if-ge',
#     0x36: 'if-gt',
#     0x37: 'if-le',
#     0x38: 'if-eqz',
#     0x39: 'if-nez',
#     0x3A: 'if-ltz',
#     0x3B: 'if-gez',
#     0x3C: 'if-gtz',
#     0x3D: 'if-lez',
#     0x3E: 'unused',
#     0x3F: 'unused',
#
#     0x40: 'unused',
#     0x41: 'unused',
#     0x42: 'unused',
#     0x43: 'unused',
#     0x44: 'aget',
#     0x45: 'aget-wide',
#     0x46: 'aget-object',
#     0x47: 'aget-boolean',
#     0x48: 'aget-byte',
#     0x49: 'aget-char',
#     0x4A: 'aget-short',
#     0x4B: 'aput',
#     0x4C: 'aput-wide',
#     0x4D: 'aput-object',
#     0x4E: 'aput-boolean',
#     0x4F: 'aput-byte',
#
#     0x50: 'aput-char',
#     0x51: 'aput-short',
#     0x52: 'iget',
#     0x53: 'iget-wide',
#     0x54: 'iget-object',
#     0x55: 'iget-boolean',
#     0x56: 'iget-byte',
#     0x57: 'iget-char',
#     0x58: 'iget-short',
#     0x59: 'iput',
#     0x5A: 'iput-wide',
#     0x5B: 'iput-object',
#     0x5C: 'iput-boolean',
#     0x5D: 'iput-byte',
#     0x5E: 'iput-char',
#     0x5F: 'iput-short',
#
#     0x60: 'sget',
#     0x61: 'sget-wide',
#     0x62: 'sget-object',
#     0x63: 'sget-boolean',
#     0x64: 'sget-byte',
#     0x65: 'sget-char',
#     0x66: 'sget-short',
#     0x67: 'sput',
#     0x68: 'sput-wide',
#     0x69: 'sput-object',
#     0x6A: 'sput-boolean',
#     0x6B: 'sput-byte',
#     0x6C: 'sput-char',
#     0x6D: 'sput-short',
#     0x6E: 'invoke-virtual',
#     0x6F: 'invoke-super',
#
#     0x70: 'invoke-direct',
#     0x71: 'invoke-static',
#     0x72: 'invoke-interface',
#     0x73: 'unused',
#     0x74: 'invoke-virtual/range',
#     0x75: 'invoke-super/range',
#     0x76: 'invoke-direct/range',
#     0x77: 'invoke-static/range',
#     0x78: 'invoke-interface-range',
#     0x79: 'unused',
#     0x7A: 'unused',
#     0x7B: 'neg-int',
#     0x7C: 'not-long',
#     0x7D: 'neg-long',
#     0x7E: 'not-long',
#     0x7F: 'neg-float',
#
#     0x80: 'neg-double',
#     0x81: 'int-to-long',
#     0x82: 'int-to-float',
#     0x83: 'int-to-double',
#     0x84: 'long-to-int',
#     0x85: 'long-to-float',
#     0x86: 'long-to-double',
#     0x87: 'float-to-int',
#     0x88: 'float-to-long',
#     0x89: 'float-to-double',
#     0x8A: 'double-to-int',
#     0x8B: 'double-to-long',
#     0x8C: 'double-to-float',
#     0x8D: 'int-to-byte',
#     0x8E: 'int-to-char',
#     0x8F: 'int-to-short',
#
#     0x90: 'add-int',
#     0x91: 'sub-int',
#     0x92: 'mul-int',
#     0x93: 'div-int',
#     0x94: 'rem-int',
#     0x95: 'and-int',
#     0x96: 'or-int',
#     0x97: 'xor-int',
#     0x98: 'shl-int',
#     0x99: 'shr-int',
#     0x9A: 'ushr-int',
#     0x9B: 'add-long',
#     0x9C: 'sub-long',
#     0x9D: 'mul-long',
#     0x9E: 'div-long',
#     0x9F: 'rem-long',
#
#     0xA0: 'and-long',
#     0xA1: 'or-long',
#     0xA2: 'xor-long',
#     0xA3: 'shl-long',
#     0xA4: 'shr-long',
#     0xA5: 'ushr-long',
#     0xA6: 'add-float',
#     0xA7: 'sub-float',
#     0xA8: 'mul-float',
#     0xA9: 'div-float',
#     0xAA: 'rem-float',
#     0xAB: 'add-double',
#     0xAC: 'sub-double',
#     0xAD: 'mul-double',
#     0xAE: 'div-double',
#     0xAF: 'rem-double',
#
#     0xB0: 'add-int/2addr',
#     0xB1: 'sub-int/2addr',
#     0xB2: 'mul-int/2addr',
#     0xB3: 'div-int/2addr',
#     0xB4: 'rem-int/2addr',
#     0xB5: 'and-int/2addr',
#     0xB6: 'or-int/2addr',
#     0xB7: 'xor-int/2addr',
#     0xB8: 'shl-int/2addr',
#     0xB9: 'shr-int/2addr',
#     0xBA: 'ushr-int/2addr',
#     0xBB: 'add-long/2addr',
#     0xBC: 'sub-long/2addr',
#     0xBD: 'mul-long/2addr',
#     0xBE: 'div-long/2addr',
#     0xBF: 'rem-long/2addr',
#
#     0xC0: 'and-long/2addr',
#     0xC1: 'or-long/2addr',
#     0xC2: 'xor-long/2addr',
#     0xC3: 'shl-long/2addr',
#     0xC4: 'shr-long/2addr',
#     0xC5: 'ushr-long/2addr',
#     0xC6: 'add-float/2addr',
#     0xC7: 'sub-float/2addr',
#     0xC8: 'mul-float/2addr',
#     0xC9: 'div-float/2addr',
#     0xCA: 'rem-float/2addr',
#     0xCB: 'add-double/2addr',
#     0xCC: 'sub-double/2addr',
#     0xCD: 'mul-double/2addr',
#     0xCE: 'div-double/2addr',
#     0xCF: 'rem-double/2addr',
#
#     0xD0: 'add-int/lit16',
#     0xD1: 'sub-int/lit16',
#     0xD2: 'mul-int/lit16',
#     0xD3: 'div-int/lit16',
#     0xD4: 'rem-int/lit16',
#     0xD5: 'and-int/lit16',
#     0xD6: 'or-int/lit16',
#     0xD7: 'xor-int/lit16',
#     0xD8: 'add-int/lit8',
#     0xD9: 'sub-int/lit8',
#     0xDA: 'mul-int/lit8',
#     0xDB: 'div-int/lit8',
#     0xDC: 'rem-int/lit8',
#     0xDD: 'and-int/lit8',
#     0xDE: 'or-int/lit8',
#     0xDF: 'xor-int/lit8',
#
#     0xE0: 'shl-int/lit8',
#     0xE1: 'shr-int/lit8',
#     0xE2: 'ushr-int/lit8',
#     0xE3: 'unused',
#     0xE4: 'unused',
#     0xE5: 'unused',
#     0xE6: 'unused',
#     0xE7: 'unused',
#     0xE8: 'unused',
#     0xE9: 'unused',
#     0xEA: 'unused',
#     0xEB: 'unused',
#     0xEC: 'unused',
#     0xED: 'unused',
#     0xEE: 'execute-inline',
#     0xEF: 'unused',
#
#     0xF0: 'invoke-direct-empty',
#     0xF1: 'unused',
#     0xF2: 'iget-quick',
#     0xF3: 'iget-wide-quick',
#     0xF4: 'iget-object-quick',
#     0xF5: 'iput-quick',
#     0xF6: 'iput-wide-quick',
#     0xF7: 'iput-object-quick',
#     0xF8: 'invoke-virtual-quick',
#     0xF9: 'invoke-virtual-quick/range',
#     0xFA: 'invoke-super-quick',
#     0xFB: 'invoke-super-quick/range',
#     0xFC: 'unused',
#     0xFD: 'unused',
#     0xFE: 'unused',
#     0xFF: 'unused'
#
# }

# 格式化op描述


"""
指令码对应的kind类型
"""
# kind_map = {
#
#     0x00: KIND_NONE,
#     0x01: KIND_NONE,
#     0x02: KIND_NONE,
#     0x03: KIND_NONE,
#     0x04: KIND_NONE,
#     0x05: KIND_NONE,
#     0x06: KIND_NONE,
#     0x07: KIND_NONE,
#     0x08: KIND_NONE,
#     0x09: KIND_NONE,
#     0x0A: KIND_NONE,
#     0x0B: KIND_NONE,
#     0x0C: KIND_NONE,
#     0x0D: KIND_NONE,
#     0x0E: KIND_NONE,
#     0x0F: KIND_NONE,
#
#     0x10: KIND_NONE,
#     0x11: KIND_NONE,
#     0x12: KIND_NONE,
#     0x13: KIND_NONE,
#     0x14: KIND_NONE,
#     0x15: KIND_NONE,
#     0x16: KIND_NONE,
#     0x17: KIND_NONE,
#     0x18: KIND_NONE,
#     0x19: KIND_NONE,
#     0x1A: KIND_STRING,
#     0x1B: KIND_STRING,
#     0x1C: KIND_TYPE,
#     0x1D: KIND_NONE,
#     0x1E: KIND_NONE,
#     0x1F: KIND_TYPE,
#
#     0x20: KIND_TYPE,
#     0x21: KIND_NONE,
#     0x22: KIND_TYPE,
#     0x23: KIND_TYPE,
#     0x24: KIND_TYPE,
#     0x25: KIND_TYPE,
#     0x26: KIND_NONE,
#     0x27: KIND_NONE,
#     0x28: KIND_NONE,
#     0x29: KIND_NONE,
#     0x2A: KIND_NONE,
#     0x2B: KIND_NONE,
#     0x2C: KIND_NONE,
#     0x2D: KIND_NONE,
#     0x2E: KIND_NONE,
#     0x2F: KIND_NONE,
#
#     0x30: KIND_NONE,
#     0x31: KIND_NONE,
#     0x32: KIND_NONE,
#     0x33: KIND_NONE,
#     0x34: KIND_NONE,
#     0x35: KIND_NONE,
#     0x36: KIND_NONE,
#     0x37: KIND_NONE,
#     0x38: KIND_NONE,
#     0x39: KIND_NONE,
#     0x3A: KIND_NONE,
#     0x3B: KIND_NONE,
#     0x3C: KIND_NONE,
#     0x3D: KIND_NONE,
#     0x3E: KIND_NONE,
#     0x3F: 'unused',
#
#     0x40: KIND_NONE,
#     0x41: KIND_NONE,
#     0x42: KIND_NONE,
#     0x43: KIND_NONE,
#     0x44: KIND_NONE,
#     0x45: KIND_NONE,
#     0x46: KIND_NONE,
#     0x47: KIND_NONE,
#     0x48: KIND_NONE,
#     0x49: KIND_NONE,
#     0x4A: KIND_NONE,
#     0x4B: KIND_NONE,
#     0x4C: KIND_NONE,
#     0x4D: KIND_NONE,
#     0x4E: KIND_NONE,
#     0x4F: KIND_NONE,
#
#     0x50: KIND_NONE,
#     0x51: KIND_NONE,
#     0x52: KIND_FIELD,
#     0x53: KIND_FIELD,
#     0x54: KIND_FIELD,
#     0x55: KIND_FIELD,
#     0x56: KIND_FIELD,
#     0x57: KIND_FIELD,
#     0x58: KIND_FIELD,
#     0x59: KIND_FIELD,
#     0x5A: KIND_FIELD,
#     0x5B: KIND_FIELD,
#     0x5C: KIND_FIELD,
#     0x5D: KIND_FIELD,
#     0x5E: KIND_FIELD,
#     0x5F: KIND_FIELD,
#
#     0x60: KIND_FIELD,
#     0x61: KIND_FIELD,
#     0x62: KIND_FIELD,
#     0x63: KIND_FIELD,
#     0x64: KIND_FIELD,
#     0x65: KIND_FIELD,
#     0x66: KIND_FIELD,
#     0x67: KIND_FIELD,
#     0x68: KIND_FIELD,
#     0x69: KIND_FIELD,
#     0x6A: KIND_FIELD,
#     0x6B: KIND_FIELD,
#     0x6C: KIND_FIELD,
#     0x6D: KIND_FIELD,
#     0x6E: KIND_METHOD,
#     0x6F: KIND_METHOD,
#
#     0x70: KIND_METHOD,
#     0x71: KIND_METHOD,
#     0x72: KIND_METHOD,
#     0x73: KIND_NONE,
#     0x74: KIND_METHOD,
#     0x75: KIND_METHOD,
#     0x76: KIND_METHOD,
#     0x77: KIND_METHOD,
#     0x78: KIND_METHOD,
#     0x79: KIND_NONE,
#     0x7A: KIND_NONE,
#     0x7B: KIND_NONE,
#     0x7C: KIND_NONE,
#     0x7D: KIND_NONE,
#     0x7E: KIND_NONE,
#     0x7F: KIND_NONE,
#
#     0x80: KIND_NONE,
#     0x81: KIND_NONE,
#     0x82: KIND_NONE,
#     0x83: KIND_NONE,
#     0x84: KIND_NONE,
#     0x85: KIND_NONE,
#     0x86: KIND_NONE,
#     0x87: KIND_NONE,
#     0x88: KIND_NONE,
#     0x89: KIND_NONE,
#     0x8A: KIND_NONE,
#     0x8B: KIND_NONE,
#     0x8C: KIND_NONE,
#     0x8D: KIND_NONE,
#     0x8E: KIND_NONE,
#     0x8F: KIND_NONE,
#
#     0x90: KIND_NONE,
#     0x91: KIND_NONE,
#     0x92: KIND_NONE,
#     0x93: KIND_NONE,
#     0x94: KIND_NONE,
#     0x95: KIND_NONE,
#     0x96: KIND_NONE,
#     0x97: KIND_NONE,
#     0x98: KIND_NONE,
#     0x99: KIND_NONE,
#     0x9A: KIND_NONE,
#     0x9B: KIND_NONE,
#     0x9C: KIND_NONE,
#     0x9D: KIND_NONE,
#     0x9E: KIND_NONE,
#     0x9F: KIND_NONE,
#
#     0xA0: KIND_NONE,
#     0xA1: KIND_NONE,
#     0xA2: KIND_NONE,
#     0xA3: KIND_NONE,
#     0xA4: KIND_NONE,
#     0xA5: KIND_NONE,
#     0xA6: KIND_NONE,
#     0xA7: KIND_NONE,
#     0xA8: KIND_NONE,
#     0xA9: KIND_NONE,
#     0xAA: KIND_NONE,
#     0xAB: KIND_NONE,
#     0xAC: KIND_NONE,
#     0xAD: KIND_NONE,
#     0xAE: KIND_NONE,
#     0xAF: KIND_NONE,
#
#     0xB0: KIND_NONE,
#     0xB1: KIND_NONE,
#     0xB2: KIND_NONE,
#     0xB3: KIND_NONE,
#     0xB4: KIND_NONE,
#     0xB5: KIND_NONE,
#     0xB6: KIND_NONE,
#     0xB7: KIND_NONE,
#     0xB8: KIND_NONE,
#     0xB9: KIND_NONE,
#     0xBA: KIND_NONE,
#     0xBB: KIND_NONE,
#     0xBC: KIND_NONE,
#     0xBD: KIND_NONE,
#     0xBE: KIND_NONE,
#     0xBF: KIND_NONE,
#
#     0xC0: KIND_NONE,
#     0xC1: KIND_NONE,
#     0xC2: KIND_NONE,
#     0xC3: KIND_NONE,
#     0xC4: KIND_NONE,
#     0xC5: KIND_NONE,
#     0xC6: KIND_NONE,
#     0xC7: KIND_NONE,
#     0xC8: KIND_NONE,
#     0xC9: KIND_NONE,
#     0xCA: KIND_NONE,
#     0xCB: KIND_NONE,
#     0xCC: KIND_NONE,
#     0xCD: KIND_NONE,
#     0xCE: KIND_NONE,
#     0xCF: KIND_NONE,
#
#     0xD0: KIND_NONE,
#     0xD1: KIND_NONE,
#     0xD2: KIND_NONE,
#     0xD3: KIND_NONE,
#     0xD4: KIND_NONE,
#     0xD5: KIND_NONE,
#     0xD6: KIND_NONE,
#     0xD7: KIND_NONE,
#     0xD8: KIND_NONE,
#     0xD9: KIND_NONE,
#     0xDA: KIND_NONE,
#     0xDB: KIND_NONE,
#     0xDC: KIND_NONE,
#     0xDD: KIND_NONE,
#     0xDE: KIND_NONE,
#     0xDF: KIND_NONE,
#
#     0xE0: KIND_NONE,
#     0xE1: KIND_NONE,
#     0xE2: KIND_NONE,
#     0xE3: KIND_NONE,
#     0xE4: KIND_NONE,
#     0xE5: KIND_NONE,
#     0xE6: KIND_NONE,
#     0xE7: KIND_NONE,
#     0xE8: KIND_NONE,
#     0xE9: KIND_NONE,
#     0xEA: KIND_NONE,
#     0xEB: KIND_NONE,
#     0xEC: KIND_NONE,
#     0xED: KIND_NONE,
#     0xEE: KIND_NONE,
#     0xEF: KIND_NONE,
#
#     0xF0: KIND_NONE,
#     0xF1: KIND_NONE,
#     0xF2: KIND_NONE,
#     0xF3: KIND_NONE,
#     0xF4: KIND_NONE,
#     0xF5: KIND_NONE,
#     0xF6: KIND_NONE,
#     0xF7: KIND_NONE,
#     0xF8: KIND_NONE,
#     0xF9: KIND_NONE,
#     0xFA: KIND_METHOD,
#     0xFB: KIND_METHOD,
#     0xFC: KIND_SITE,
#     0xFD: KIND_SITE,
#     0xFE: KIND_NONE,
#     0xFF: KIND_NONE,
#
# }

"""
指令码对应的解释格式类型
"""
# format_map = {
#
#     0x00: '10x',
#     0x01: '12x',
#     0x02: '22x',
#     0x03: '32x',
#     0x04: '12x',
#     0x05: '22x',
#     0x06: '32x',
#     0x07: '12x',
#     0x08: '22x',
#     0x09: '32x',
#     0x0A: '11x',
#     0x0B: '11x',
#     0x0C: '11x',
#     0x0D: '11x',
#     0x0E: '10x',
#     0x0F: '11x',
#
#     0x10: '11x',
#     0x11: '11x',
#     0x12: '11n',
#     0x13: '21s',
#     0x14: '31i',
#     0x15: '21h',
#     0x16: '21s',
#     0x17: '31i',
#     0x18: '51l',
#     0x19: '21h',
#     0x1A: '21c',
#     0x1B: '31c',
#     0x1C: '21c',
#     0x1D: '11x',
#     0x1E: '11x',
#     0x1F: '21c',
#
#     0x20: '22c',
#     0x21: '12x',
#     0x22: '21c',
#     0x23: '22c',
#     0x24: '35c',
#     0x25: '3rc',
#     0x26: '31t',
#     0x27: '11x',
#     0x28: '10t',
#     0x29: '20t',
#     0x2A: '30t',
#     0x2B: '31t',
#     0x2C: '31t',
#     0x2D: '23x',
#     0x2E: '23x',
#     0x2F: '23x',
#
#     0x30: '23x',
#     0x31: '23x',
#     0x32: '22t',
#     0x33: '22t',
#     0x34: '22t',
#     0x35: '22t',
#     0x36: '22t',
#     0x37: '22t',
#     0x38: '21t',
#     0x39: '21t',
#     0x3A: '21t',
#     0x3B: '21t',
#     0x3C: '21t',
#     0x3D: '21t',
#     0x3E: '',
#     0x3F: '',
#
#     0x40: '',
#     0x41: '',
#     0x42: '',
#     0x43: '',
#     0x44: '23x',
#     0x45: '23x',
#     0x46: '23x',
#     0x47: '23x',
#     0x48: '23x',
#     0x49: '23x',
#     0x4A: '23x',
#     0x4B: '23x',
#     0x4C: '23x',
#     0x4D: '23x',
#     0x4E: '23x',
#     0x4F: '23x',
#
#     0x50: '23x',
#     0x51: '23x',
#     0x52: '22c',
#     0x53: '22c',
#     0x54: '22c',
#     0x55: '22c',
#     0x56: '22c',
#     0x57: '22c',
#     0x58: '22c',
#     0x59: '22c',
#     0x5A: '22c',
#     0x5B: '22c',
#     0x5C: '22c',
#     0x5D: '22c',
#     0x5E: '22c',
#     0x5F: '22c',
#
#     0x60: '21c',
#     0x61: '21c',
#     0x62: '21c',
#     0x63: '21c',
#     0x64: '21c',
#     0x65: '21c',
#     0x66: '21c',
#     0x67: '21c',
#     0x68: '21c',
#     0x69: '21c',
#     0x6A: '21c',
#     0x6B: '21c',
#     0x6C: '21c',
#     0x6D: '21c',
#     0x6E: '35c',
#     0x6F: '35c',
#
#     0x70: '35c',
#     0x71: '35c',
#     0x72: '35c',
#     0x73: '10x',
#     0x74: '3rc',
#     0x75: '3rc',
#     0x76: '3rc',
#     0x77: '3rc',
#     0x78: '3rc',
#     0x79: '',
#     0x7A: '',
#     0x7B: '12x',
#     0x7C: '12x',
#     0x7D: '12x',
#     0x7E: '12x',
#     0x7F: '12x',
#
#     0x80: '12x',
#     0x81: '12x',
#     0x82: '12x',
#     0x83: '12x',
#     0x84: '12x',
#     0x85: '12x',
#     0x86: '12x',
#     0x87: '12x',
#     0x88: '12x',
#     0x89: '12x',
#     0x8A: '12x',
#     0x8B: '12x',
#     0x8C: '12x',
#     0x8D: '12x',
#     0x8E: '12x',
#     0x8F: '12x',
#
#     0x90: '23x',
#     0x91: '23x',
#     0x92: '23x',
#     0x93: '23x',
#     0x94: '23x',
#     0x95: '23x',
#     0x96: '23x',
#     0x97: '23x',
#     0x98: '23x',
#     0x99: '23x',
#     0x9A: '23x',
#     0x9B: '23x',
#     0x9C: '23x',
#     0x9D: '23x',
#     0x9E: '23x',
#     0x9F: '23x',
#
#     0xA0: '23x',
#     0xA1: '23x',
#     0xA2: '23x',
#     0xA3: '23x',
#     0xA4: '23x',
#     0xA5: '23x',
#     0xA6: '23x',
#     0xA7: '23x',
#     0xA8: '23x',
#     0xA9: '23x',
#     0xAA: '23x',
#     0xAB: '23x',
#     0xAC: '23x',
#     0xAD: '23x',
#     0xAE: '23x',
#     0xAF: '23x',
#
#     0xB0: '12x',
#     0xB1: '12x',
#     0xB2: '12x',
#     0xB3: '12x',
#     0xB4: '12x',
#     0xB5: '12x',
#     0xB6: '12x',
#     0xB7: '12x',
#     0xB8: '12x',
#     0xB9: '12x',
#     0xBA: '12x',
#     0xBB: '12x',
#     0xBC: '12x',
#     0xBD: '12x',
#     0xBE: '12x',
#     0xBF: '12x',
#
#     0xC0: '12x',
#     0xC1: '12x',
#     0xC2: '12x',
#     0xC3: '12x',
#     0xC4: '12x',
#     0xC5: '12x',
#     0xC6: '12x',
#     0xC7: '12x',
#     0xC8: '12x',
#     0xC9: '12x',
#     0xCA: '12x',
#     0xCB: '12x',
#     0xCC: '12x',
#     0xCD: '12x',
#     0xCE: '12x',
#     0xCF: '12x',
#
#     0xD0: '22s',
#     0xD1: '22s',
#     0xD2: '22s',
#     0xD3: '22s',
#     0xD4: '22s',
#     0xD5: '22s',
#     0xD6: '22s',
#     0xD7: '22s',
#     0xD8: '22b',
#     0xD9: '22b',
#     0xDA: '22b',
#     0xDB: '22b',
#     0xDC: '22b',
#     0xDD: '22b',
#     0xDE: '22b',
#     0xDF: '22b',
#
#     0xE0: '22b',
#     0xE1: '22b',
#     0xE2: '22b',
#     0xE3: '',
#     0xE4: '',
#     0xE5: '',
#     0xE6: '',
#     0xE7: '',
#     0xE8: '',
#     0xE9: '',
#     0xEA: '',
#     0xEB: '',
#     0xEC: '',
#     0xED: '',
#     0xEE: '',
#     0xEF: '',
#
#     0xF0: '',
#     0xF1: '',
#     0xF2: '',
#     0xF3: '',
#     0xF4: '',
#     0xF5: '',
#     0xF6: '',
#     0xF7: '',
#     0xF8: '',
#     0xF9: '',
#     0xFA: '45cc',
#     0xFB: '4rcc',
#     0xFC: '35c',
#     0xFD: '3rc',
#     0xFE: '10x',
#     0xFF: '10x'
#
# }

"""
kind对应的section类型
"""
KIND_SECTION_TYPE_TYPE_ID = 0x0002
KIND_SECTION_TYPE_PROTO_ID = 0x0003
KIND_SECTION_TYPE_FIELD_ID = 0x0004
KIND_SECTION_TYPE_METHOD_ID = 0x0005
KIND_SECTION_TYPE_STRING_DATA = 0x2002

"""
kind到section类型的映射表
"""
kind_section_type_map = {
    KIND_STRING: KIND_SECTION_TYPE_STRING_DATA,
    KIND_TYPE: KIND_SECTION_TYPE_TYPE_ID,
    KIND_FIELD: KIND_SECTION_TYPE_FIELD_ID,
    KIND_METHOD: KIND_SECTION_TYPE_METHOD_ID,
    KIND_PROTO: KIND_SECTION_TYPE_PROTO_ID,
}


def getKindDesc(context, kind, kind_x):
    """
    通过context获取kind描述
    context:    上下文，包含section相关信息
    kind:       引用类型
    kind_x:     引用数值
    """
    if kind in kind_section_type_map and not kind_x is None:
        section_type = kind_section_type_map[kind]
        return context.getSectionItemDesc(section_type, kind_x)

    return None

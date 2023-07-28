#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：hardware_equip.py
@Author  ：szhu9903
@Date    ：2023/7/5 14:34 
'''

# noinspection PyUnresolvedReferences
from odoo import fields, models

class HardwareType(models.Model):
    """
    设备类型表
    """
    _name = 'hardware.hardware.type'
    _description = '设备类型表'
    _rec_name = 'ht_name'


    ht_name = fields.Char('分类名称', required=True)
    ht_code_down = fields.Integer('编码范围下', required=True)
    ht_code_up = fields.Integer('编码范围上', required=True)


class HardwareConfigVar(models.Model):
    """
    设备配置项
    """
    _name = 'hardware.hardware.configvar'
    _description = '设备配置项'
    _rec_name = 'hcv_variablekey'

    hcv_type = fields.Many2one('hardware.hardware.type', '设备类型')
    hcv_variablekey = fields.Char('参数项名称', required=True)
    hcv_variablevalue = fields.Char('参数项取值', required=True)
    hcv_describe = fields.Char('描述')

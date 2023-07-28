#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：demo.py.py
@Author  ：szhu9903
@Date    ：2023/7/25 16:58 
'''

from odoo import fields, models

class Full103Env(models.Model):
    """
    环境数据
    """
    _name = 'hardware.full103.env'
    _description = '环境数据'
    _rec_name = 'fe_equipcode'

    fe_equipid = fields.Many2one('hardware.hardware.equip', '设备')
    fe_equipcode = fields.Integer('设备编码')
    fe_temperature = fields.Float('温度', digits=(5, 2))
    fe_humidity = fields.Float('湿度', digits=(5, 2))

class Full103Relay(models.Model):
    """
    继电器控制
    """
    _name = 'hardware.full103.relay'
    _description = '继电器控制'
    _rec_name = 'fr_equipcode'

    fr_equipid = fields.Many2one('hardware.hardware.equip', '设备')
    fr_equipcode = fields.Integer('设备编码')
    fr_switch = fields.Selection([('0', '开'), ('1', '关')],'开/关')
    fr_controlmode = fields.Selection([('0', '自动'), ('1', '手动')],'控制方式')

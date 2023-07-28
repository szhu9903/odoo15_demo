#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：demo.py.py
@Author  ：szhu9903
@Date    ：2023/7/25 16:58 
'''

from odoo import fields, models

class DemoEnv(models.Model):
    """
    测试板设备环境数据
    """
    _name = 'hardware.demo.env'
    _description = '环境数据'
    _rec_name = 'de_equipcode'

    de_equipid = fields.Many2one('hardware.hardware.equip', '设备')
    de_equipcode = fields.Integer('设备编码')
    de_temperature = fields.Float('温度', digits=(5, 2))
    de_humidity = fields.Float('湿度', digits=(5, 2))

class DemoLed(models.Model):
    """
    测试板设备LED控制
    """
    _name = 'hardware.demo.led'
    _description = 'LED控制'
    _rec_name = 'dl_equipcode'

    dl_equipid = fields.Many2one('hardware.hardware.equip', '设备')
    dl_equipcode = fields.Integer('设备编码')
    dl_switch = fields.Selection([('0', '开'), ('1', '关')],'开/关')
    dl_r = fields.Integer('LED-R')
    dl_g = fields.Integer('LED-G')
    dl_b = fields.Integer('LED-B')

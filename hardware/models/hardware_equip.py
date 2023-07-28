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
from odoo.exceptions import ValidationError

class HardwareEquip(models.Model):
    _name = 'hardware.hardware.equip'
    _description = '设备表'
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _rec_name = 'he_name'

    he_name = fields.Char('设备名称', required=True)
    he_num = fields.Char('设备编号', required=True)
    he_type = fields.Many2one('hardware.hardware.type', '设备分类')
    he_equipstatus = fields.Selection([('BROKEN', '离线'), ('LINKED', '在线')], '登录状态', default='BROKEN')
    he_starttype = fields.Selection([('START', '离线'), ('STOP', '在线'), ('UNASSIGNED', '待分配')], '设备状态', default='UNASSIGNED')
    he_effect = fields.Selection([('0', '临时设备'), ('1', '正常设备')], '设备作用', default='1')

    def button_check_equip(self):
        # self.ensure_one()
        for equip in self:
            print(equip)
        raise ValidationError('Place check equip effect!')
        # return  False




#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：sys_purview.py
@Author  ：szhu9903
@Date    ：2023/7/24 15:22 
'''

from odoo import fields, models

class SysPurview(models.Model):
    """
    系统api权限
    """
    _name = 'hardware.sys.purview'
    _description = 'api权限'
    _rec_name = 'sp_name'

    sp_name = fields.Char('权限名称', required=True)
    sp_apipath = fields.Char('api_path', required=True)
    sp_type = fields.Selection([('1','查看'),('2','操作')],'权限类型', required=True, default='1')

class SysMenu(models.Model):
    """
    系统后台管理菜单
    """
    _name = 'hardware.sys.menu'
    _description = '后台管理菜单'
    _rec_name = 'sm_name'

    sm_name = fields.Char('菜单名称', required=True)
    sm_menupath = fields.Char('path')
    sm_menuupid = fields.Many2one('hardware.sys.menu','父级菜单')
    sm_sort = fields.Integer('菜单顺序', required=True, default=0)

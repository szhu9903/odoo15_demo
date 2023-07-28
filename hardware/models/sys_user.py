#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：sys_user.py
@Author  ：szhu9903
@Date    ：2023/7/24 09:24 
'''

from odoo import fields, models

class SysUser(models.Model):
    _name = 'hardware.sys.user'
    _description = '用户信息'
    _rec_name = 'su_username'

    su_account = fields.Char('web账号', required=True)
    su_pwd = fields.Char('web密码', required=True, default='')
    su_sex = fields.Selection([('男','男'),('女','女')], '性别', default='男')
    su_username = fields.Char('用户名', required=True, default='')
    su_userphoto = fields.Binary('头像')
    su_phone = fields.Char('电话', default='')
    su_email = fields.Char('邮箱', default='')
    su_isadmin = fields.Selection([('0','否'),('1','是')], '后台用户', default='1')
    su_delflag = fields.Selection([('0','有效'),('1','无效')],'有效状态', default='0')

    su_odoouser = fields.Many2one('res.users', '关联odoo用户')
    role_ids = fields.Many2many('hardware.sys.role', 'ur_relation', 'ur_userid', 'ur_roleid', '角色')


class SysRole(models.Model):
    """
    系统角色
    """
    _name = 'hardware.sys.role'
    _description = '角色'
    _rec_name = 'sr_name'

    sr_name = fields.Char('角色名称', required=True)
    user_ids = fields.Many2many('hardware.sys.user', 'ur_relation', 'ur_roleid', 'ur_userid', '用户')
    purview_ids = fields.Many2many('hardware.sys.purview', 'rp_relation', 'rp_roleid', 'rp_purviewid', 'api权限')
    menu_ids = fields.Many2many('hardware.sys.menu', 'rm_relation', 'rm_roleid', 'rm_menuid', '后台管理菜单')

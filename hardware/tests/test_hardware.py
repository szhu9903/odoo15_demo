#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：odoo 
@File    ：test_hardware.py
@Author  ：szhu9903
@Date    ：2023/7/5 13:58 
'''

from odoo.tests.common import TransactionCase

class TestHardware(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Hardware = self.env['hardware.hardware_equip']
        self.hardware1 = self.Hardware.create({
            "he_name": "testname",
            "he_num": "1001",
        })
    def test_book_create(self):
        "New Books are active by default"
        self.assertEqual(self.hardware1.he_equipstatus, 'BROKEN')


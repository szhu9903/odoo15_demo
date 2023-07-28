# -*- coding: utf-8 -*-
{
    'name': "hardware_center",

    'summary': "设备，控制，管理",

    'description': "硬件设备管理",

    'author': "ZSJ",
    'website': "https://zsjblog.com",

    'category': 'mydemo/hardware',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        ''
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/hardware_equip.xml',
        'views/hardware_type.xml',
        'views/hardware_configvar.xml',
        'views/sys_user.xml',
        'views/sys_role.xml',
        'views/sys_purview.xml',
        'views/sys_webmenu.xml',
        'views/demo_env.xml',
        'views/demo_led.xml',
        'views/full103_env.xml',
        'views/full103_relay.xml',
        'views/hardware_menu.xml',

        'templates/hardware_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

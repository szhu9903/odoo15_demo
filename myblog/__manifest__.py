# -*- coding: utf-8 -*-
{
    # 模块名称
    'name': "myblog",
    #关键词
    'summary': "个人博客",
    #模块说明
    'description': "个人博客",
    #作者 网站
    'author': "ZSJ",
    'website': "https://zsjblog.com",
    #类别
    'category': 'mydemo/myblog',
    'version': '0.1',

    # 本模块所依赖的模块，安装本模块会同时安装依赖的模块
    'depends': ['base','mail'],

    # 加载的处理文件，总是加载
    'data': [
        'views/blog.xml',
        'views/blog_user.xml',
        'views/blog_type.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/blog_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
from odoo import fields,models,api,osv
import traceback,base64
from xlrd import open_workbook
from io import StringIO
from PIL import Image



class Blog(models.Model):
    _name = 'myblog.blog'
    _description = u'博客'
    _rec_name = 'blog_title'
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = 'blog_views asc'

    blog_title = fields.Char('博文标题',track_visibility='onchange')
    blog_brief = fields.Text('文章摘要',track_visibility='onchange')
    blog_cover = fields.Char('文章封面url',track_visibility='onchange')
    blog_data = fields.Binary('文章封面文件',track_visibility='onchange')
    author_id = fields.Many2one('myblog.blog.user',string='作者')
    blog_type = fields.Many2one('myblog.blog.type',string='文章分类')
    blog_content = fields.Html('博文内容',track_visibility='onchange')
    blog_views = fields.Integer('浏览量')
    blog_comment_count = fields.Integer('评论总数')
    blog_like_count = fields.Integer('点赞数量')
    create_date = fields.Datetime('发表时间')
    del_flag = fields.Integer('删除标志',default=0)
    # zsta = fields.Float('a')
    # zend = fields.Float('b')
    # znum = fields.Float(compute='_compute_znum',store=True)   #store 是否实际存在数据库中

    color = fields.Integer('颜色')
    priority = fields.Selection([
        ('0','低'),
        ('1','中'),
        ('2','高')],
        '优先级',default='1')
    kanban_state = fields.Selection([
        ('normal','进行中'),
        ('blocked','挂起'),
        ('done','完成')],
    '看板状态',default='normal')


    @api.model
    def create(self, vals):
        blog_data = vals.get('blog_data')
        if blog_data:
            img_data = base64.b64decode(blog_data)
            with open('test.jpg', 'wb') as af:
                af.write(img_data)
                af.close()
        res = super(Blog,self).create(vals)
        return res


    def write(self, vals):
        blog_data = vals.get('blog_data')
        # if self.zblog_views <0:
        #     raise osv.except_osv(_(u'警告'),_(u'浏览量不小于0'))
        if blog_data:
            img_data = base64.b64decode(blog_data)
            with open('test.jpg', 'wb') as af:
                af.write(img_data)
                af.close()
        res = super(Blog,self).write(vals)
        return res




#图片文件读取
    def get_blog_data(self):
        try:
            actives = self.browse(self.env.context.get('active_ids'))
            for record in actives and actives:
                bytes_data = record.blog_data
                if bytes_data:
                    img_data = base64.b64decode(bytes_data)
                    with open('test.jpg','wb') as af:
                        af.write(img_data)
                        af.close()
        except:
            traceback.print_exc()

    # #动态字段
    # @api.depends('zsta','zend')
    # def _compute_znum(self):
    #     for record in self:
    #         if record.zend == 0:
    #             record.znum = record.zsta
    #         else:
    #             record.znum = round(record.zsta/record.zend,2)



    @api.onchange('blog_views')
    def _onchange_blog_views(self):
        if self.blog_views < 0:
            return {
                'warning':{
                    'title':'警告',
                    'message':'浏览量不能小于0'
                }
            }




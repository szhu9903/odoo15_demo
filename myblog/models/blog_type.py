
from odoo import models,fields

class BlogType(models.Model):
    _name = 'myblog.blog.type'
    _description = u'文章分类'
    _rec_name = 'type_name'
    _inherit = ['mail.thread']
    _order = 'blog_count'

    type_name = fields.Char('分类名称',track_visibility='onchange')
    blog_count = fields.Integer('文章数量',track_visibility='onchange')
    up_type = fields.Many2one('myblog.blog.type','上级分类')
    create_by = fields.Many2one('myblog.blog.user','创建人')
    del_flag = fields.Integer('删除标志',default=0)

    #https://www.cnblogs.com/ygj0930/p/10826232.html
    def get_myblog_blog(self):
        sql = """
        select id from myblog_blog where blog_type='%s'
        """%self.id
        self._cr.execute(sql)
        res = self._cr.fetchall()
        blog_list = [blog_id[0] for blog_id in res]
        formview_ref = self.env.ref('myblog.view_myblog_form',False)
        treeview_ref = self.env.ref('myblog.view_myblog_tree',False)
        return {
            'name': '所有文章',
            'view_type': 'form',
            'view_model': 'form,tree',
            'res_model': 'myblog.blog',
            'domain':"[('id','in',%s)]"%blog_list,
            'views':[(treeview_ref and treeview_ref.id or False,'tree'),
                     (formview_ref and formview_ref.id or False,'form')],
            'type':'ir.actions.act_window',
            'target':'main'
        }



from odoo import models,fields,api
import hashlib
from werkzeug.security import generate_password_hash

class BlogUser(models.Model):
    _name = 'myblog.blog.user'
    _description = '用户'
    _rec_name = 'user_name'
    _inherit = ['mail.thread']
    _order = 'account asc'

    account = fields.Char('账号',track_visibility='onchange')
    pwd = fields.Char('密码',track_visibility='onchange')
    sex = fields.Selection([
        ('0','男'),
        ('1','女')],string ='性别', track_visibility='onchange')
    phone = fields.Char('电话',track_visibility='onchange')
    email = fields.Char('邮箱',track_visibility='onchange')
    github_token = fields.Char('GitHub',track_visibility='onchange')
    user_name = fields.Char('用户名称',track_visibility='onchange')
    user_photo = fields.Char('用户头像',track_visibility='onchange')
    del_flag = fields.Integer('删除标志', default=0)

    @api.model
    def create(self,vals):
        pwd = vals.get('pwd')
        if pwd:
            vals['pwd'] = generate_password_hash(pwd)
        res = super(BlogUser,self).create(vals)
        return res

    def write(self,vals):
        pwd = vals.get('pwd')
        if pwd:
            vals['pwd'] = generate_password_hash(pwd)
        res = super(BlogUser,self).write(vals)
        return res


    #
    # @api.model
    # def create(self, vals):
    #     pwd = vals.get('zpwd')
    #     if pwd:
    #         hl = hashlib.md5(pwd.encode(encoding='utf-8'))
    #         vals['zpwd'] = hl.hexdigest()
    #     res =  super(ZsjBlogUser,self).create(vals)
    #     return res

    # def write(self, vals):
    #     pwd = vals.get('zpwd')
    #     if pwd:
    #         hl = hashlib.md5(pwd.encode(encoding='utf-8'))
    #         vals['zpwd'] = hl.hexdigest()
    #     res = super(ZsjBlogUser,self).write(vals)
    #     return res
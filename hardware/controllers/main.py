# -*- coding: utf-8 -*-

from odoo import http

class Hardware(http.Controller):
    @http.route('/hardware/main', auth='user')
    def index(self, **kwargs):
        return "Hello, world"

    @http.route('/hardware/hardwares', auth='public')
    def list(self, **kwargs):
        HardwaresEquip = http.request.env['hardware.hardware.equip']
        hardwares = HardwaresEquip.search([])
        return http.request.render(
            'hardware.hardware_list_template', {'hardwares':hardwares})
        # return http.request.render('hardware.listing', {
        #     'root': '/hardware/hardware',
        #     'objects': http.request.env['hardware.hardware'].search([]),
        # })

#     @http.route('/hardware/hardware/objects/<model("hardware.hardware"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hardware.object', {
#             'object': obj
#         })

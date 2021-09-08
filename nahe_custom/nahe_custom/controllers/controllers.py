# -*- coding: utf-8 -*-
# from odoo import http


# class naheCustom(http.Controller):
#     @http.route('/nahe_custom/nahe_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_custom/nahe_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_custom.listing', {
#             'root': '/nahe_custom/nahe_custom',
#             'objects': http.request.env['nahe_custom.nahe_custom'].search([]),
#         })

#     @http.route('/nahe_custom/nahe_custom/objects/<model("nahe_custom.nahe_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_custom.object', {
#             'object': obj
#         })

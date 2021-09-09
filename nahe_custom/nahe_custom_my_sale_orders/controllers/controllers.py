# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo/repositorios/naheCustom/naheCustomMySaleOrders(http.Controller):
#     @http.route('/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders.listing', {
#             'root': '/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders',
#             'objects': http.request.env['odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders.odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders'].search([]),
#         })

#     @http.route('/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders/objects/<model("odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders.odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo/repositorios/nahe_custom/nahe_custom_my_sale_orders.object', {
#             'object': obj
#         })

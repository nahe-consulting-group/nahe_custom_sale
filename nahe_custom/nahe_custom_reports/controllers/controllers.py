# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo/repositorios/naheCustomReports(http.Controller):
#     @http.route('/odoo/repositorios/nahe_custom_reports/odoo/repositorios/nahe_custom_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo/repositorios/nahe_custom_reports/odoo/repositorios/nahe_custom_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo/repositorios/nahe_custom_reports.listing', {
#             'root': '/odoo/repositorios/nahe_custom_reports/odoo/repositorios/nahe_custom_reports',
#             'objects': http.request.env['odoo/repositorios/nahe_custom_reports.odoo/repositorios/nahe_custom_reports'].search([]),
#         })

#     @http.route('/odoo/repositorios/nahe_custom_reports/odoo/repositorios/nahe_custom_reports/objects/<model("odoo/repositorios/nahe_custom_reports.odoo/repositorios/nahe_custom_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo/repositorios/nahe_custom_reports.object', {
#             'object': obj
#         })

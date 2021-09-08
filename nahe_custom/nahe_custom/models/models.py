# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nahe_custom_comments(models.Model):
	_inherit = 'sale.order.line'

	comments = fields.Text(string='Comentarios')

class nahe_custom_estados(models.Model):
	_inherit = 'sale.order'

	listo = fields.Boolean(string='Listo')
	preparando = fields.Boolean(string='Preparando')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

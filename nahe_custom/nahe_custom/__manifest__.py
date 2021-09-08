# -*- coding: utf-8 -*-
{
    'name': "nahe_custom",

    'summary': "Modificaciones para sale.order.form y tree por Nähe.",

    'description': """
        Dentro de este modulo se incorporan las modificaciones custom para sale.order.form y tree, la idea es dejarlas aqui y podes instalarlas.
        Que no se pierdan con un update.
    """,

    'author': "Nähe Consulting Group",
    'website': "https://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

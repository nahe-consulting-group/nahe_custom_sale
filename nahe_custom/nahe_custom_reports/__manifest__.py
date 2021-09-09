# -*- coding: utf-8 -*-
{
    'name': "Nähe custom reports",

    'summary': """
        Nähe custom reports editamos el reporte de presupuesto y factura""",

    'description': """
        Nähe custom reports necesita que este instalado nahe_custom_sale/nahe_custom
    """,

    'author': "Nähe Consulring Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nahe_custom'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

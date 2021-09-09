# -*- coding: utf-8 -*-
{
    'name': "Nähe custom my sale orders",

    'summary': """
        Agregamos en el listado de pedidos del cliente en website_sale mas detalles""",

    'description': """
        Agregamos en el listado de pedidos si el pedido esta siendo preparado, si esta listo para entregar o si ya fue entregado. 
        Esto lo ve cada cliente desde /my/orders. Nos basamos en el modulo nahe_custom,
        que agrega a las sale.order las opciones preparando y listo
    """,

    'author': "Nähe Consulring Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nahe_custom','sale','website','website_sale'],

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

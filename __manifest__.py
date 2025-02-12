# -*- coding: utf-8 -*-
{
    'name': "KBI Custom",

    'summary': "Modul Custom Kyoraku Blowmolding Indonesia",

    'description': """
Modul Custom Kyoraku Blowmolding Indonesia
    """,

    'author': "PT. Lintang Utama Infotek",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}


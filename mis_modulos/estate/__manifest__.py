# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'estateSor',
    'version': '1.2',
    'category': 'Sales/estate',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'depends': [
        'base',        
    ],
    'data': [     
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml'        
    ],
    'demo': [        
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'estate',
    'version': '1.2',
    'category': 'Sales/estate',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'depends': [
        'base',        
    ],
    'data': [     
        'security/ir.model.access.csv' 
    ],
    'demo': [        
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
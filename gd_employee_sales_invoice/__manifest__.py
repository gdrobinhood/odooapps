# -*- coding: utf-8 -*-

{
    'name': "Employee Sales Invoice",
    'author': "hola@dynamica.com.pa",
    'website': "https://dynamica.com.pa",
    'category': 'Human Resources',
    'summary': """Display the number of quotations and sales order quickly on the Employee""",
    'license': 'AGPL-3',
    'description': """""",
    'version': '1.0',
    'depends': [
        'hr', 
        'sale_management', 
        'account', 
        'sale', 
        'contacts'
    ],
    'data': [
        'views/account_move.xml',
        'views/employee_view.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

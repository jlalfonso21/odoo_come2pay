# -*- coding: utf-8 -*-
{
    "name": "Come2Pay Payment Acquirer",
    "summary": """Payment Acquirer: Come2Pay Implementation""",
    "author": "Jorge Luis Alfonso Chavez",
    "category": "Accounting/Payment Acquirers",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["payment"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

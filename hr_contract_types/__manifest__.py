# -*- coding: utf-8 -*-

{
    'name': 'CloudBI Fusion Employee Contracts Types',
    'version': '16.0.1.1.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """
        Contract type in contracts
    """,
    'description': """CloudBI Fusion Employee Contracts Types,CloudBI Fusion Employee, Employee Contracts""",
    'author': 'Odoo SA,Eqilibrium Solutions',
    'company': 'Eqilibrium Solutions',
    'maintainer': 'Eqilibrium Solutions',
    'website': 'https://www.eqilibriumsolutions.com',
    'depends': ['hr', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_view.xml',
        'data/hr_contract_type_data.xml',
    ],
    'installable': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}

# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Rahul CK(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU AFFERO GENERAL
#    PUBLIC LICENSE (AGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC
#    LICENSE (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Email Verification for Partner and Employee",
    'version': '16.0.1.0.0',
    'category': 'Discuss',
    'summary': """Check Whether A Given E-mail ID Is Valid Or Not""",
    'description': """Check Whether A Given E-mail ID Is Valid Or Not In
        Partner And Employee Form""",
    'author': "Eqilibrium Solutions",
    'company': "Eqilibrium Solutions",
    'maintainer': 'Eqilibrium Solutions',
    'website': "https://www.eqilibriumsolutions.com",
    'depends': ['base', 'hr'],
    'external_dependencies': {'python': ['validate_email', 'py3DNS']},
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

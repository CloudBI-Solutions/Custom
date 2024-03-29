# -*- coding: utf-8 -*-
###############################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Cybrosys Technologies (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Fusion HRMS Reminders Todo',
    'version': '16.0.2.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': 'HR Reminder For Fusion HR',
    'author': 'Eqilibrium Solutions,Open HRMS',
    'company': 'Eqilibrium Solutions',
    'website': "https://www.eqilibriumsolutions.com",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_reminder_security.xml',
        'views/hr_reminder_view.xml',
        'data/ir_cron_reminder.xml'

    ],
    'assets': {
        'web.assets_backend': [
            'hr_reminder/static/src/css/notification.css',
            'hr_reminder/static/src/scss/reminder.scss',
            'hr_reminder/static/src/xml/reminder_topbar.xml',
            'hr_reminder/static/src/js/reminder_topbar.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

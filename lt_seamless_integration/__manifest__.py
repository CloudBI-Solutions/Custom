##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
{
    'name': 'Link Meetings to Customers without Sending Invitations',
    'summary': 'Link Meetings to Customers without Sending Invitations or '
               'Reminders while still keeping Client Information in CloudBI Fusion',
    'author': "lumitec GmbH",
    'website': "https://www.lumitec.solutions",
    'category': 'Extra Tools',
    'version': '16.0.1.0.0',
    'license': 'OPL-1',
    'images': ['static/description/thumbnail.png'],
    'depends': [
        'base',
        'calendar',
        'crm',
        'event',
        'contacts',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/event_views.xml',
        'views/meeting_type_views.xml',
        'views/calendar_event_views.xml',
        'views/crm_lead_views.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}

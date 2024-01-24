##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import models, Command
from collections import defaultdict
from odoo.tools import is_html_empty


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    def action_create_calendar_event(self):
        """On scheduling meeting through schedule activity the partner gets added to the representative"""
        self.ensure_one()
        representative_ids = self.ids
        representative_ids.append(self.env.user.partner_id.id)
        action = self.env["ir.actions.actions"]._for_xml_id("calendar.action_calendar_event")
        action['context'] = {
            'default_activity_type_id': self.activity_type_id.id,
            'default_res_id': self.env.context.get('default_res_id'),
            'default_res_model': self.env.context.get('default_res_model'),
            'default_name': self.summary or self.res_name,
            'default_description': self.note if not is_html_empty(self.note) else '',
            'default_activity_ids': [(6, 0, self.ids)],
        }
        partners = self.env.user.partner_id
        if self.res_model == 'res.partner' and self.res_id and self.res_id not in partners.ids:
            action['context'].update({
                'default_representative_ids': [(4, self.res_id), (4, self.env.user.partner_id.id)],
            })
        model = self.env[self.res_model].browse(self.res_id)
        if self.res_model in ['helpdesk.ticket', 'sale.order', 'project.task'] and model.partner_id.id \
                and model.partner_id.id not in partners.ids:
            action['context'].update({
                'default_representative_ids': [(4, model.partner_id.id), (4, self.env.user.partner_id.id)],
            })
        if self.res_model == 'event.event' and model.organizer_id.id and model.organizer_id.id not in partners.ids:
            action['context'].update({
                'default_representative_ids': [(4, model.organizer_id.id), (4, self.env.user.partner_id.id)],
            })
        if self.env.context.get('default_res_model') == 'crm.lead' and model.partner_id.id:
            action['context'].update({
                'model_id': self.env['ir.model']._get_id(self.env.context.get('default_res_model')),
                'res_id': self.env.context.get('default_res_id'),
                'model_name': self.env.context.get('default_res_model'),
                'default_representative_ids': [(4, model.partner_id.id), (4, self.env.user.partner_id.id)],
            })
        return action


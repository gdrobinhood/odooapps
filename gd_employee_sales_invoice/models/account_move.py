# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    hr_employee_id = fields.Many2one('hr.employee', string='Employee')
    
    @api.onchange('partner_id')
    def _onchange_partner_hr_employee_id(self):
        for record in self:
            if record.partner_id:
                if record.partner_id.hr_employee_id:
                    record.hr_employee_id = record.partner_id.hr_employee_id.id
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    hr_employee_id = fields.Many2one('hr.employee', string='Employee')
    
    @api.onchange('partner_id')
    def _onchange_partner_hr_employee_id(self):
        for record in self:
            if record.partner_id:
                if record.partner_id.hr_employee_id:
                    record.hr_employee_id = record.partner_id.hr_employee_id.id
        
    
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res['hr_employee_id'] = self.hr_employee_id.id
        return res
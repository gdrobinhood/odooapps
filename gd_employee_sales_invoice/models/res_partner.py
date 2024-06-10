# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    hr_employee_id = fields.Many2one('hr.employee', string='Employee')
    
    

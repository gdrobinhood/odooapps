# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    sales_order_count = fields.Integer(compute='_compute_sales_order', string='Number of Sales Order')

    def _compute_sales_order(self):
        for employee in self:
            orders = self.env['sale.order'].sudo().search([('hr_employee_id','=',employee.id)])
            employee.sales_order_count = len(orders)
                
    def display_employee_sales_order(self):
        if self.id:
            context="{'group_by':'state'}"
            return {
                'name': _('Sales'),
                'view_mode': 'kanban,tree,calendar,pivot,graph,form',
                'res_model': 'sale.order',
                'type': 'ir.actions.act_window',
                'domain': [('hr_employee_id','=',self.id)],
                'context': context
             }




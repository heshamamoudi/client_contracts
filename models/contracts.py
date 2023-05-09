# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class client_contract(models.Model):
    _name = 'client_contract.contract'
    _description = 'clients Contracts Module provides contracting methods'

    name = fields.Char(string='Name', required=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Client',
                                 domain="[('is_company','=',True),('is_customer','=',True)]")
    date = fields.Date(string='Contract Date')
    client_responsible = fields.Many2one('res.partner',
                                         domain="[('is_company','=',False),('is_customer','=',False),('parent_id','=',partner_id)]")
    # supply information
    product_type = fields.Many2one('client_contract.product', string='Product Type')
    monthly_pay = fields.Float(string='Monthly Payment Amount')
    monthly_vat = fields.Float(string='Monthly Payment Amount')
    monthly_total = fields.Float(string='Monthly Payment Amount VAT Inclusive')
    total = fields.Float(string='Total Paid Amount')
    monthly_pay_type = fields.Many2one('client_contract.payment.month', string='Total Monthly Payments')
    annual_pay_type = fields.Many2one('client_contract.payment', string='Total Monthly Payments')
    init_pay = fields.Float(string='Initial Payment Amount')
    due_init = fields.Date(string='Due Date of Initial Payment Amount')
    last_pay = fields.Float(string='Last Payment Amount')
    due_last = fields.Date(string='Due Date of Last Payment Amount')
    contract_types = fields.Many2many('client_contract.appendix', string='Appendixes Applies On Contract')
    seq_date = fields.Datetime(string='Sequence Creation Date', store=True, default=lambda self: fields.datetime.now())

    @api.model_create_multi
    def create(self, vals):
        for vals in vals:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['seq_date'])
                ) if 'date_order' in vals else None
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'client_contract_contract', sequence_date=seq_date) or _("New")
        return super().create(vals)


class client_contract_appendix(models.Model):
    _name = 'client_contract.appendix'
    _description = 'Appendixes for Client Contracts'

    name = fields.Char(string='Name', translate=True)
    lines = fields.Many2many('client_contract.appendix.line', string='Lines Applies on Appendix')


class client_contract_appendix_line(models.Model):
    _name = 'client_contract.appendix.line'
    _description = 'Appendixes Line for Client Contracts'

    name = fields.Char(string='Name', translate=True)
    description = fields.Char(string='Description')

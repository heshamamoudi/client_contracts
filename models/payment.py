from odoo import models, fields, api


class client_contract_payment(models.Model):
    _name = 'client_contract.payment'
    _description = 'clients Contracts Module provides contracting methods annual payment types'

    name = fields.Char(string='Name', translate=True)


class client_contract_payment_month(models.Model):
    _name = 'client_contract.payment.month'
    _description = 'clients Contracts Module provides contracting methods monthly payment types'

    name = fields.Char(string='Name', translate=True)

from odoo import models, fields, api


class client_contract_product(models.Model):
    _name = 'client_contract.product'
    _description = 'clients Contracts Module provides contracting methods product types'

    name = fields.Char(string='Name',translate=True)

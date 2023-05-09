from odoo import models, fields, api


class client_contract(models.Model):
    _inherit = 'res.partner'

    land_mark = fields.Char(string='Landmark Name')
    national_address = fields.Char(string='National Address Short Code')

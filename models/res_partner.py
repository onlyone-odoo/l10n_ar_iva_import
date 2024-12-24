from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    account_iva_file_id = fields.Many2one("account.iva.file", string="Archivo de IVA")

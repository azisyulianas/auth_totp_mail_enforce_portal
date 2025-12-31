from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auth_totp_policy = fields.Selection(selection_add=[
        ('portal_required', 'Portal users only'),
    ])
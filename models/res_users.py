from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _mfa_type(self):
        r = super()._mfa_type()
        if r is not None:
            return r
        ICP = self.env['ir.config_parameter'].sudo()
        if ICP.get_param('auth_totp.policy') == 'portal_required' and not self.env.user.email:
            return 'totp_mail'
        return r
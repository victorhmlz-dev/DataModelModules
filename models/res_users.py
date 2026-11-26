# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):
    """Campos comunes a Customer y Employee.

    name, email y phone ya vienen de res.users (via su res.partner),
    solo falta el apellido.
    """
    _inherit = 'res.users'

    lastname = fields.Char(string='Apellido')

# -*- coding: utf-8 -*-

# pyrefly: ignore[missing-import]
from odoo import models, fields, api


class Customer(models.Model):
    _name = 'dmm.customer'
    _description = 'dmm.dmm'

    name = fields.Char()
    phone = fields.Integer()
    mail = fields.Char()

    
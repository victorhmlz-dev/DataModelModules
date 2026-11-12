# -*- coding: utf-8 -*-

# pyrefly: ignore[missing-import]
from odoo import models, fields, api


class Item(models.Model):
    _name = 'dmm.item'
    _description = 'dmm.dmm'

    name = fields.Char()
    description = fields.Char()
    price = fields.float()
    category = fields.Char()
    disponibility = fields.boolean()

    orders = fields.Many2many('dmm.order')
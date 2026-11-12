# -*- coding: utf-8 -*-

# pyrefly: ignore[missing-import]
from odoo import models, fields, api


class Order(models.Model):
    _name = 'dmm.order'
    _description = 'dmm.dmm'

    date = fields.Date()
    status = fields.Char()
    total = fields.float()
    pay_method = fields.Char()

    tables = fields.One2many('dmm.table', order)
    items = fields.Many2many('dmm.item')
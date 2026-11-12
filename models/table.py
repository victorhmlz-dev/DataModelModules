# -*- coding: utf-8 -*-

# pyrefly: ignore[missing-import]
from odoo import models, fields, api


class Table(models.Model):
    _name = 'dmm.table'
    _description = 'dmm.dmm'

    number = fields.Integer()
    capacity = fields.Integer()
    location = fields.Char()
    status = fields.Char()

    
    order = fields.Many2one('dmm.order')
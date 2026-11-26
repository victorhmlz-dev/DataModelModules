# -*- coding: utf-8 -*-

from odoo import models, fields


class Table(models.Model):
    _name = 'dmm.table'
    _description = 'Table'

    number = fields.Integer(string='Número')
    capacity = fields.Integer(string='Capacidad')
    location = fields.Char(string='Ubicación')
    status = fields.Char(string='Estado')

    order = fields.Many2one('dmm.order', string='Pedido')
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Table(models.Model):
    _name = 'dmm.table'
    _description = 'Table'

    number = fields.Integer(string='Número')
    capacity = fields.Integer(string='Capacidad')
    location = fields.Char(string='Ubicación')
    status = fields.Char(string='Estado')

    # Relación con Pedido
    order = fields.Many2one('dmm.order', string='Pedido')

    # Relación con Empleado/Camarero asignado
    employee = fields.Many2one('res.users', string='Camarero asignado')

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _inherit = 'res.users'

    visits = fields.Integer(string='Visitas')
    status = fields.Char(string='Estado')
    spent = fields.Float(string='Gasto total')

    # Pedidos realizados por el cliente
    # Usamos 'customer_orders' para evitar conflicto con los pedidos de empleado en res.users
    customer_orders = fields.One2many('dmm.order', 'customer', string='Pedidos del cliente')

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'res.users'

    rol = fields.Char(string='Rol')

    # Pedidos atendidos por el empleado
    # Usamos 'employee_orders' para evitar conflicto con los pedidos de cliente en res.users
    employee_orders = fields.One2many('dmm.order', 'employee', string='Pedidos atendidos')
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _name = 'dmm.order'
    _description = 'Order'

    date = fields.Date(string='Fecha')
    status = fields.Char(string='Estado')
    total = fields.Float(string='Total')
    pay_method = fields.Char(string='Método de pago')

    # Relaciones con Cliente y Empleado (ambos heredan de res.users)
    employee = fields.Many2one('res.users', string='Empleado / Camarero', required=True)
    customer = fields.Many2one('res.users', string='Cliente', required=True)

    # Relación con Mesas y Productos
    tables = fields.One2many('dmm.table', 'order', string='Mesas')
    products = fields.Many2many(
        'dmm.product',
        'dmm_order_product_rel',
        'order_id',
        'product_id',
        string='Productos'
    )
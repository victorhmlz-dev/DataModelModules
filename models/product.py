# -*- coding: utf-8 -*-

from odoo import models, fields


class Product(models.Model):
    _name = 'dmm.product'
    _description = 'Product'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    price = fields.Float(string='Precio')
    category = fields.Char(string='Categoría')
    disponibility = fields.Boolean(string='Disponible')

    orders = fields.Many2many('dmm.order', 'dmm_order_product_rel', string='Pedidos')

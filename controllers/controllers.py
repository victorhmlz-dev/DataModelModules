# -*- coding: utf-8 -*-
# from odoo import http


# class Dmm(http.Controller):
#     @http.route('/dmm/dmm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dmm/dmm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dmm.listing', {
#             'root': '/dmm/dmm',
#             'objects': http.request.env['dmm.dmm'].search([]),
#         })

#     @http.route('/dmm/dmm/objects/<model("dmm.dmm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dmm.object', {
#             'object': obj
#         })

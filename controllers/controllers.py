# -*- coding: utf-8 -*-
# from odoo import http


# class CustomKbi(http.Controller):
#     @http.route('/custom_kbi/custom_kbi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_kbi/custom_kbi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_kbi.listing', {
#             'root': '/custom_kbi/custom_kbi',
#             'objects': http.request.env['custom_kbi.custom_kbi'].search([]),
#         })

#     @http.route('/custom_kbi/custom_kbi/objects/<model("custom_kbi.custom_kbi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_kbi.object', {
#             'object': obj
#         })


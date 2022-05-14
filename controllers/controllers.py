# -*- coding: utf-8 -*-
# from odoo import http


# class OdooCome2pay(http.Controller):
#     @http.route('/odoo_come2pay/odoo_come2pay/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_come2pay/odoo_come2pay/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_come2pay.listing', {
#             'root': '/odoo_come2pay/odoo_come2pay',
#             'objects': http.request.env['odoo_come2pay.odoo_come2pay'].search([]),
#         })

#     @http.route('/odoo_come2pay/odoo_come2pay/objects/<model("odoo_come2pay.odoo_come2pay"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_come2pay.object', {
#             'object': obj
#         })

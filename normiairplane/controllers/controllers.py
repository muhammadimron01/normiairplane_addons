# -*- coding: utf-8 -*-
# from odoo import http


# class Normiairplane(http.Controller):
#     @http.route('/normiairplane/normiairplane', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/normiairplane/normiairplane/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('normiairplane.listing', {
#             'root': '/normiairplane/normiairplane',
#             'objects': http.request.env['normiairplane.normiairplane'].search([]),
#         })

#     @http.route('/normiairplane/normiairplane/objects/<model("normiairplane.normiairplane"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('normiairplane.object', {
#             'object': obj
#         })

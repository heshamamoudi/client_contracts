# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SignDocumentController(http.Controller):

    @http.route('/sign_document/<model("my.model"):document>', type='http', auth='public')
    def sign_document(self, document):
        values = {
            'document': document,
        }


    @http.route('/sign_document/sign', type='http', auth='public', methods=['POST'])
    def sign_document_submit(self, **post):
        document_id = int(post.get('document_id'))
        signature = post.get('signature')

        document = request.env['my.model'].sudo().browse(document_id)
        document.write({'signature': signature})

        return http.request.redirect('/sign_document/thank_you')


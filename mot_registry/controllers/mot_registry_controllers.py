from odoo import http

class Registry(http.Controller):
    @http.route('/kawiil/', auth='public', website=True)
    def index(self, **kw):
        return "O hai mark"
    
    @http.route('/compare/', auth='public', website=True)
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        return http.request.render('mot_registry.website', {
            'motorcycles':motorcycles,
        })
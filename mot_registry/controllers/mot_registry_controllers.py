from odoo import http

class Registry(http.Controller):
    @http.route('/kawiil/', auth='public', website=True)
    def index(self, **kw):
        return "O hai mark"
    
    @http.route('/compare/', auth='public', website=True)
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','Motorcycle')])
        return http.request.render('motorcycle.registry.website', {
            'motorcycles':motorcycles,
        })
    '''
    @http.route('/motorcycles/<model("product.template"):4m0gus>/', auth='public', website=True)
    def motorcycles(self, motorcycles):
        return http.request.render('product.product.template')
    '''
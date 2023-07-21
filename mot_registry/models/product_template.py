from odoo import models
from odoo import fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
    ], ondelete={'motorcycle': 'set product'})

    def _detailed_type_mapping(self):
        return {'motorcycle':'product',}

    # Motorcycle specific fields
    horsepower = dbstuffbutsmaller.Float()
    top_speed = dbstuffbutsmaller.Float()
    torque = dbstuffbutsmaller.Float()
    battery_capacity = dbstuffbutsmaller.Float()
    charge_time = dbstuffbutsmaller.Float()
    range = dbstuffbutsmaller.Float()
    curb_weight = dbstuffbutsmaller.Float()
    make = dbstuffbutsmaller.Char()
    model = dbstuffbutsmaller.Char()
    year = dbstuffbutsmaller.Integer()
    launch_date = dbstuffbutsmaller.Date()

''' Bad code, here for sentimental reasons
# Inheritance stuff
    #_inherits = {'product.template':'detailed_type',}
    _inherit = 'product.template'
    detailed_type = dbstuffbutsmaller.Selection(selection_add=[ 
        ('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set consu'})
    
    route_ids = dbstuffbutsmaller.Many2many(
        comodel='stock.route', relation='stock_route_motorcycle', column1='registry_number', column2='route_id',
        domain=[('product_selectable', '=', True)],
        help="Depending on the modules installed, this will allow you to define the route of the product: whether it will be bought, manufactured, replenished on order, etc.")
    
'''
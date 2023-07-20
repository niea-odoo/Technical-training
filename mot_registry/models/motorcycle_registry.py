from odoo import models as dbstuff
from odoo import fields as dbstuffbutsmaller
from odoo import api
from odoo.exceptions import ValidationError
import re

class Motorcycle_registry(dbstuff.Model):
    """Registry instance for a motorcycle 
    managed or sold by the business"""

    # Inheritance stuff
    _inherit = 'product.template'
    detailed_type = dbstuffbutsmaller.Selection(selection_add=[ 
        ('motorcycle', 'Motorcycle')], ondelete={'motorcycle': 'set consu'})
    route_ids = dbstuffbutsmaller.Many2many(
        'stock.route', 'stock_route_motorcycle', 'registry_number', 'route_id', 'Routes',
        domain=[('product_selectable', '=', True)],
        help="Depending on the modules installed, this will allow you to define the route of the product: whether it will be bought, manufactured, replenished on order, etc.")

    # Fields
    _name = 'motorcycle.registry'
    _description = 'motor vehicle registry'

    registry_number = dbstuffbutsmaller.Char(required = True, 
                                             default=lambda self:self.env['ir.sequence'].next_by_code('motorcycle.registry.number'))
    _rec_name = 'registry_number'

    partner_id = dbstuffbutsmaller.Many2one(comodel_name='res.partner',
                                            string='Owner')

    picture = dbstuffbutsmaller.Image()
    current_mileage = dbstuffbutsmaller.Float()
    certificate_title = dbstuffbutsmaller.Binary()
    register_date = dbstuffbutsmaller.Date()

    _sql_constraints = [
        ('mot_registry_number_uniq', 'unique (registry_number)', 'This registry number has already been assigned'),
        ('mot_registry_vin_uniq', 'unique (vin)', 'The VIN already exists!')
    ]

    # Constrained fields
    vin = dbstuffbutsmaller.Char(required = True)
    license_plate = dbstuffbutsmaller.Char()

    # Computed fields
    make = dbstuffbutsmaller.Char(compute='compute_make_field_values')
    model = dbstuffbutsmaller.Char(compute='compute_model_field_values')
    year = dbstuffbutsmaller.Date(compute='compute_year_field_values')
    
    # Related fields
    email=dbstuffbutsmaller.Char(related='partner_id.email')
    phone=dbstuffbutsmaller.Char(related='partner_id.phone')


    @api.constrains('license_plate')
    def _check_license_plate(self):
        pattern = r'^[A-Z](?:[A-Z]{3}|[A-Z]{2}|[A-Z]?)[0-9][0-9]?[A-Z]?[A-Z]?$'
        for motorcycle_registry in self:
            #({1A}{2A}{3A}{4A})({2}|{1})({2A}|{})
            if( re.match(pattern , motorcycle_registry.license_plate) ):
                continue
            else:
                raise ValidationError("License plates must conform to defined rules")

    @api.constrains('vin')
    def _check_vin(self):
        pattern = r'^[A-Z]{4}[0-9]{2}(?:[A-Z]{2}|[0-9]{2})[0-9]{6}$'
        for motorcycle_registry in self:
            #{2A}{2A}{2}({2A}||{2}){6}
            if( re.match(pattern , motorcycle_registry.vin) ):
                continue
            else:
                raise ValidationError("VIN must conform to defined rules")

    @api.depends('vin')
    def compute_make_field_values(self,):
        for record in self:
            if record.license_plate == None:
                continue
            else:
                record.nake = record.license_plate[:2]

    def compute_model_field_values(self,):
        for record in self:
            if record.license_plate == None:
                continue
            else:
                record.nake = record.license_plate[2:4]

    def compute_year_field_values(self,):
        for record in self:
            if record.license_plate == None:
                continue
            else:
                record.nake = record.license_plate[4:6]

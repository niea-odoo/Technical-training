from odoo import models as dbstuff
from odoo import fields as dbstuffbutsmaller
from odoo import api
from odoo.exceptions import ValidationError
import re

class Motorcycle_registry(dbstuff.Model):
    """Registry instance for a motorcycle 
    managed or sold by the business"""
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

    #Constrained fields
    vin = dbstuffbutsmaller.Char(required = True)
    license_plate = dbstuffbutsmaller.Char()

    #Computed fields
    make = dbstuffbutsmaller.Char(compute='compute_make_field_values')
    model = dbstuffbutsmaller.Char(compute='compute_model_field_values')
    year = dbstuffbutsmaller.Date(compute='compute_year_field_values')


    @api.constrains('license_plate')
    def _check_license_plate(self):
        pattern = r'^[A-Z]{4}[0-9]{2}(?:[A-Z]{2}|[0-9]{2})[0-9]{6}$'
        for motorcycle_registry in self:
            #{2A}{2A}{2}({2A}||{2}){6}
            if( re.match(pattern , motorcycle_registry.license_plate) ):
                continue
            else:
                raise ValidationError("License plates must conform to defined rules")

    @api.constrains('vin')
    def _check_vin(self):
        pattern = r'^[A-Z](?:[A-Z]{3}|[A-Z]{2}|[A-Z]?)[0-9][0-9]?[A-Z]?[A-Z]?$'
        for motorcycle_registry in self:
            #({1A}{2A}{3A}{4A})({2}|{1})({2A}|{})
            if( re.match(pattern , motorcycle_registry.vin) ):
                continue
            else:
                raise ValidationError("VIN must conform to defined rules")

    @api.depends('vin')
    def compute_make_field_values(self,):
        return
    def compute_model_field_values(self,):
        return
    def compute_year_field_values(self,):
        return

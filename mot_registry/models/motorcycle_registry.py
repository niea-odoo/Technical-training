from odoo import models as dbstuff
from odoo import fields as dbstuffbutsmaller

class Motorcycle_registry(dbstuff.Model):
    """Registry instance for a motorcycle 
    managed or sold by the business"""
    _name = 'motorcycle.registry'
    _description = 'motor vehicle registry'

    registry_number = dbstuffbutsmaller.Char(required = True)
    _rec_name = 'registry_number'

    

    vin = dbstuffbutsmaller.Char(required = True)
    first_name = dbstuffbutsmaller.Char(required = True)
    last_name = dbstuffbutsmaller.Char(required=True)
    license_plate = dbstuffbutsmaller.Char()

    picture = dbstuffbutsmaller.Image()

    current_mileage = dbstuffbutsmaller.Float()

    certificate_title = dbstuffbutsmaller.Binary()

    register_date = dbstuffbutsmaller.Date()

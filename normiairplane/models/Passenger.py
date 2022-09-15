from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Passenger(models.Model):
    _name = 'normiairplane.passenger'
    _description = 'Passenger'

    name = fields.Char(string='Passenger Name', required=True)
    nationality = fields.Selection([
        ('indonesia', 'Indonesia'),
        ('malaysia', 'Malaysia'),
        ('singapore', 'Singapore'),
    ], string='Nationality', required=True)
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)
    passport = fields.Char(string='Passport Number', required=True)
    address = fields.Char(string='Address', required=True)
    phone = fields.Char(string='Phone', required=True)
    ticket_ids = fields.One2many(comodel_name='normiairplane.ticket',
                                 inverse_name='passenger_id', 
                                 string='Ticket List')

    @api.constrains('name')
    def constrains_name(self):
        passengers = self.env['normiairplane.passenger'].search([]).mapped('name')  
        if len(passengers) != len(set(passengers)):
            raise ValidationError('Name has been used. Please enter another name.')
        
        for rec in self:
            if(rec.name < 3):
                raise ValidationError('Name must be more than three characters')
        
    
    
    

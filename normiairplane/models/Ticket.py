from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Ticket(models.Model):
    _name = 'normiairplane.ticket'
    _description = 'Ticket'

    name = fields.Char(string='Ticket Code', required=True)
    passenger_id = fields.Many2one(comodel_name='normiairplane.passenger', 
                                   string='Passengers',
                                   required=True)
    flight_id = fields.Many2one(comodel_name='normiairplane.flight', 
                                string='Flights',
                                required=True)
    gender = fields.Char(compute='_compute_gender', string='Gender')
    passport = fields.Char(string='Passport Number')
    nationality = fields.Char(string='Nationality')
    total = fields.Integer(string='Total', required=True)
    price = fields.Integer(compute='_compute_price', string='Price')
    purchase_date = fields.Datetime(string='Date', required=True)

    state = fields.Selection([
        ('none', ''),
        ('booking', 'Booking'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, default='none')
    
    def confirm_button(self):
        self.write({'state': 'confirm'}) 

    def done_button(self):
        self.write({'state': 'done'}) 
    
    def cancel_button(self):
        self.write({'state': 'cancel'}) 
    
    @api.depends('passenger_id')
    def _compute_gender(self):
        for rec in self:
            passenger = self.env['normiairplane.passenger'].search([('id', '=', rec.passenger_id.id)])
            rec.gender = passenger.gender
            rec.passport = passenger.passport
            rec.nationality = passenger.nationality
    
    @api.depends('flight_id')
    def _compute_price(self):
        for rec in self:
            flight = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
            rec.price = flight.price * rec.total
    
    @api.model
    def create(self, vals):
        record = super(Ticket, self).create(vals)
        record.write({'state': 'booking'})
        if record.flight_id:
            self.env['normiairplane.flight'].search([('id', '=', record.flight_id.id)]).write({'seat': record.flight_id.seat - record.total})
        return record
    
    @api.ondelete(at_uninstall=False)
    def _ondelete_flight_seat(self):
        if self.filtered(lambda line: line.state != 'cancel'):
            raise ValidationError('Mohon maaf, data hanya bisa dihapus ketika pengguna membatalkan pemesanan')
        else:
            if(self.flight_id):
                a = []
                for rec in self:
                    a = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
                for ob in a:
                    ob.seat += self.total
    
    def write(self, vals):
        a = []
        for rec in self:
            a = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
        for data in a:
            data.seat += self.total
        record = super(Ticket, self).write(vals)
        b = []
        for rec in self:
            b = self.env['normiairplane.flight'].search([('id', '=', rec.flight_id.id)])
        for databaru in b:
            if databaru in a:
                databaru.seat -= self.total
            else:
                pass
        return record
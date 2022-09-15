from odoo import api, fields, models


class Flight(models.Model):
    _name = 'normiairplane.flight'
    _description = 'Flight Item'

    name = fields.Char(string='Flight Code', required=True)
    source = fields.Selection(string='Source',
                              required=True,
                              selection=[
                                ('jakarta', 'Jakarta'),
                                ('bandung', 'Bandung'),
                                ('semarang', 'Semarang'),
                                ('yogyakarta', 'Yogyakarta'),
                                ('surabaya', 'Surabaya'),
                                ('bali', 'Bali'),
                                ('lombok', 'Lombok'),
                                ('batam', 'Batam'),
                                ('medan', 'Medan'),
                                ('padang', 'Padang'),
                                ('pekanbaru', 'Pekanbaru'),
                                ('palembang', 'Palembang'),
                                ('tanjung_pinang', 'Tanjung Pinang'),
                                ('lampung', 'Lampung'),
                              ])
    destination = fields.Selection(string='Destination',
                                   required=True, 
                                   selection=[
                                        ('jakarta', 'Jakarta'),
                                        ('bandung', 'Bandung'),
                                        ('semarang', 'Semarang'),
                                        ('yogyakarta', 'Yogyakarta'),
                                        ('surabaya', 'Surabaya'),
                                        ('bali', 'Bali'),
                                        ('lombok', 'Lombok'),
                                        ('batam', 'Batam'),
                                        ('medan', 'Medan'),
                                        ('padang', 'Padang'),
                                        ('pekanbaru', 'Pekanbaru'),
                                        ('palembang', 'Palembang'),
                                        ('tanjung_pinang', 'Tanjung Pinang'),
                                        ('lampung', 'Lampung'),
                                   ])
    take_of = fields.Datetime(string='Take Of Date', required=True)
    price = fields.Integer(string='Price', required=True)
    seat = fields.Integer(string='Remaining Seats', required=True)
    ticket_ids = fields.One2many(comodel_name='normiairplane.ticket',
                                inverse_name='flight_id',           
                                string='Ticket Code')
    

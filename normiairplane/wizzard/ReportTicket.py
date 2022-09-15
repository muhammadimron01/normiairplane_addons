from odoo import api, fields, models

class ReportTicket(models.TransientModel):
    _name = 'normiairplane.reportticket'
    _description = 'New Description'

    from_date = fields.Date(string='From', required=False)
    to_date = fields.Date(string='To', required=False)

    def action_report_ticket(self):
        filter = []
        from_date = self.from_date
        to_date = self.to_date

        if from_date:
            filter += [('purchase_date', '>=', from_date)]
        
        if to_date:
            filter += [('purchase_date', '<=', to_date)]

        income = self.env['normiairplane.ticket'].search_read(filter)
        prices = self.env['normiairplane.ticket'].search([('state', '=', 'done')]).mapped('price')

        total = 0
        for price in prices:
            total += price
        
        data = {
            'income': income,
            'total': total
        }

        return self.env.ref('normiairplane.report_ticket_wizzard_pdf').report_action(self, data=data)


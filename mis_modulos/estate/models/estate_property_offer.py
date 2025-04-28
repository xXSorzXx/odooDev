from odoo import api,fields, models # type: ignore
from datetime import datetime,timedelta # type: ignore
from odoo.exceptions import UserError # type: ignore


class estate_property_offer(models.Model):
    _name="estate_property_offer"
    _description="offer"

    price = fields.Float(string="Price")
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused','Refused')],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate_property", string="Property", required=True)
    validity = fields.Integer(string='Validity (days)',default=7)
    created_date = fields.Date(string="Created Date",default=datetime.today(),readonly = True)
    date_deadline = fields.Date(compute="_calculate_deadline", inverse="_inverse_deadline",string="Deadline", store = True)

    @api.depends("validity", "created_date")
    def _calculate_deadline(self):
        for record in self:
            record.date_deadline = record.created_date + timedelta(days=record.validity)
    
    def _inverse_deadline(self):
        for record in self:
            delta = record.date_deadline - record.created_date
            record.validity = delta.days

    def accept_offer(self):
        for record in self:
            accepted_offer = record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted')
            if accepted_offer:
                raise UserError("Ya existe una oferta aceptada")
            else:
                record.property_id.selling_price = record.price
                record.property_id.buyer = record.partner_id
                record.status = 'accepted'
        return True


    def delete_offer(self):
        for record in self:
            if record.status == 'accepted':
                record.property_id.selling_price = 0
                record.property_id.buyer = 0
            record.status = 'refused'
        return True
from odoo import fields, models # type: ignore

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


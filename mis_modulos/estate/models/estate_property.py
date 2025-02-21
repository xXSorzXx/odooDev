from odoo import fields,models # type: ignore

class estate_property(models.Model):
    _name = "estate_property"
    _description = "test jsor"

    name = fields.Char(required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(help="help")
    date_availability = fields.Date(copy=False, default=fields.Datetime.today)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    garden_orientation = fields.Selection(
        string='garden',
        selection=[('north', 'North'),('south', 'South'), ('easth', 'Easth'), ('west', 'West')],
        help="this is a test of selection"
    
    )
    state = fields.Selection(
        string='state',
        selection=[('new', 'New'), ('offer', 'Offer'), ('received', 'Received'), ('offerAccepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled') ],
        default = 'new',
        copy=False
    )

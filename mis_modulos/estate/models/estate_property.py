from odoo import fields,models # type: ignore

class estate_property(models.Model):
    _name = "estate_property"
    _description = "test jsor"

    name = fields.Char(required=True)
    description = fields.Text(string="label Ui")
    postcode = fields.Char(help="help")
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='garden',
        selection=[('north', 'North'),('south', 'South'), ('easth', 'Easth'), ('west', 'West')],
        help="this is a test of selection"
    )

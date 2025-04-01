from odoo import fields, models #type: ignore

class estate_property_type(models.Model):
    _name = "estate_property_type"
    _description = "types"

    name = fields.Char(required=True)
from odoo import fields, models #type: ignore

class estate_property_tag(models.Model):
    _name = "estate_property_tag"
    _description = "tag"

    name = fields.Char(required=True)
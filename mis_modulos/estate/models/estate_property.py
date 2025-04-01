from odoo import api, fields,models # type: ignore

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
    buyer = fields.Many2one("res.partner", string="Buyer",copy=False)    
    sales_person = fields.Many2one("res.users", string="Sales Person", index=True, tracking=True, default = lambda self: self.env.user)
    tag_ids = fields.Many2many("estate_property_tag", string="Property Tag", default=lambda self: [])
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
    property_type_id = fields.Many2one("estate_property_type", string="Property Type")
    offer_ids = fields.One2many('estate_property_offer', 'property_id')
    total_area = fields.Integer(compute = "_total_area")
    best_price = fields.Float(compute = "_best_price", string="Best Price")    

    @api.depends('garden_area', 'living_area')
    def _total_area(self):
         for record in self:
              record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids')
    def _best_price(self):
         for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0.0
              

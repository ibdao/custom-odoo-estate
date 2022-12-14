from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate module tutorial"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False,
        default=fields.Datetime.end_of(
            fields.Datetime.today(), 'quarter'
        )
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(
        readonly=True, 
        copy=False,
    )
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    garden = fields.Boolean()    
    garage = fields.Boolean()    
    facades = fields.Integer()
    garden_area = fields.Integer()   
    garden_orientation = fields.Selection(
        selection=[
            ('north','North'), 
            ('west','West'), 
            ('south','South'), 
            ('east','East')
        ],
    )

    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        selection = [
            ('new','New'), 
            ('offer received','Offer Received'), 
            ('offer accepted','Offer Accepted'),
            ('sold','Sold'), 
            ('canceled','Canceled')
        ], 
        required=True
    )

    property_type_id = fields.Many2one("res.partner", string="Partner")






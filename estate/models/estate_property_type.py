from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate module many2one relationships"

    name = fields.Char(required=True)
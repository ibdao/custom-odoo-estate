# Following Odoo Dev Tutorial

{
    'name':'Estate Module',
    'depends' : ['base'],
    'data' : [
        'security/ir.model.access.csv', 
        'views/estate_property_views.xml',
        'views/property_type.xml',
        'views/estate_menu.xml'],
    'application' : True,
    'auto_install': True,
    'installable': True,
}
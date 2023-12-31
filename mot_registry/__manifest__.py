{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': 'Motorcycle Registry\n====================\nThis Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.',
    'author': 'niea-odoo',
    'depends':['mrp','website'],
    'website': 'my github repo',
    'category': 'Kawiil/Stuff',


    # MASTER DATA
    'data': [
        'security/mot_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/motorcycle_registry_data.xml',
        'views/mot_registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_views.xml',
        'views/mot_registry_web_templates.xml',
    ],
    # DEMO DATA
    'demo':[
        'demo/demo.xml',
    ],

    'application': True, 
}
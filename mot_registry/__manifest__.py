{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': 'Motorcycle Registry\n====================\nThis Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.',
    'author': 'niea-odoo',
    'website': 'my github repo',
    'category': 'Kawiil/Stuff',

    'application': True, 

    # MASTER DATA
    'data': [
        'security/mot_registry_groups.xml',
        'security/ir.model.access.csv',
        'views/mot_registry_menuitems.xml',
    ],
    # DEMO DATA
    'demo':[
        'demo/demo.xml',
    ],

}
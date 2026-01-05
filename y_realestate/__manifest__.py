{
       'name': "Real Estate Advertising",
       'version': '1.0',
       'depends': ['base'],
       'author': "Chatpong",
       'category': 'Advertising',
       'description': """
       Real Estate Advertising Description
       """, 
       'sequence': -1000,
       'data': [
            'security/ir.model.access.csv',
            'views/property.xml',
            'views/property_type_views.xml',
            'views/property_tag_views.xml',
            'views/menu.xml',
        ],
       'demo': [
            'data/property_demo.xml',
        ],
       'installable': True,
       'application': True,
       'autoinstall': False
   }
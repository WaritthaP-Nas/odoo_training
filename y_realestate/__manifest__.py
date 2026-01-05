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
            'views/menu.xml',
        ],
       'demo': [           
        ],
       'installable': True,
       'application': True,
       'autoinstall': False
   }
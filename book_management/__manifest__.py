{
    'name' : 'Book Management',
    'version' : '1.0.0',
    'category' : 'management',
    'summary' : 'Manage books',
    'description' : 'This module manages books',
    'author' : 'Elantamilkumaran',
    'depends' : ['base'],
    'data' : [
        'views/book_view.xml',
        'security/ir.model.access.csv'
    ],
    'application' : True,
    'installable' : True
}
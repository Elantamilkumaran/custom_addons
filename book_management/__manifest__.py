{
    'name' : 'Book Management',
    'version' : '1.0.0',
    'category' : 'management',
    'summary' : 'Manage books',
    'description' : 'This module manages books',
    'author' : 'Elantamilkumaran',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/book_menu.xml',
        'wizard/book_confirm_wizard_view.xml',
        'data/book_tags.xml'
    ],
    'sequence':-9,
    'application': True,
    'installable' : True
}
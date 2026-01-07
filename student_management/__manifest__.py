{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students',
    'description': 'A simple student management system',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'view/student_view.xml',
    ],
    'installable': True,
    'application': True,
}

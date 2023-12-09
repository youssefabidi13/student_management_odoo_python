{
    'name': 'Student Management',
    'summary': "Student Management Software",
    'sequence': 10,
    'description': "Une solution odoo pour la gestion des étudiants",
    'author': "ABIDI Youssef",
    'website': "https://odoo.com/app/Student_Management",
    'category': 'Students',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/student.xml',
        'views/department_views.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
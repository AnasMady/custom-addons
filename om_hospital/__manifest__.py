{
    'author':'Eng. Anas',
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category':'Hospital',
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'sequence': -200,
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/female.patient.xml',
        'views/appointment.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'application':True,
    'auto_install':False,
    'installable': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
{
    'name' : 'Student Details',
    'version' : '1.0',
    'summary': "Sample module",
    'sequence': 1,
    'description': """
Student Details
======================

Key Features
------------
* Form View
* Tree view
""",
    'category': 'Sales',
    'author': 'Balaraman',
    'website': 'https://github.com/balraman/',
    'depends' : ['base'],
    'data': [
			'views/student_view.xml',
			],
    'images': ['images/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

{
    'name': "Al Hassan E-way Format",
    'author':
        'ENZAPPS',
    'summary': """
This module is for Al Hassan E-way Format.
""",

    'description': """
        This module is for Al Hassan E-way Format.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base','account','sale','contacts','purchase','stock','hr_expense','e_way_bill'],
    "images": ['static/description/icon.png'],
    'data': [
        # 'views/account_move.xml',
        'reports/report.xml',
        'reports/report_views.xml',


        # 'views/newxml.xml',


    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}

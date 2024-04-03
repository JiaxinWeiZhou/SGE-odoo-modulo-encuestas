{
    'name': "jwz_encuestas",

    'summary': """
        Módulo de encuestas""",

    'description': """
        Crea tus encuestas personalizadas
    """,

    'author': "Jiaxin Wei",

    'category': 'Uncategorized',
    'version': '0.1',
    'license':'LGPL-3',

    'depends': ['base'],

    'data': [
        'data/demo.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/actions.xml',
        'views/menu.xml',
        'views/encuesta.xml',
        'views/pregunta.xml',
        'views/respuestas.xml',
        'views/respuestat.xml',
        'views/opcionseleccion.xml'          
    ],
    'demo': [
        'data/demo.xml',
    ],
    'application': True
}

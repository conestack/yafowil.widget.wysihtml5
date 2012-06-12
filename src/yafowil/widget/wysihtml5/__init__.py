import os


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [
        {'resource': 'wysihtml5/dist/wysihtml5-0.3.0.js',
         'thirdparty': True,
         'order': 21,},
        {'resource': 'bootstrap-wysihtml5/lib/js/bootstrap.min.js',
         'thirdparty': True,
         'order': 22,},
        {'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.js',
         'thirdparty': True,
         'order': 22,},
        {'resource': 'widget.js',
         'thirdparty': False,
         'order': 23,}
    ]


def get_css():
    return [
        #{'resource': 'bootstrap-wysihtml5/lib/bootstrap.min.css',
        # 'thirdparty': True,
        # 'order': 20,},
        {'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.css',
         'thirdparty': False,
         'order': 21,},
    ]

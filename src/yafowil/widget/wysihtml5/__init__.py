import os


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [{
        'resource': 'wysihtml5/dist/wysihtml5-0.3.0.min.js',
        'thirdparty': True,
        'order': 20,
    }, {
        'resource': 'widget.js',
        'thirdparty': False,
        'order': 21,
    }]


def get_css():
    return []

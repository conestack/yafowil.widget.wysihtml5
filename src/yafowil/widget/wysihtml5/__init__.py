import os


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [
    {
        'resource': 'wysihtml5/parser_rules/advanced.js',
        'thirdparty': True,
        'order': 20,
    },
    {
        'resource': 'wysihtml5/dist/wysihtml5-0.3.0.js',
        'thirdparty': True,
        'order': 21,
    },
    #{
    #    'resource': 'bootstrap-wysihtml5/lib/js/wysihtml5-0.3.0_rc3.js',
    #    'thirdparty': True,
    #    'order': 20,
    #},
    {
        'resource': 'widget.js',
        'thirdparty': False,
        'order': 22,
    }]


def get_css():
    return []

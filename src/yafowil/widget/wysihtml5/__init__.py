import os
from yafowil.base import factory


# XXX: use fanstatic
resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'group': 'wysihtml',
    'resource': 'wysihtml5/dist/wysihtml5-0.3.0.js',
    'order': 21,
}, {
    'group': 'wysihtml',
    'resource': 'bootstrap-wysihtml5/lib/js/bootstrap.min.js',
    'order': 22,
}, {
    'group': 'wysihtml',
    'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.js',
    'order': 22,
}, {
    'group': 'yafowil.widget.wysihtml',
    'resource': 'widget.js',
    'order': 23,
}]

css = [{
    'group': 'wysihtml',
    'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.css',
    'order': 21,
}, {
    'group': 'yafowil.widget.wysihtml',
    'resource': 'widget.css',
    'order': 22,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.wysihtml5',
                           resourcedir, js=js, css=css)
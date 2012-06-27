import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'resource': 'wysihtml5/dist/wysihtml5-0.3.0.js',
    'thirdparty': True,
    'order': 21,
}, {
    'resource': 'bootstrap-wysihtml5/lib/js/bootstrap.min.js',
    'thirdparty': True,
    'order': 22,
}, {
    'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.js',
    'thirdparty': True,
    'order': 22,
}, {
    'resource': 'widget.js',
    'thirdparty': False,
    'order': 23,
}]

# 'resource': 'bootstrap-wysihtml5/lib/bootstrap.min.css'
# 'thirdparty': True,
# 'order': 20

css = [{
    'resource': 'bootstrap-wysihtml5/src/bootstrap-wysihtml5.css',
    'thirdparty': False,
    'order': 21,
}, {
    'resource': 'widget.css',
    'thirdparty': False,
    'order': 22,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.wysihtml5',
                           resourcedir, js=js, css=css)
from yafowil.base import factory
from yafowil.utils import entry_point
import os


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'yafowil.widget.wysihtml5.dependencies',
    'resource': 'wysihtml5/wysihtml5-0.3.0.js',
    'order': 21,
}, {
    'group': 'yafowil.widget.wysihtml5.dependencies',
    'resource': 'bootstrap3-wysihtml5/bootstrap3-wysihtml5.js',
    'order': 22,
}, {
    'group': 'yafowil.widget.wysihtml5.common',
    'resource': 'widget.js',
    'order': 23,
}]
css = [{
    'group': 'yafowil.widget.wysihtml5.dependencies',
    'resource': 'bootstrap3-wysihtml5/bootstrap-wysihtml5.css',
    'order': 21,
}, {
    'group': 'yafowil.widget.wysihtml5.dependencies',
    'resource': 'bootstrap3-wysihtml5/wysiwyg-color.css',
    'order': 21,
}, {
    'group': 'yafowil.widget.wysihtml5.common',
    'resource': 'widget.css',
    'order': 22,
}]


@entry_point(order=10)
def register():
    from yafowil.widget.wysihtml5 import widget
    factory.register_theme('default', 'yafowil.widget.wysihtml5',
                           resourcedir, js=js, css=css)

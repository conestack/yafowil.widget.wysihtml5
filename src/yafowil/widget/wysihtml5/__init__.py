from yafowil.base import factory
from yafowil.utils import entry_point
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


##############################################################################
# Default
##############################################################################

# webresource ################################################################

scripts = wr.ResourceGroup(
    name='yafowil-wysihtml5-scripts',
    path='yafowil.widget.wysihtml5'
)
scripts.add(wr.ScriptResource(
    name='wysihtml5-js',
    directory=os.path.join(resources_dir, 'wysihtml5'),
    resource='wysihtml5-0.3.0.js',
    compressed='wysihtml5-0.3.0.min.js'
))
scripts.add(wr.ScriptResource(
    name='wysihtml5-bootstrap3-js',
    depends=['jquery-js', 'wysihtml5-js'],
    directory=os.path.join(resources_dir, 'bootstrap3-wysihtml5'),
    resource='bootstrap3-wysihtml5.js',
    compressed='wysihtml5-0.3.0.min.js'
))
scripts.add(wr.ScriptResource(
    name='yafowil-wysihtml5-js',
    depends='wysihtml5-bootstrap3-js',
    directory=resources_dir,
    resource='widget.js',
    compressed='wisget.min.js'
))

styles = wr.ResourceGroup(
    name='yafowil-wysihtml5-styles',
    path='yafowil.widget.wysihtml5'
)
styles.add(wr.StyleResource(
    name='wysihtml5-bootstrap3-css',
    directory=os.path.join(resources_dir, 'bootstrap3-wysihtml5'),
    resource='bootstrap-wysihtml5.css'
))
styles.add(wr.StyleResource(
    name='wysihtml5-bootstrap3-color-css',
    depends='wysihtml5-bootstrap3-css',
    directory=os.path.join(resources_dir, 'bootstrap3-wysihtml5'),
    resource='wysiwyg-color.css'
))
styles.add(wr.StyleResource(
    name='yafowil-wysihtml5-css',
    directory=resources_dir,
    resource='widget.css'
))

# B/C resources ##############################################################

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


##############################################################################
# Registration
##############################################################################

@entry_point(order=10)
def register():
    from yafowil.widget.wysihtml5 import widget  # noqa

    # Default
    factory.register_theme(
        'default', 'yafowil.widget.wysihtml5', resources_dir,
        js=js, css=css
    )
    factory.register_scripts('default', 'yafowil.widget.wysihtml5', scripts)
    factory.register_styles('default', 'yafowil.widget.wysihtml5', styles)

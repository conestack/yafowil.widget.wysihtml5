from yafowil.base import (
    factory,
    fetch_value,
)
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    textarea_renderer,
)
from yafowil.utils import (
    managedprops,
    data_attrs_helper
)


wysihtml5_options = [
    # extra options
    'focus',
    'resize',
    'size',
    'stylesheets',
    # toolbar options
    'color',
    'emphasis',
    'font-styles',
    'html',
    'image',
    'justify',
    'link',
    'lists',
]

@managedprops(*wysihtml5_options)
def wysihtml5_textarea_renderer(widget, data):
    custom_attrs = data_attrs_helper(widget, data, wysihtml5_options)
    return textarea_renderer(widget, data, custom_attrs=custom_attrs)

def wysihtml5_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-wysihtml5'})


factory.register(
    'wysihtml5',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[wysihtml5_textarea_renderer],
    display_renderers=[wysihtml5_display_renderer])

factory.doc['blueprint']['wysihtml5'] = \
"""Add-on blueprint `yafowil.widget.wysihtml5
<http://github.com/bluedynamics/yafowil.widget.wysihtml5/>`_ .
"""

factory.defaults['wysihtml5.default'] = ''

factory.defaults['wysihtml5.wrap'] = None
factory.doc['props']['wysihtml5.wrap'] = \
"""Either ``soft``, ``hard``, ``virtual``, ``physical`` or  ``off``.
"""

factory.defaults['wysihtml5.cols'] = 80
factory.doc['props']['wysihtml5.cols'] = \
"""Number of characters.
"""

factory.defaults['wysihtml5.rows'] = 10
factory.doc['props']['wysihtml5.rows'] = \
"""Number of lines.
"""

factory.defaults['wysihtml5.readonly'] = None
factory.doc['props']['wysihtml5.readonly'] = \
"""Flag for readonly.
"""

factory.defaults['wysihtml5.class'] = 'wysihtml5'

#
# Extra options

factory.defaults['wysihtml5.focus'] = None
factory.doc['props']['wysihtml5.focus'] = \
"""Set the focus to the editor after loading.
Options: widget.
Values: [True|False|None (default)].
"""

factory.defaults['wysihtml5.resize'] = None
factory.doc['props']['wysihtml5.resize'] = \
"""Resize the widget, if content grows out of the textareas display size.
Options: widget.
Values: [True|False|None (default)].
"""

factory.defaults['wysihtml5.size'] = None
factory.doc['props']['wysihtml5.size'] = \
"""Size of toolbar buttons.
Options: bootstrap-wysihtml5.
Values: ['large'|'small'|'mini'|None (default)].
"""

factory.defaults['wysihtml5.stylesheets'] = None
factory.doc['props']['wysihtml5.stylesheets'] = \
"""Additional stylesheets to inject to the editor.
Options: widget.
Values: Stylesheet or list of stylesheets or None.
"""

#
# Toolbar Options

factory.defaults['wysihtml5.color'] = None
factory.doc['props']['wysihtml5.color'] = \
"""Show the color styles toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.emphasis'] = None
factory.doc['props']['wysihtml5.emphasis'] = \
"""Show the emphasis toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.font-styles'] = None
factory.doc['props']['wysihtml5.font-styles'] = \
"""Show the font styles toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.html'] = None
factory.doc['props']['wysihtml5.html'] = \
"""Show the html toolbar button.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.image'] = None
factory.doc['props']['wysihtml5.image'] = \
"""Show the image toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.justify'] = None
factory.doc['props']['wysihtml5.justify'] = \
"""Show the justify styles toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.link'] = None
factory.doc['props']['wysihtml5.link'] = \
"""Show the link toolbar button.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

factory.defaults['wysihtml5.lists'] = None
factory.doc['props']['wysihtml5.lists'] = \
"""Show the list toolbar buttons.
Options: bootstrap-wysihtml5.
Values: [True|False|None (use default)].
"""

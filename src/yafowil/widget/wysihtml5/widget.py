from yafowil.base import (
    factory,
    fetch_value,
)
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    textarea_renderer,
)


def wysihtml5_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-wysihtml5'})


factory.register(
    'wysihtml5',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[textarea_renderer],
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

WYSIHTML5 widget
================

Features
--------

    - renders textarea with wysihtml5 css class and provides a wysihtml5
      resources.

Load requirements::

    >>> import yafowil.loader
    >>> import yafowil.widget.wysihtml5

Test widget::

    >>> from yafowil.base import factory

Render widget::

    >>> widget = factory('wysihtml5', 'rt', props={'required': True})
    >>> widget()
    u'<textarea 
    class="wysihtml5" 
    cols="80" 
    id="input-rt" 
    name="rt" 
    required="required" 
    rows="10"></textarea>'

Widget extraction::

    >>> request = {'rt': ''}
    >>> data = widget.extract(request)

No input was given::

    >>> data.errors
    [ExtractionError('Mandatory field was empty',)]

Empty string in extracted::

    >>> data.extracted
    ''

Widget extraction. Returns markup from tinymce::

    >>> request = {'rt': '<p>1</p>'}
    >>> data = widget.extract(request)
    >>> data.errors
    []

    >>> data.extracted
    '<p>1</p>'

    >>> widget(data)
    u'<textarea 
    class="wysihtml5" 
    cols="80" 
    id="input-rt" 
    name="rt" 
    required="required" 
    rows="10"><p>1</p></textarea>'

Display renderer::

    >>> widget = factory('wysihtml5', 'rt', value='<p>foo</p>', mode='display')
    >>> widget()
    u'<div class="display-wysihtml5"><p>foo</p></div>'

    >>> widget = factory('wysihtml5', 'rt', mode='display')
    >>> widget()
    u'<div class="display-wysihtml5"></div>'

More options::

    >>> widget = factory('wysihtml5', 'rt', props={'required': True,
    ... 'focus': True, 'resize': True, 'size': 'mini', 'color': True,
    ... 'emphasis': True, 'font-styles': True, 'html': True, 'image': True,
    ... 'justify': True, 'link': True, 'lists': True,
    ... 'stylesheets': ['style1', 'style2']})
    >>> widget()
    u'<textarea 
    class="wysihtml5" 
    cols="80" 
    data-color=\'true\' 
    data-emphasis=\'true\' 
    data-focus=\'true\' 
    data-font-styles=\'true\' 
    data-html=\'true\' 
    data-image=\'true\' 
    data-justify=\'true\' 
    data-link=\'true\' 
    data-lists=\'true\' 
    data-resize=\'true\' 
    data-size=\'mini\' 
    data-stylesheets=\'["style1", "style2"]\' 
    id="input-rt" 
    name="rt" 
    required="required" 
    rows="10"></textarea>'

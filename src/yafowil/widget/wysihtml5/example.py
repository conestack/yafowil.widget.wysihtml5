from yafowil.base import factory


DOC_WYSIHTML5 = """
bootstrap-wysihtml5
-------------------

Richtext widget using bootstrap-wysihtml5.

.. code-block:: python

    editor = factory('#field:wysihtml5', props={
        'label': 'wysihtml5 Field',
        'focus': True,
        'resize': True,
        'size': 'mini',
        'color': True,
        'emphasis': True,
        'font-styles': True,
        'html': True,
        'image': True,
        'justify': True,
        'link': True,
        'lists': True,
    })

"""

def get_example():
    ex1 = factory(u'fieldset', name='yafowil_wysihtml5')
    ex1['text'] = factory('#field:wysihtml5', props={
        'label': 'wysihtml5 Field',
        'focus': True,
        'size': 'mini',
        'resize': True,
        'color': True,
        'emphasis': True,
        'font-styles': True,
        'html': True,
        'image': True,
        'justify': True,
        'link': True,
        'lists': True,
    })
    return [{'widget': ex1,
            'doc': DOC_WYSIHTML5,
            'title': 'wysihtml5 Field'}]

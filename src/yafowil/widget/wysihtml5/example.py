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
        'size': 'sm',
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


DOC_WYSIHTML5_DEPRECATION = """
.. raw:: html

    <div class="alert alert-danger">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Deprecation Notice:</strong>
        yafowil.widget.wysihtml5 is 
        <strong>
            deprecated
        </strong>
        and will no longer receive support or further development.
        Please use 
        <a class="link-offset-3"
           href="../++widget++yafowil.widget.tiptap/index.html">
            yafowil.widget.tiptap
        </a>
        instead.
    </div>
"""


def get_example():
    ex1 = factory(u'fieldset', name='yafowil_wysihtml5')
    ex1['text'] = factory('#field:wysihtml5', props={
        'label': 'wysihtml5 Field',
        'focus': True,
        'size': 'sm',
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
    return [{
        'widget': ex1,
        'doc': DOC_WYSIHTML5 if factory.theme != 'bootstrap5'
               else DOC_WYSIHTML5_DEPRECATION + DOC_WYSIHTML5,
        'title': 'wysihtml5 Field',
    }]

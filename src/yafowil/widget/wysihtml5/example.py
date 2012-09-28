from yafowil.base import factory


DOC_WYSIHTML5 = """
WYSIHTML5
---------

Richtext widget using WYSIHTML5.

.. code-block:: python

    part['text'] = factory('#field:wysihtml5', props={
        'label': 'WYSIHTML5 Field'})
"""

def wysihtml5():
    part = factory(u'fieldset', name='yafowilwidgetwysihtml5')
    part['text'] = factory('#field:wysihtml5', props={
        'label': 'WYSIHTML5 Field'})
    return {'widget': part,
            'doc': DOC_WYSIHTML5,
            'title': 'WYSIHTML5 Field'}


def get_example():
    return [wysihtml5()]
from yafowil.base import factory

def get_example():
    part = factory(u'fieldset', name='yafowilwidgetwysihtml5')
    part['text'] = factory('field:label:error:wysihtml5', props={
        'label': 'Enter some text (local, lorem ipsum)',
        'value': ''})
    return [{'widget': part, 'doc': 'TODO'}]

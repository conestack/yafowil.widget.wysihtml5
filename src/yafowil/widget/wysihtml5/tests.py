from node.utils import UNSET
from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
from yafowil.tests import fxml
import yafowil.loader


if not IS_PY2:
    from importlib import reload


class TestWysihtml5Widget(YafowilTestCase):

    def setUp(self):
        super(TestWysihtml5Widget, self).setUp()
        from yafowil.widget.wysihtml5 import widget
        reload(widget)

    def test_renderer(self):
        # Render widget
        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            props={
                'required': True
            })
        self.assertEqual(widget(), (
            '<textarea class="wysihtml5" cols="80" id="input-wysihtml5" '
            'name="wysihtml5" required="required" rows="10"></textarea>'
        ))

    def test_extraction(self):
        # Widget extraction
        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            props={
                'required': True
            })
        # No input was given
        request = {'wysihtml5': ''}
        data = widget.extract(request)
        self.assertEqual(data.errors,
            [ExtractionError('Mandatory field was empty')]
        )
        # Empty string in extracted
        self.assertEqual(data.extracted, '')
        # Widget extraction. Returns markup from tinymce
        request = {'wysihtml5': '<p>1</p>'}
        data = widget.extract(request)
        self.assertEqual(data.errors, [])
        self.assertEqual(data.extracted, '<p>1</p>')
        self.assertEqual(widget(data), (
            '<textarea class="wysihtml5" cols="80" id="input-wysihtml5" '
            'name="wysihtml5" required="required" rows="10"><p>1</p></textarea>'
        ))

    def test_display_renderer(self):
        # Display renderer
        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            value='<p>foo</p>',
            mode='display')
        self.assertEqual(widget(),
            '<div class="display-wysihtml5"><p>foo</p></div>'
        )

        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            mode='display')
        self.assertEqual(widget(),
            '<div class="display-wysihtml5"></div>'
        )

    def test_wysihtml5_options(self):
        # More options
        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            props={
                'required': True,
                'focus': True,
                'resize': True,
                'size': 'xs',
                'color': True,
                'emphasis': True,
                'font-styles': True,
                'html': True,
                'image': True,
                'justify': True,
                'link': True,
                'lists': True,
                'stylesheets': ['style1', 'style2']
            })
        self.assertEqual(widget(), (
            '<textarea class="wysihtml5" cols="80" data-color=\'true\' '
            'data-emphasis=\'true\' data-font-styles=\'true\' '
            'data-html=\'true\' data-image=\'true\' data-justify=\'true\' '
            'data-link=\'true\' data-lists=\'true\' data-size=\'xs\' '
            'id="input-wysihtml5" name="wysihtml5" required="required" '
            'rows="10"></textarea>'
        ))


if __name__ == '__main__':
    unittest.main()                                          # pragma: no cover

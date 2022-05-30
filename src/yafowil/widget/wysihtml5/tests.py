from yafowil.base import ExtractionError
from yafowil.base import factory
from yafowil.compat import IS_PY2
from yafowil.tests import YafowilTestCase
import os
import unittest


if not IS_PY2:
    from importlib import reload


def np(path):
    return path.replace('/', os.path.sep)


class TestWysihtml5Widget(YafowilTestCase):

    def setUp(self):
        super(TestWysihtml5Widget, self).setUp()
        from yafowil.widget import wysihtml5
        from yafowil.widget.wysihtml5 import widget
        reload(widget)
        wysihtml5.register()

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
        self.assertEqual(
            data.errors,
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
        self.assertEqual(
            widget(),
            '<div class="display-wysihtml5"><p>foo</p></div>'
        )

        widget = factory(
            'wysihtml5',
            name='wysihtml5',
            mode='display')
        self.assertEqual(
            widget(),
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

    def test_resources(self):
        factory.theme = 'default'
        resources = factory.get_resources('yafowil.widget.wysihtml5')
        self.assertTrue(resources.directory.endswith(
            np('/wysihtml5/resources')
        ))
        self.assertEqual(resources.path, 'yafowil-wysihtml5')

        scripts = resources.scripts
        self.assertEqual(len(scripts), 3)

        self.assertTrue(scripts[0].directory.endswith(
            np('/wysihtml5/resources/wysihtml5')
        ))
        self.assertEqual(scripts[0].path, 'yafowil-wysihtml5/wysihtml5')
        self.assertEqual(scripts[0].file_name, 'wysihtml5-0.3.0.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        self.assertTrue(scripts[1].directory.endswith(
            np('/wysihtml5/resources/bootstrap3-wysihtml5')
        ))
        self.assertEqual(
            scripts[1].path,
            'yafowil-wysihtml5/bootstrap3-wysihtml5'
        )
        self.assertEqual(scripts[1].file_name, 'bootstrap3-wysihtml5.js')
        self.assertTrue(os.path.exists(scripts[1].file_path))

        self.assertTrue(scripts[2].directory.endswith(
            np('/wysihtml5/resources')
        ))
        self.assertEqual(scripts[2].path, 'yafowil-wysihtml5')
        self.assertEqual(scripts[2].file_name, 'widget.min.js')
        self.assertTrue(os.path.exists(scripts[2].file_path))

        styles = resources.styles
        self.assertEqual(len(styles), 3)

        self.assertTrue(styles[0].directory.endswith(
            np('/wysihtml5/resources/bootstrap3-wysihtml5')
        ))
        self.assertEqual(
            styles[0].path,
            'yafowil-wysihtml5/bootstrap3-wysihtml5'
        )
        self.assertEqual(styles[0].file_name, 'bootstrap-wysihtml5.css')
        self.assertTrue(os.path.exists(styles[0].file_path))

        self.assertTrue(styles[1].directory.endswith(
            np('/wysihtml5/resources/bootstrap3-wysihtml5')
        ))
        self.assertEqual(
            styles[1].path,
            'yafowil-wysihtml5/bootstrap3-wysihtml5'
        )
        self.assertEqual(styles[1].file_name, 'wysiwyg-color.css')
        self.assertTrue(os.path.exists(styles[1].file_path))

        self.assertTrue(styles[2].directory.endswith(
            np('/wysihtml5/resources')
        ))
        self.assertEqual(styles[2].path, 'yafowil-wysihtml5')
        self.assertEqual(styles[2].file_name, 'widget.css')
        self.assertTrue(os.path.exists(styles[2].file_path))


if __name__ == '__main__':
    unittest.main()

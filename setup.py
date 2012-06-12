from setuptools import setup, find_packages
import os

version = '1.2'
shortdesc = 'wysihtml5 richtext widget for YAFOWIL with bootstrap integration'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]', 'yafowil.webob', 'gunicorn']

setup(name='yafowil.widget.wysihtml5',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Environment :: Web Environment',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'License :: OSI Approved :: BSD License',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://github.com/bluedynamics/yafowil.widget.wysihtml5',
      license='Simplified BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['yafowil', 'yafowil.widget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'yafowil',
      ],
      tests_require=tests_require,
      extras_require = dict(
          test=tests_require,
      ),
      test_suite="yafowil.widget.wysihtml5.tests.test_suite",
      entry_points="""
      [yafowil.plugin]
      register = yafowil.widget.wysihtml5:register
      resourcedir = yafowil.widget.wysihtml5:get_resource_dir
      javascripts = yafowil.widget.wysihtml5:get_js
      stylesheets = yafowil.widget.wysihtml5:get_css
      example = yafowil.widget.wysihtml5.example:get_example
      """,
      )

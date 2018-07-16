
History
=======

1.4 (2018-07-16)
----------------

- Python 3 compatibility.
  [rnix]

- Convert doctests to unittests.
  [rnix]


1.3 (2017-03-01)
----------------

- Use ``yafowil.utils.entry_point`` decorator.
  [rnix, 2016-06-28]


1.2 (2015-01-23)
----------------

- Refactor to bootstrap 3 integrating
  ``https://github.com/schnawel007/bootstrap3-wysihtml5``.
  [rnix, 2014-07-03]


1.1
---

- Replace stylesheet options with stylesheets and allow a string as path as
  well as a list of paths to stylesheets to include in wysihtml5 configuration.
  [thet]

- Add configuration options to control the toolbar (font-styles, color,
  emphasis, lists, html, link, image plus extra justify toolbar buttons) as
  well as additional extra configuration options (toolbar size, focus after
  loading, resize automatically and additional stylesheet).
  [thet]

- Pass Javascript widget configuration options via data attributes.
  [thet]

- Don't register the bootstrap.min.js file. This should be done wether with
  yafowil.bootstrap or another Twitter Bootstrap integration package.
  [thet]

- Fix resource group names to reflect the package name.
  [thet]


1.0
---

- make it work
  [thet, 2012-06-12]

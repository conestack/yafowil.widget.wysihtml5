Changes
=======

2.0.1 (2026-10-31)
------------------

- Extend the JS tests to 100 % coverage, all modules including bundles are
  loaded by the tests now.
  [rnix]

- Lint and format the JS code with biome. ``make check`` runs ``biome check``,
  ``make format`` runs ``biome check --write`` (see ``include.mk``). Behavior
  unchanged.
  [rnix]

- JS tooling: Commit ``pnpm-lock.yaml``. Upgrade ``@web/test-runner`` to 1.0
  and run the JS tests headless in Chromium via Playwright. Drop the accidental
  ``install`` dev dependency. Pin patched versions of vulnerable transitive
  dependencies via ``pnpm.overrides``.
  [rnix]

- Modernise the code ruff flags as outdated: ``u''`` prefixes. Behaviour
  unchanged. ``super(Class, self)`` is kept, see ``cone.app``.
  [rnix]

- Sort the imports with ruff (one per line, ``from`` imports first, no
  sections) and format the code with ``ruff format`` (90 characters per line,
  single quotes).
  [rnix]

- Add ``qa.ruff`` domain to Makefile and pin the ruff configuration in
  ``pyproject.toml``, ``make check`` runs ``ruff check``.
  [rnix]

- Drop the Python 2 remnants: ``yafowil.compat`` usage and ``IS_PY2`` branches.
  [rnix]

- Declare ``requires-python = ">=3.10"``.
  [rnix]


2.0.0 (2026-02-03)
------------------

- Refactor package layout to use ``pyproject.toml`` and implicit namespace packages.
  [rnix]

- Rewrite JavaScript using ES6.
  [lenadax]


1.5 (2025-11-03)
----------------

- Pin upper versions of dependencies.
  [lenadax]


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

.. -*- mode: rst -*-

pycountry-convert
-----------------

Extension of Python package `pycountry <https://pypi.python.org/pypi/pycountry>`_ providing conversion functions.


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs| |license|
    * - info
      - |hits| |contributors|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions|
    * - other
      - |requires|


.. |docs| image:: https://readthedocs.org/projects/pycountry-convert/badge/?style=flat
    :alt: Documentation Status
    :target: http://pycountry-convert.readthedocs.io

.. |hits| image:: http://hits.dwyl.io/TuneLab/pycountry-convert.svg
    :alt: Hits
    :target: http://hits.dwyl.io/TuneLab/pycountry-convert

.. |contributors| image:: https://img.shields.io/github/contributors/TuneLab/pycountry-convert.svg
    :alt: Contributors
    :target: https://github.com/TuneLab/pycountry-convert/graphs/contributors

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/TuneLab/pycountry-convert.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/TuneLab/pycountry-convert

.. |coveralls| image:: https://coveralls.io/repos/TuneLab/pycountry-convert/badge.svg?branch=master&service=github
    :alt: Code Coverage Status
    :target: https://coveralls.io/r/TuneLab/pycountry-convert

.. |version| image:: https://img.shields.io/pypi/v/pycountry-convert.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycountry-convert.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |requires| image:: https://requires.io/github/TuneLab/pycountry-convert/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/TuneLab/pycountry-convert/requirements/?branch=master

.. end-badges


Install
-------

.. code-block:: bash

    pip install pycountry-convert


Architecture
------------

Using country data derived from wikipedia, this package provides conversion
functions between ISO country names, country-codes, and continent names.


Functions
---------

- ``map_countries(cn_name_format="default", cn_extras={})``: Return a dict of countries with key as country name (standard and official) with ISO 3166-1 values Alpha 2, Alpha 3, and Numeric. This mapping will include countries defined within `pycountry`, Wikipedia, and whatever extra countries provided by parameter `cn_extras`. Parameter `cn_name_format` will format the country name as request to either be using the default layout `"default"`, lowercase `"lower"`, or uppercase `"upper"`.

- ``country_alpha2_to_continent_code()``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to continent name.

- ``country_alpha2_to_country_name(cn_name_format="default")``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to country name.

- ``country_name_to_country_alpha2(cn_name, cn_name_format="default")``: Convert country name to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .

- ``country_alpha3_to_country_name(cn_name_format="default")``: Convert `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ to country name.

- ``country_name_to_country_alpha3(cn_name, cn_name_format="default")``: Convert country name to `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ .

- ``country_alpha3_to_country_alpha2()``: Convert `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .


Parameter: cn_name_format
---------------------------

- ``COUNTRY_NAME_FORMAT_DEFAULT "default"``: Country names as provide by ``pycountry``.
- ``COUNTRY_NAME_FORMAT_LOWER "lower"``: All lowercase country names.
- ``COUNTRY_NAME_FORMAT_UPPER "upper"``: All uppercase country names.


Parameter: cn_extras
---------------------------

Dictionary of `{ cn_name: cn_alpha2_code, ... }`

Dependencies
------------

``pycountry-convert`` module is built upon Python 3 and has dependencies upon
several Python modules available within `Python Package Index PyPI <https://pypi.python.org/pypi>`_.

- `pycountry <https://pypi.python.org/pypi/pycountry>`_
- `pprintpp <https://pypi.python.org/pypi/pprintpp>`_


.. :changelog:

Release History
===============

0.7.2 (2018-02-16)
------------------
- Python 2.7 supported
- Travis CI testing both Python 2.7 and 3.6.

0.7.1 (2018-02-15)
------------------
- migrate to github/TuneLab.
- Python 2.7 support
- lru_cache()

0.6.7 (2018-02-15)
------------------
- pycountry: added common_name (vgavro)

0.6.6 (2018-01-25)
------------------
- migrate to github/tuneinc.
- LICENSE: MIT

0.6.2 (2017-12-09)
------------------
- readthedocs.org

0.5.4 (2017-12-07)
------------------
- LICENSE: LGPL 3.0

0.5.0 (2017-11-30)
------------------
- README.rst
- Hits and Contributors

0.3.0 (2017-11-27)
------------------
- README.rst
- Travis CI

0.1.9 (2017-03-12)
------------------
- Makefile and README.rst

0.1.8 (2016-11-19)
------------------
- Makefile and README.rst

0.1.0 (2016-11-17)
------------------
- Initial Code
- Code pulled from TuneLab/tune-mv-integration-python
- Country name to Country Alpha-2 Code cleanup

0.0.1 (2016-11-17)
------------------
- Initial commit



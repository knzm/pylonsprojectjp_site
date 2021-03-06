import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'webhelpers',
    'pyramid_mako',
    'pyramid_jinja2',
    'pyramid_layout',
    'pyramid_assetviews',
    'pyramid_fanstatic',
    'js.modernizr',
    'js.bootstrap<3.0',
    'formalchemy',
    'pyramid_tw2',
    'docutils',
    'tw2.core',
    'tw2.forms',
    'tw2.tinymce',
    'formencode',
    'genshi',
    ]

links = [
    "https://github.com/knzm/pyramid_tw2/zipball/master#egg=pyramid_tw2-dev",
    ]

setup(name='pylonsprojectjp',
      version='0.0',
      description='Pylons Project JP',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pylonsprojectjp',
      install_requires=requires,
      dependency_links=links,
      entry_points="""\
      [paste.app_factory]
      main = pylonsprojectjp:main
      [console_scripts]
      initialize_pylonsprojectjp_db = pylonsprojectjp.scripts.initializedb:main
      """,
      )


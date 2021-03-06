import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_mako',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'hashids',
	'colander',
	'deform',
	'WebHelpers2',
	'lxml',
]

setup(
    name='py-shrt-lkr',
    version='0.0',
    description='py-shrt-lkr',
    long_description=README + '\n\n' + CHANGES,
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
    test_suite='py_shrt_lkr',
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = py_shrt_lkr:main
        [console_scripts]
        initialize_py-shrt-lkr_db = py_shrt_lkr.scripts.initializedb:main
    """,
)

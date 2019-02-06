# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '4.1.1.dev0'

setup(
    name='plone.app.contentrules',
    version=version,
    description="Plone integration for plone.contentrules",
    long_description=(open("README.rst").read() + "\n\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Zope2",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='plone automatic content rules',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.app.contentrules',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    extras_require={'test': 'plone.app.testing'},
    install_requires=[
        'setuptools',
        'six',
        'plone.contentrules',
        'plone.memoize',
        'plone.stringinterp',
        'plone.uuid',
        'plone.autoform',
        'plone.app.z3cform',
        'plone.app.vocabularies',
        'transaction',
        'zope.annotation',
        'zope.browser',
        'zope.component',
        'zope.container',
        'zope.event',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.publisher >= 3.11.0',
        'zope.schema',
        'zope.site',
        'zope.traversing',
        'Acquisition',
        'Products.CMFPlone',
        'Products.CMFCore',
        'Products.GenericSetup >= 2.0.dev0',
        'Products.statusmessages',
        'ZODB3',
        'Zope2 >= 2.12.3',
    ],
)

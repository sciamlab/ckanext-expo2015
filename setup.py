from setuptools import setup, find_packages
import sys, os

version = '2.0'

setup(
    name='ckanext-expo2015',
    version=version,
    description="Open Expo 2015 CKAN Extension",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Alessio Dragoni',
    author_email='ad@sciamlab.com',
    url='http://github.com/sciamlab/ckanext-expo2015',
    license='GNU Affero General Public License (AGPL) v3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.expo2015'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        expo2015 = ckanext.expo2015.plugin:Expo2015Plugin
        # Add plugins here, e.g.
        # myplugin=ckanext.expo2015.plugin:PluginClass
    ''',
)

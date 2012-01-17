#!/usr/bin/env python
'''
Created Jan 12, 2012

@author: thalin

Setup script for znote
'''
from distutils.core import setup

setup_dict = {
    'name': 'znote',
    'version': '.1a',
    'description': 'Zeke\'s Notes and Tasks app for Django',
    'author': 'Zeke Harris (thalin)',
    'author_email': 'thalin@zen-finity.com',
    'url': 'git@executor.zen-finity.com:znote.git',
    'install_requires': ['django>=1.3',
                         'django-tastypie>=0.9.11',
                         'django-mptt>=0.5.2',
                         'django-extensions>=0.7.1',
                         'Pygments>=1.4',
                         'django-object-permissions>=1.4.2',
                         'Markdown>=2.1.0'],
    'packages': ['znote']
}

setup(**setup_dict)

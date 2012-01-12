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
    'packages': ['znote']
}

setup(**setup_dict)

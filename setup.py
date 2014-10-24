#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import litfisk

setup(name='litfisk',
      version = litfisk.__version__,
      author = litfisk.__author__ , 
      author_email = litfisk.__email__,
      url = 'http://github.com/johnjosephhorton/litfisk',
      packages = [''],
      package_data = {'':['*.md', 'templates/*']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['litfisk = litfisk:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['pypdf >= 1.13'],
      )


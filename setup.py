#!/usr/bin/env python

from distutils.core import setup

setup(name             = 'doublex',
      version          = '0.3',
      author           = 'David Villa Alises',
      author_email     = 'David.Villa@gmail.com',
      packages         = ['doublex'],
      data_files       = [('/usr/share/doc/python-doublex', ['README.rst'])],
      url              = 'https://bitbucket.org/DavidVilla/python-doublex',
      license          = 'GPLv3',
      description      = 'Test doubles framework for Python',
      long_description = open('README.rst').read(),
      requires         = ['hamcrest'],
      classifiers      = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
)

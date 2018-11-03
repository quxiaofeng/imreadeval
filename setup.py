#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import io
from setuptools import setup

with io.open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='imreadeval',
    version='0.1',
    description='An evaluation to python imread functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Editors :: Raster-Based',
    ],
    url='http://github.com/quxiaofeng/imreadeval',
    author='QU Xiaofeng',
    author_email='xiaofeng.qu@aqara.com',
    install_requires=[
          'matplotlib',
          'Pillow',
          'scipy',
          'scikit-image',
      ],
    license='MIT',
    package=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False
)


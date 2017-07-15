#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nau_net',
    version='1.0.2',
    description='NAU school network CLI.',
    url='https://github.com/zhanba/nau_net',
    author='zhanba',
    author_email='c5e1856@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='NAU network CLI',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'nau': ['conf.ini']},
    install_requires=['click', 'requests', 'beautifulsoup4', 'future'],
    entry_points={
        'console_scripts': [
            'nau = nau.cli:cli',
        ],
    },
    zip_safe=True
)

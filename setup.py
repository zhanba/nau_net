#!/usr/bin/env python
from setuptools import setup

setup(
    name='hive-executor-py',
    version='1.0.0.dev1',
    description='A hive client python project',
    url='https://github.com/calvinjiang/hive-executor-py',
    author='zhanba',
    author_email='c5e1856@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='hive client python',
    packages=['hive'],
)
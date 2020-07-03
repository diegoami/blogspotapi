
#! coding: utf-8
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='blogspotapi',
    version='0.3.4',
    packages=['blogspotapi'],
    include_package_data=True,
    keywords='blogspot api wrapper',
    license='BSD License',
    install_requires=['requests', 'amaraapi'],
    description='Python Blogspot API Wrapper',
    long_description=README,
    url='https://github.com/diegoami/blogspotapi/',
    author='Diego Amicabile',
    author_email='diego.amicabile@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
)
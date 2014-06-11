#!/usr/bin/env python
from setuptools import setup
import os

from templated_emails.version import __version__

long_description = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')).read()

setup(
    name='templated-emails',
    version=__version__,
    url='https://github.com/philippWassibauer/templated-emails',
    author="Philipp Wassibauer",
    author_email="phil@gidsy.com",
    license='MIT License',
    packages=['templated_emails'],
    package_data={
        'templated_emails': [
            'templates/templated_emails/*.html',
        ]
    },
    description='Like django-notifications, but just for sending plain emails. Written because it is annoying to fork other apps just to make an email into an HTML email',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    install_requires=[
        'django',
        'pynliner',
        'cssutils',
    ],
)

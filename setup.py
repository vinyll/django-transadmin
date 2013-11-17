# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='django-transadmin',
    version='0.2.5',
    description='Translate texts from the admin interface.',
    long_description=open('README.md').read(),
    author='Vincent Agnano',
    author_email='vincent.agnano@scopyleft.fr',
    url='http://github.com/vinyll/django-transadmin',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Utilities',
    ]
)

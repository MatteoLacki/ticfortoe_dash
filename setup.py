# This Python file uses the following encoding: utf-8
from setuptools import setup, find_packages

setup(  
    name='ticfortoe_dash',
    packages=find_packages(),
    version='0.0.1',
    description='Description.',
    long_description='Long description.',
    author='MatteoLacki',
    author_email='matteo.lacki@gmail.com',
    url='https://github.com/MatteoLacki/ticfortoe_dash.git',
    keywords=['Great module', 'Devel Inside'],
    classifiers=['Development Status :: 1 - Planning',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering :: Chemistry',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
    install_requires=[
        'dash',
        'dash-bootstrap-components',
        'requests',
        'ticfortoe_dash'
    ]
)

#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files, and 
modifies them according to metamorphic relationships (MRs) 
passed in as parameters.
'''

setup(
    name='mmff',
    version='0.0.1',
    author='Andrew Lonsdale',
    author_email='andrew.lonsdale@lonsbio.com.au',
    packages=['morphs'],
    package_dir={'morphs': 'mmff/morphs'},
    entry_points={
        'console_scripts': ['mmff = mmff.mmff:main']
    },
    url='https://github.com/lonsbio/Mighty-Morphin-FASTA-Files',
    license='LICENSE',
    description=('Metamorphic test generator for FASTA files.'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython==1.68","scikit-bio==0.5.0"],
)

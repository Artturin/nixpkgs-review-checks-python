from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='nixpkgs-review-checks-python',
    version='0.0.1',
    description='',
    packages=find_packages(),
    license='MIT',
    author='Artturin',
    install_requires=[''],
    include_package_data=True,
    package_data={
        '': ['ofborg.graphql']
    },
    entry_points={
        'console_scripts': [
            'nixpkgs-review = nixpkgs_review.main:main'
        ]
    }
)

from setuptools import setup, find_packages

setup(
    name='tilhub',
    version='0.0.01',
    description='TIL, and I do not want to forget',

    author='J. J. A. Costello',

    packages=find_packages(where='tilhub'),
    package_dir={'': 'tilhub'}
)
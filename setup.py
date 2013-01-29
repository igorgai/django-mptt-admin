from setuptools import setup, find_packages


version = '0.1'

setup(
    name='django-mptt-admin',
    version=version,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    include_package_data=True,
    zip_safe=False,
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
)
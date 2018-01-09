"""This is the setup file for the project.
The standard setup rules apply:
python setup.py build
sudo python setup.py install
"""

from distutils.core import setup
from glob import glob

from setuptools import find_packages
from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession

print find_packages()

setup(
    name='HelloWorld',
    version='20180108',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=[str(req.req) for req in parse_requirements(
        'requirements.txt', session=PipSession())
    ])

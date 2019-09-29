##############################################################################
#
#   {{cookiecutter.package_name}}
#
#   Setup script for the package.
#
#   AUTHOR: {{cookiecutter.author}}
#   AFFILIATION: {{cookiecutter.affiliation}}
#   CONTACT: {{cookiecutter.contact}}
#   CREATED: {{cookiecutter.date_created}}
#   LICENSE: {{cookiecutter.license}}
#   USAGE: python setup.py install --user
#
##############################################################################

from setuptools import setup

setup(name="{{cookiecutter.package_name}}",
	version="0.0.0.9000",
	description="",
	url="",
	author="{{cookiecutter.author}}",
	author_email="{{cookiecutter.contact}}",
	license="{{cookiecutter.license}}",
	packages=["{{cookiecutter.package_name}}"],
	zip_safe=False)
##############################################################################
#
#   {{cookiecutter.package_name}}
#
#   Basic package tests.
#
#   AUTHOR: {{cookiecutter.author}}
#   AFFILIATION: {{cookiecutter.affiliation}}
#   CONTACT: {{cookiecutter.contact}}
#   CREATED: {{cookiecutter.date_created}}
#   LICENSE: {{cookiecutter.license}}
#   USAGE: pytest test_basic.py
#
##############################################################################

# import the testing framework
import pytest

# import the package
import {{cookiecutter.package_name}}

##############################################################################

def test_simple_load():
	"""Tests if the package is functional."""
	result =  \
	    {{cookiecutter.package_name}}.{{cookiecutter.module_name}}.f(True)
	assert result

def test_exception():
	"""Tests if the exception is raised correctly."""
	with pytest.raises({{cookiecutter.package_name}}.\
		exceptions.SomethingWentWrong):
			result = {{cookiecutter.module_name}}.f(False)
###############################################################################
#
#   Makefile with useful commands for package development.
#
#   AUTHOR: {{cookiecutter.author}}
#   AFFILIATION: {{cookiecutter.affiliation}}
#   CONTACT: {{cookiecutter.contact}}
#   CREATED: {{cookiecutter.date_created}}
#   LICENSE: {{cookiecutter.license}}
#   USAGE: make [...]
#
###############################################################################

V_ENV = ENV

.PHONY: help test coverage docs env

help:
	@echo "help - display this message"
	@echo "test - run package tests with pytest tool"
	@echo "docs - generate Sphinx HTML documentation"
	@echo "env - create a conda virtual environment for package development"

test:
	pytest

docs:
	$(MAKE) -C docs html
	@echo "Built documentation under: docs/_build/html/index.html"

env:
	conda env create --prefix $(V_ENV) -f environment.yaml
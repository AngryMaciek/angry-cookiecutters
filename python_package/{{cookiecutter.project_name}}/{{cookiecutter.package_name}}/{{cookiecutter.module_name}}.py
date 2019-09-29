##############################################################################
#
#   {{cookiecutter.module_name}}
#
#   Main module of the package.
#
#   AUTHOR: {{cookiecutter.author}}
#   AFFILIATION: {{cookiecutter.affiliation}}
#   CONTACT: {{cookiecutter.contact}}
#   CREATED: {{cookiecutter.date_created}}
#   LICENSE: {{cookiecutter.license}}
#
##############################################################################

# import the module with custom exceptions
import {{cookiecutter.package_name}}.exceptions

##############################################################################

def f(bool):
	"""Sample core function of the package."""
	if bool:
		return(True)
	else:
		raise {{cookiecutter.package_name}}.exceptions.SomethingWentWrong\
			("Error message.")

		
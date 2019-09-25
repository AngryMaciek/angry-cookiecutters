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
import exceptions

##############################################################################

def f(bool):
	"""Sample core function of the package."""
	if bool:
		return(True)
	else:
		raise exceptions.IncorrectInput\
			("Error message.")

		
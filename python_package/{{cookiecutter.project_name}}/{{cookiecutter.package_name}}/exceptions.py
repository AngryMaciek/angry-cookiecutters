##############################################################################
#
#   {{cookiecutter.package_name}}
#
#   Exceptions for the package.
#
#   AUTHOR: {{cookiecutter.author}}
#   AFFILIATION: {{cookiecutter.affiliation}}
#   CONTACT: {{cookiecutter.contact}}
#   CREATED: {{cookiecutter.date_created}}
#   LICENSE: {{cookiecutter.license}}
#
##############################################################################

class Error(Exception):
    """Base class for other exceptions."""
    pass

class SomethingWentWrong(Error):
    """Raised when something went wrong."""
    pass

Installation
============

Virtual environment
-------------------

This is the preferable way to install {{cookiecutter.package_name}}.
If you use `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ (or Anaconda, for that matter) and its virtual environments the package can be installed directly from my channel at Anaconda Cloud service.:

.. code-block:: bash

   conda install -c angrymaciek {{cookiecutter.package_name}}

pip installation
----------------

All the requirements to be installed by ``pip`` are listed in ``requirements.txt``. Clone the repository from GtHub first, install the requirements and then install this package:

.. code-block:: bash

   cd;
   git clone https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
   pip install -r {{cookiecutter.package_name}}/requirements.txt --user;
   pip install {{cookiecutter.package_name}} --user;

Provided all the requirements are satisfied for your default environment it is OK to install the package directly from GitHub:

.. code-block:: bash

   pip install git+https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git --user

Import test
-----------

After the installation please test if the package might be successfully loaded in a ``python`` interpreter:

.. code-block:: python

   import {{cookiecutter.package_name}}
   {{cookiecutter.package_name}}.{{cookiecutter.module_name}}.f(True)
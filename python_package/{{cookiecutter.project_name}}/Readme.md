# {{cookiecutter.package_name}}
*{{cookiecutter.author}}  
{{cookiecutter.affiliation}}*

[General information about the package]

## Installation & Use

### Virtual environment

All the requirements are listed in environment.yaml which is also a base to create a `conda` virtual environment to install and run this package in.
```bash
# clone the repository:
cd;
git clone https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
cd {{cookiecutter.package_name}};
# create a virtual environment and install the package within:
conda env create --prefix ENV -f environment.yaml;
conda activate $HOME/{{cookiecutter.package_name}}/ENV;
pip install .
# test the package in a python interpreter:
python
import {{cookiecutter.package_name}}
{{cookiecutter.package_name}}.{{cookiecutter.module_name}}.f(True)
```

This package has been tested with `pytest` package.
In order to run these tests again activate the virtual environment and run pytest:
```bash
cd $HOME/{{cookiecutter.package_name}};
conda activate $HOME/{{cookiecutter.package_name}}/ENV;
pytest;
```

### Global installation

Provided all the requirements are satisfied for your default environment it is OK to install the package globally and directly from GitHub:  
```bash
pip install git+https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
```

### Package removal

In order to uninstall the package use `pip` (either within a virtual environment of in your default environment):
```bash
pip uninstall {{cookiecutter.package_name}};
```

## License

{{cookiecutter.license}}


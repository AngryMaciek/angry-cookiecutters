# {{cookiecutter.package_name}}
*{{cookiecutter.author}}  
{{cookiecutter.affiliation}}*

[General information about the package]

## Installation & Use

### Virtual environment

All the requirements are listed in requirements.yaml which is also a base to create a `conda` virtual environment to install and run this package in:
```bash
cd;
git clone https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
cd {{cookiecutter.package_name}};
conda env create --prefix ENV -f requirements.yaml;
$HOME/{{cookiecutter.package_name}}/ENV/bin/python setup.py build;
$HOME/{{cookiecutter.package_name}}/ENV/bin/python setup.py install --user;
```

To try the package out activate the virtual environment and start python interpreter:
```bash
conda activate $HOME/{{cookiecutter.package_name}}/ENV;
python
```

```python
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

Provided all the requirements are satisfied for your default python interpreter it is OK to install the package globally.  
  
This package might installed directly from GitHub with `pip`:
```bash
pip install git+https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
```

Alternatively, you can clone the repository and install it manually, just as in the previous section.

In order to uninstall the package use `pip`:
```bash
pip uninstall {{cookiecutter.package_name}};
```

## License

{{cookiecutter.license}}


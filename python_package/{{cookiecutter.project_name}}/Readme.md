# {{cookiecutter.package_name}}
*{{cookiecutter.author}}  
{{cookiecutter.affiliation}}*

[General information about the package]

## Installation & Use

### Virtual environment (preferable)

If you use [miniconda](https://docs.conda.io/en/latest/miniconda.html) (or Anaconda, for that matter) and its virtual environments the package can be installed directly from my channel at [Anaconda Cloud](https://anaconda.org/) service:
```bash
conda install -c angrymaciek {{cookiecutter.package_name}}
```

### pip installation

All the requirements to be installed by `pip` are listed in requirements.txt. Clone the repository first, install the requirements and then install this package:
```bash
cd;
git clone https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git;
cd {{cookiecutter.package_name}};
pip install -r requirements.txt --user;
pip install . --user;
```
Provided all the requirements are satisfied for your default environment it is OK to install the package directly from GitHub:  
```bash
pip install git+https://github.com/AngryMaciek/{{cookiecutter.package_name}}.git --user;
```

### Use test

Test if the package might be successfully loaded in a python interpreter:
```python
import {{cookiecutter.package_name}}
{{cookiecutter.package_name}}.{{cookiecutter.module_name}}.f(True)
```

## License

{{cookiecutter.license}}
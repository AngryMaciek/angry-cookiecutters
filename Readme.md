# Cookie cutters

*Maciej Bak  
Swiss Institute of Bioinformatics*

My collection of project templates for [cookiecutter][1].

## Usage

Install the latest version of cookiecutter,
preferably from [anaconda cloud service][2] (but for that you will need `conda` installed).
```bash
conda install -c conda-forge cookiecutter
```

Clone this repository (under your $HOME directory):
```bash
cd;
git clone https://github.com/AngryMaciek/cookiecutters.git;
```

From now on you can create new projects from templates as:
```bash
cd {directory_for_the_new_project}
cookiecutter $HOME/cookiecutters/{template_directory}
```

## License

GNU General Public License

[1]: https://cookiecutter.readthedocs.io/en/latest/
[2]: https://anaconda.org/
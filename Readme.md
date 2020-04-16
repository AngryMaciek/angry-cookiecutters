# Cookie cutters

*Maciej Bak  
Swiss Institute of Bioinformatics*

My collection of project templates for [cookiecutter][1].

## Usage

Install the latest version of cookiecutter,
preferably from [anaconda cloud service][2] (but for that you will need `conda` installed - see the last section of this document).
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

Apache 2.0

## Appendix: Download, Install and Load Miniconda3

On Linux:
  ```bash
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh
  source .bashrc
  ```

On macOS:
  ```bash
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
  bash Miniconda3-latest-MacOSX-x86_64.sh
  source .bashrc
  ```




[1]: https://cookiecutter.readthedocs.io/en/latest/
[2]: https://anaconda.org/

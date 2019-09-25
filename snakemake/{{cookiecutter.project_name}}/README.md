# Install Snakemake
Snakemake is a workflow management system that helps to create and execute data processing pipelines. It requires python3 and can be most easily installed via the bioconda package of the python anaconda distribution. You're setup right after the following steps:

## Step 1: Downloading Miniconda3 and install it
On Linux:
  ```bash
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh
  source .bashrc
  ```

On MacOS X:
  ```bash
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
  bash Miniconda3-latest-MacOSX-x86_64.sh
  source .bashrc
  ```

## Step 2: Install Snakemake

Install snakemake version which you need (see the dependencies, the latest version is likely a good choice):
  ```bash
  conda install -c bioconda snakemake=5.4.0
  ```

If you are missing some dependancy packages (PackageNotFoundError): check their channels on anaconda cloud and add channels to this command. Conda automatically installs dependancies but you have to have all channels profived:
  ```bash
  conda install -c bioconda -c conda-forge snakemake=5.4.0
  ```

# Run the Pipeline
Adjust the yaml_files/config.yaml to your needs. That is, provide all needed information (input/output).

Write a DAG (directed acyclic graph) into dag.pdf:
  ```bash
  bash snakemake.dag_run
  ```
If you are happy with what will be done, run the pipeline locally:
  ```bash
  bash snakemake.local_run
  ```
or on a cluster environment (if required, adapt the 'slurm_cluster.json' and 'jobscript.sh' files before starting the run):
  ```bash
  bash snakemake.local_run
  ```


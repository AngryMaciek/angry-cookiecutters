# Run the pipeline on a computational cluster

cleanup () {
  rc=$?
  rm -rf .snakemake/
  rm -rf output_dir/
  cd $user_dir
  echo "Exit status: $rc"
}
trap cleanup EXIT

set -eo pipefail  # ensures that script exits at first command that exits with non-zero status
set -u  # ensures that script exits when unset variables are used
set -x  # facilitates debugging by printing out executed commands

user_dir=$PWD
pipeline_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd $pipeline_dir

snakemake \
  --snakefile="Snakefile" \
  --configfile config.yaml \
  --cluster-config cluster_config.json \
  --use-singularity \
  --cores 10 \
  --local-cores 2 \
  --printshellcmds \
  --verbose \
  --cluster \
  "sbatch \
  --cpus-per-task={cluster.threads} \
  --mem={cluster.mem} \
  --qos={cluster.queue} \
  --time={cluster.time} \
  --output={params.LOG_cluster_log}-%j-%N.log \
  -p shi" \
  --singularity-args "--no-home --bind ${PWD}"

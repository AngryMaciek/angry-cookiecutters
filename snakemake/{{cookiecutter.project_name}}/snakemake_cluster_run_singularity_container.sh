# Run the pipeline on a computational cluster

snakemake \
--use-singularity \
--jobscript jobscript_singularity_container.sh \
--configfile config.yaml \
-p \
--cores 10 \
--local-cores 2 \
--cluster-config cluster_config.json \
--cluster \
"sbatch \
--cpus-per-task={cluster.threads} \
--mem={cluster.mem} \
--qos={cluster.queue} \
--time={cluster.time} \
--output={params.LOG_cluster_log}-%j-%N.out \
-p scicore \
--export=JOB_NAME={rule} \
--open-mode=append"

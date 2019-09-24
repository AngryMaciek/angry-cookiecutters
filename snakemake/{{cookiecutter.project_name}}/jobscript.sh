#!/bin/bash
# properties = {properties}

#PATH=~/miniconda3/bin/conda:${{PATH}}
#export PATH

echo -e "JOB ID\t$SLURM_JOBID"
echo "=============================="
echo -e "rule\t$JOB_NAME"
echo -e "=============================="

ml purge
{exec_job}

echo -e "==============================\n"

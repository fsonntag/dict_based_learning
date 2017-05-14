#!/usr/bin/env bash
set -x

source /workspace/dict_based_learning/bin/cloud_env.sh
/workspace/dict_based_learning/bin/train_extractive_qa.py $@ 2>$JOBID.txt 1>&2

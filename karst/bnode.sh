
# Script for cluster nodes to follow.
#
# Basically,
# - each benchmark directory has a list of things to do
# - nodes grab a few configs off the list & run them many times
# - nodes save results to their own temp. directory
#
# There's just a few complications to make filesystem operations faster &
#  hopefully avoid filesystem data races.

## -----------------------------------------------------------------------------
## constants

USER="zmahmoud"
USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"

BOTH="both"
BENCHMARK="Benchmark"
TEST="Test"
MAIN="main.py"

BAK=".bak"
# Suffix for backup files

MUTEX=".lock"
# Suffix for lockfiles

ITERS=40
# Number of iterations to run for each configuration

CHUNK=500
# Number of configurations to grab at once

KARST_INPUT="karst_input.txt"
# List of configurations that need to be run. Each benchmark has one of these.

KARST_OUTPUT="karst_output.txt"
# This script collects results for each benchmark in a `KARST_OUTPUT` file

NODE_INPUT="node_input.txt"
NODE_OUTPUT="node_output.txt"
# Local list of TODO/DONE, so we can clean up after killed nodes

# Use PBS_JOBID as unique id for nodes
NODE_QSTAT="qstat ${PBS_JOBID}"
# To check my status

## -----------------------------------------------------------------------------
## setup RETIC and PYTHON

TAR_SUFFIX="tar.gz"
PYTHON_VERSION="Python-3.4.3"
RETICULATED="reticulated"
RETIC_TAR="${USER_HOME}/${RETICULATED}.${TAR_SUFFIX}"
PYTHON_TAR="${USER_HOME}/${PYTHON_VERSION}.${TAR_SUFFIX}"

MY_TMP="/tmp/${PBS_JOBID}"

mkdir ${MY_TMP}
tar -xzf ${PYTHON_TAR} -C ${MY_TMP}
tar -xzf ${RETIC_TAR} -C ${MY_TMP}

PYTHON_EXEC="${MY_TMP}/${PYTHON_VERSION}/python"
RETIC="${MY_TMP}/${RETICULATED}/retic.py"

# change shebang line to use ${PYTHON_EXEC}
sed -i${BAK} "s,#!.*,#!${PYTHON_EXEC}," ${RETIC}

## -----------------------------------------------------------------------------
## main

while [ 1 ]; do # (remaining_time() > 1): #hours
  # -- pick random benchmark with work left to do
  ALL_BENCHMARKS=()
  for BM in ${RP}/*/; do
    # Valid benchmarks have at least one output folder
    #   http://stackoverflow.com/a/4264351/5237018
    if [ $( find ${BM} -maxdepth 1 -name "${KARST_INPUT}*[0-9]" -print -quit ) ]; then
      ALL_BENCHMARKS+=(${BM})
    fi
  done
  NUM_BENCHMARKS=${#ALL_BENCHMARKS[@]}
  if [ ${NUM_BENCHMARKS} -eq 0 ]; then
    # Couldn't find anything to do
    printf "All jobs finished, ${PBS_JOBID} says goodbye\n"
    break
  fi
  MY_BENCHMARK=${ALL_BENCHMARKS[${RANDOM} % ${NUM_BENCHMARKS} ]}
  # -- pick random non-empty worklist for the benchmark
  ALL_WORKLISTS=()
  for WL in ${MY_BENCHMARK}/${KARST_INPUT}*[0-9]; do
    if [ -s ${WL} ]; then
      ALL_WORKLISTS+=(${WL})
    else
      # empty worklist
      printf "Empty worklist ${WL}\n"
      rm ${WL}
    fi
  done
  NUM_WORKLISTS_LEFT=${#ALL_WORKLISTS[@]}
  if [ ${NUM_WORKLISTS_LEFT} -eq 0 ]; then
    printf "No worklists in directory ${BM}, retrying\n"
    continue
  fi
  MY_WORKLIST=${ALL_WORKLISTS[${RANDOM} % ${NUM_WORKLISTS_LEFT} ]}
  # -- try locking the worklist
  #TODO MY_LOCKFILE=${MY_WORKLIST}${MUTEX}
  MY_LOCKFILE=${MY_BENCHMARK}/${MUTEX}
  if [ -f ${MY_LOCKFILE} ]; then
    printf "Node ${PBS_JOBID} failed to lock ${MY_WORKLIST}, already exists\n"
    continue
  else
    printf "${PBS_JOBID}\n" >> ${MY_LOCKFILE}
  fi
  if [ ! $( wc -l < ${MY_LOCKFILE} ) -eq 1 ]; then
    printf "Node ${PBS_JOBID} failed to lock ${MY_WORKLIST}, wc failed\n"
    continue
  fi
  # -- got lock, setup working directory, if not already there
  MY_DIR=${MY_BENCHMARK}/${TEST}/${PBS_JOBID}
  MY_CONFIGS=${MY_DIR}/${NODE_INPUT}
  MY_OUTPUT=${MY_DIR}/${NODE_OUTPUT}
  if [ ! -d ${MY_DIR} ]; then
    mkdir ${MY_DIR}
    cp -r ${MY_BENCHMARK}/${BOTH}/* ${MY_DIR}
  fi
  # -- read a few lines from the list
  head -n ${CHUNK} ${MY_WORKLIST} > ${MY_CONFIGS}
  sed -i${BAK} "1,${CHUNK}d" ${MY_WORKLIST}
  # -- unlock
  rm ${MY_LOCKFILE} ${MY_WORKLIST}${BAK}
  # -- ok time to run
  while read CONFIG; do
    ## -- copy files in
    COPY_FROM_DIRS=(${MY_BENCHMARK}/${BENCHMARK}/*/)
    FILE_INDEX=0
    IFS='-' read -ra FILE_IDS <<< ${CONFIG}
    for FILE_ID in ${FILE_IDS[@]}; do
      CUR_DIR=${COPY_FROM_DIRS[${FILE_INDEX}]}
      cp ${CUR_DIR}/${FILE_ID}.py ${MY_DIR}/$( basename ${CUR_DIR} ).py
      FILE_INDEX=$(( ${FILE_INDEX} + 1 ))
    done
    ## -- run the config
    printf "${CONFIG}    0    ["             >> ${MY_OUTPUT}
    for i in $( seq 1 ${ITERS} ); do
      printf $( ${RETIC} ${MY_DIR}/${MAIN} ) >> ${MY_OUTPUT}
      printf ", "                            >> ${MY_OUTPUT}
    done
    printf "]\n"                             >> ${MY_OUTPUT}
  done < ${MY_CONFIGS}
done

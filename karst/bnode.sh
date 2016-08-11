
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
RP="/N/u/${USER}/Karst/retic_performance"
RETIC="/N/u/${USER}/Karst/reticulated/retic.py"

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

CHUNK=10
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
## main

while [ 1 ]; do # (remaining_time() > 1): #hours
  # -- pick random benchmark with work left to do
  MY_BENCHMARK=""
  NUM_BENCHMARKS_LEFT=0
  for BM in ${RP}/*/; do
    if [ -e ${BM}/${KARST_INPUT}*[0-9] ]; then
      NUM_BENCHMARKS_LEFT=$(( NUM_BENCHMARKS_LEFT + 1 ))
    fi
  done
  BENCHMARK_ID=$(( ( RANDOM % NUM_BENCHMARKS_LEFT ) + 1 ))
  for BM in ${RP}/*/; do
    if [ -e ${BM}/${KARST_INPUT}*[0-9] ]; then
      BENCHMARK_ID=$(( BENCHMARK_ID - 1 ))
      if [ ${BENCHMARK_ID} -eq 0 ]; then
        MY_BENCHMARK=${BM}
        break
      fi
    fi
  done
  if [ ! -d ${MY_BENCHMARK} ]; then
    # Couldn't find anything to do
    printf "All jobs finished, ${PBS_JOBID} says goodbye\n"
    break
  fi
  # -- pick random non-empty worklist for the benchmark
  MY_WORKLIST=""
  NUM_WORKLISTS_LEFT=0
  for WL in ${MY_BENCHMARK}/${KARST_INPUT}*[0-9]; do
    if [ -s ${WL} ]; then
      NUM_WORKLISTS_LEFT=$(( NUM_WORKLISTS_LEFT + 1 ))
    fi
  done
  WORKLIST_ID=$(( ( RANDOM % NUM_WORKLISTS_LEFT) + 1 ))
  for WL in ${MY_BENCHMARK}/${KARST_INPUT}*[0-9]; do
    if [ -s ${WL} ]; then
      WORKLIST_ID=$(( WORKLIST_ID - 1 ))
      if [ ${WORKLIST_ID} -eq 0 ]; then
        MY_WORKLIST=${WL}
        break
      fi
    fi
  done
  if [ ! ${MY_WORKLIST} ]; then
    # Delete the empty worklist files
    rm ${MY_BENCHMARK}/${KARST_INPUT}*
    continue
  fi
  # -- setup working directory, if not already there
  MY_DIR=${MY_BENCHMARK}/${TEST}/${PBS_JOBID}
  MY_CONFIGS=${MY_DIR}/${NODE_INPUT}
  MY_OUTPUT=${MY_DIR}/${NODE_OUTPUT}
  if [ ! -d ${MY_DIR} ]; then
    mkdir ${MY_DIR}
    cp -r ${MY_BENCHMARK}/${BOTH}/* ${MY_DIR}
  fi
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
  # -- got lock, read a few lines from the list
  head -n ${CHUNK} ${MY_WORKLIST} > ${MY_CONFIGS}
  sed -i${BAK} "1,${CHUNK}d" ${MY_WORKLIST}
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

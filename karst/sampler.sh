BENCHMARK_NAME="Espionage"
SAMPLE_NUMBER="0"
#### DO NOT MOVE THE ABOVE 2 LINES!

# Collect 1 random sample for a configuration
#
# A configuration is ready for samping if:
# - it contains a `sample/` directory
# - the `sample/` directory contains files named `samples.txtI`
#   where `I` in `[0-9]`
#
# Nodes running this script will run the configurations in one `samples.txt`
#  and save output to the `sample/` directory

# THATS THE IDEA AT LEAST

## -----------------------------------------------------------------------------
## constants

USER="zmahmoud"
USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"

BOTH="both"
SAMPLE="sample"
BENCHMARK="Benchmark"
TEST="Test"
MAIN="main.py"

ITERS=40
# Number of iterations to run for each configuration

KARST_INPUT="samples.txt"
# List of configurations that need to be run. Each benchmark has one of these.

KARST_OUTPUT="sample_output.txt"
# This script collects results for each benchmark in a `KARST_OUTPUT` file

NODE_INPUT="node_input.txt"
NODE_OUTPUT="node_output.txt"
# Local list of TODO/DONE, so we can clean up after killed nodes

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

# NOTE: breaks immediately after doing 1 sample
while [ 1 ]; do
  # -- pick random benchmark with work left to do
  #ALL_BENCHMARKS=()
  #for BM in ${RP}/*/; do
  #  # Valid benchmarks have at least one output folder
  #  #   http://stackoverflow.com/a/4264351/5237018
  #  if [ $( find ${BM}/${SAMPLE} -maxdepth 1 -name "${KARST_INPUT}*[0-9]" -print -quit ) ]; then
  #    ALL_BENCHMARKS+=(${BM})
  #  fi
  #done
  #NUM_BENCHMARKS=${#ALL_BENCHMARKS[@]}
  #if [ ${NUM_BENCHMARKS} -eq 0 ]; then
  #  # Couldn't find anything to do
  #  printf "All jobs finished, ${PBS_JOBID} says goodbye\n"
  #  break
  #fi
  #MY_BENCHMARK=${ALL_BENCHMARKS[${RANDOM} % ${NUM_BENCHMARKS} ]}
  MY_BENCHMARK="${RP}/${BENCHMARK_NAME}";
  # -- pick random non-empty worklist for the benchmark
  #ALL_WORKLISTS=()
  #for WL in ${MY_BENCHMARK}/${SAMPLE}/${KARST_INPUT}*[0-9]; do
  #  if [ -s ${WL} ]; then
  #    ALL_WORKLISTS+=(${WL})
  #  else
  #    # empty worklist
  #    printf "Empty worklist ${WL}\n"
  #    rm ${WL}
  #  fi
  #done
  #NUM_WORKLISTS_LEFT=${#ALL_WORKLISTS[@]}
  #if [ ${NUM_WORKLISTS_LEFT} -eq 0 ]; then
  #  printf "No worklists in directory ${BM}, retrying\n"
  #  break
  #fi
  #MY_WORKLIST=${ALL_WORKLISTS[${RANDOM} % ${NUM_WORKLISTS_LEFT} ]}
  MY_WORKLIST="${MY_BENCHMARK}/${SAMPLE}/samples.txt${SAMPLE_NUMBER}"
  # -- setup working directory, if not already there
  MY_DIR=${MY_BENCHMARK}/${SAMPLE}/${PBS_JOBID}
  MY_CONFIGS=${MY_DIR}/${NODE_INPUT}
  MY_OUTPUT=${MY_DIR}/${NODE_OUTPUT}
  if [ ! -d ${MY_DIR} ]; then
    mkdir ${MY_DIR}
    cp -r ${MY_BENCHMARK}/${BOTH}/* ${MY_DIR}
  fi
  cp ${MY_WORKLIST} ${MY_CONFIGS}
  cd ${MY_DIR}; # ~!!!!!!!!!!!!~
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
      printf $( ${RETIC} ./${MAIN} ) >> ${MY_OUTPUT}
      printf ", "                            >> ${MY_OUTPUT}
    done
    printf "]\n"                             >> ${MY_OUTPUT}
  done < ${MY_CONFIGS}
  break
done

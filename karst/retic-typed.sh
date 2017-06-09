# Goal:
# Run just the typed configuration for a benchmark
#
# Need to make `typed.tar.gz` in Zeina's home directory

USER="zmahmoud"
USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"

ITERS=40
# Number of iterations to run for each configuration

TAR_SUFFIX="tar.gz"
PYTHON_VERSION="Python-3.4.3"
PYTHON_TAR="${USER_HOME}/${PYTHON_VERSION}.${TAR_SUFFIX}"
TYPED_TAR="${USER_HOME}/typed.${TAR_SUFFIX}"
RETICULATED="reticulated"
RETIC_TAR="${USER_HOME}/${RETICULATED}.${TAR_SUFFIX}"

MY_TMP="/tmp/${PBS_JOBID}"
MY_OUTPUT="${PBS_JOBID}.txt"

mkdir ${MY_TMP}
tar -xzf ${PYTHON_TAR} -C ${MY_TMP}
tar -xzf ${RETIC_TAR} -C ${MY_TMP}

PYTHON_EXEC="${MY_TMP}/${PYTHON_VERSION}/python"
RETIC="${MY_TMP}/${RETICULATED}/retic.py"

# change shebang line to use ${PYTHON_EXEC}
sed -i${BAK} "s,#!.*,#!${PYTHON_EXEC}," ${RETIC}

## -----------------------------------------------------------------------------
## main

for BM in "${USER_HOME}/typed/*/"; do
  echo ${BM};
  cd ${BM};
  for i in $( seq 1 ${ITERS} ); do
    printf $( ${RETIC} main.py ) >> ${MY_OUTPUT};
    printf " "                            >> ${MY_OUTPUT};
  done
done

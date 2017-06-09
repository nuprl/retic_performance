# Goal:
# Run just the untyped configuration for a benchmark

USER="zmahmoud"
USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"

ITERS=40
# Number of iterations to run for each configuration

TAR_SUFFIX="tar.gz"
PYTHON_VERSION="Python-3.4.3"
PYTHON_TAR="${USER_HOME}/${PYTHON_VERSION}.${TAR_SUFFIX}"
UNTYPED_TAR="${USER_HOME}/untyped.${TAR_SUFFIX}"
RETICULATED="reticulated"
RETIC_TAR="${USER_HOME}/${RETICULATED}.${TAR_SUFFIX}"

MY_TMP="${USER_HOME}/${PBS_JOBID}"
MY_OUTPUT="${PBS_JOBID}.txt"

mkdir ${MY_TMP}
tar -xzf ${PYTHON_TAR} -C ${MY_TMP}
tar -xzf ${UNTYPED_TAR} -C ${MY_TMP}
tar -xzf ${RETIC_TAR} -C ${MY_TMP}

PYTHON_EXEC="${MY_TMP}/${PYTHON_VERSION}/python"
RETIC="${MY_TMP}/${RETICULATED}/retic.py"

# change shebang line to use ${PYTHON_EXEC}
sed -i${BAK} "s,#!.*,#!${PYTHON_EXEC}," ${RETIC}

## -----------------------------------------------------------------------------
## main

for BM in "${USER_HOME}/untyped/*/"; do
  echo ${BM};
  cd ${BM};
  for i in $( seq 1 ${ITERS} ); do
    printf $( ${RETIC} main.py ) >> ${MY_OUTPUT};
    printf " "                            >> ${MY_OUTPUT};
  done
  cd -;
done

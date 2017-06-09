USER="zmahmoud"
USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"

ITERS=40
# Number of iterations to run for each configuration

TAR_SUFFIX="tar.gz"
PYTHON_VERSION="Python-3.4.3"
PYTHON_TAR="${USER_HOME}/${PYTHON_VERSION}.${TAR_SUFFIX}"
UNTYPED_TAR="${USER_HOME}/untyped.${TAR_SUFFIX}"

MY_TMP="/tmp/${PBS_JOBID}"

mkdir ${MY_TMP}
tar -xzf ${PYTHON_TAR} -C ${MY_TMP}
tar -xzf ${UNTYPED_TAR} -C ${MY_TMP}

PYTHON_EXEC="${MY_TMP}/${PYTHON_VERSION}/python"

## -----------------------------------------------------------------------------
## main

for BM in "${MY_TMP}/untyped/*/"; do
  echo ${BM};
  cd ${BM};
  for i in $( seq 1 ${ITERS} ); do
    ${PYTHON_EXEC} main.py;
  done
  cd -;
done

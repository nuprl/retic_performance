# usage: ./bsample-run.sh
# MUST BE CALLED FROM THIS DIRECTORY
#
# - finds all benchmarks' `sample/` folders
# - finds all un-run samples in each folder
# - makes a copy of `sampler.sh` tailored to each
# - runs all the samplers
#

## -----------------------------------------------------------------------------
## --- edit these parameters

USER="zmahmoud"
SAMPLE="sample"
BMGLOB="*"
WALLTIME="11:00:00"

## -----------------------------------------------------------------------------

USER_HOME="/N/u/${USER}/Karst"
RP="${USER_HOME}/retic_performance"
QSUB="qsub -k o -l nodes=1:ppn=16,walltime=${WALLTIME} "
for MY_SAMPLE_DIR in ${RP}/${BMGLOB}/${SAMPLE}/; do
  BM=$( basename $( dirname ${MY_SAMPLE_DIR} ) );
  for TXT in ${MY_SAMPLE_DIR}/samples.txt*; do
    NUM=${TXT: -1}
    MY_SCRIPT="${BM}-sampler-${NUM}.sh"
    echo "BENCHMARK_NAME=${BM}" >> ${MY_SCRIPT}
    echo "SAMPLE_NUMBER=${NUM}" >> ${MY_SCRIPT}
    tail -n +3 sampler.sh >> ${MY_SCRIPT}
    ${QSUB} ${MY_SCRIPT}
    #echo "made script for ${BM} no ${NUM}";
  done;
done;

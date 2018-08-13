#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm7_m160.root -o ${SIM_DIR}/dm7.root 
error = ${SIM_DIR}/dm7.err
output = ${SIM_DIR}/dm7.output
notification = Never
priority = 0
Queue
EOM

echo "$CMD" | condor_submit &

read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM/pMSSM_MCMC1_38_870285_dm13_chi1pmchi20.root -o ${SIM_DIR}/dm13.root
error = ${SIM_DIR}/dm13.err
output = ${SIM_DIR}/dm13.output
notification = Never
priority = 0
Queue
EOM

echo "$CMD" | condor_submit &
  

read -r -d '' CMD << EOM
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
arguments = ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/TChiZW/OfficialScan/TChiWZ_mNlsp150mLsp130.root -o ${SIM_DIR}/dm20.root
error = ${SIM_DIR}/dm20.err
output = ${SIM_DIR}/dm20.output
notification = Never
priority = 0
Queue
EOM

echo "$CMD" | condor_submit &



#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob

qsub -cwd -l h_vmem=2G -o /tmp/dm7.output -e /tmp/dm7.err ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM_MCMC1_38_870285_dm7_m160.root -o ${SIM_DIR}/dm7.root

qsub -cwd -l h_vmem=2G -o /tmp/dm13.output -e /tmp/dm13.err ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM_MCMC1_38_870285_dm13_chi1pmchi20.root -o ${SIM_DIR}/dm13.root

qsub -cwd -l h_vmem=2G -o /tmp/dm20.output -e /tmp/dm20.err ./run_sim_analysis_single.sh -i /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/pMSSM_MCMC1_38_870285_dm20_chi1pmchi20_m160.root -o ${SIM_DIR}/dm20.root

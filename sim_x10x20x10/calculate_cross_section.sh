#!/bin/bash

. "/afs/desy.de/user/n/nissanuv/cms-tools/bg/def.sh"

shopt -s nullglob 

#check output directory
if [ ! -d "$CS_SIG_OUTPUT_DIR" ]; then
  mkdir $CS_SIG_OUTPUT_DIR
fi

if [ ! -d "$CS_SIG_OUTPUT_DIR/def" ]; then
  mkdir "$CS_SIG_OUTPUT_DIR/def"
fi

if [ ! -d "$CS_SIG_OUTPUT_DIR/params" ]; then
  mkdir "$CS_SIG_OUTPUT_DIR/params"
fi

if [ ! -d "$CS_SIG_OUTPUT_DIR/stdout" ]; then
  mkdir "$CS_SIG_OUTPUT_DIR/stdout"
fi

if [ ! -d "$CS_SIG_OUTPUT_DIR/stderr" ]; then
  mkdir "$CS_SIG_OUTPUT_DIR/stderr"
fi

module load root6

timestamp=$(date +%Y%m%d_%H%M%S%N)
output_file="${WORK_DIR}/condor_submut.${timestamp}"
echo "output file: $output_file"

cat << EOM > $output_file
universe = vanilla
should_transfer_files = IF_NEEDED
executable = /bin/bash
notification = Never
priority = 0
EOM

for f in /nfs/dust/cms/user/beinsam/CommonNtuples/MC_BSM/CompressedHiggsino/M1M2Scan/slha/*; do
	filename=$(basename $f .slha)
	for p in "" "-"; do
		cat << EOP  > "$CS_SIG_OUTPUT_DIR/def/${filename}$p"
collider_type = proton-proton
center_of_mass_energy = 13000
particle1 = 1000023
particle2 = ${p}1000024
slha = $f
result = total
pdf_lo = MSTW2008lo90cl
pdfset_lo = 0
pdf_nlo = MSTW2008nlo90cl
pdfset_nlo = 0
mu_f = 0.5
mu_r = 0.5
precision = 0.001
max_iters = 3
EOP
	done
done

for f in $CS_SIG_OUTPUT_DIR/def/*; do
	filename=$(basename $f)
	echo "Will run:"
	echo $CS_SINGLE "$CS_SIG_OUTPUT_DIR/params/$filename" "$f"
cat << EOM >> $output_file
arguments = $CS_SINGLE $CS_SIG_OUTPUT_DIR/params/$filename $f
error = ${CS_SIG_OUTPUT_DIR}/stderr/${filename}.err
output = ${CS_SIG_OUTPUT_DIR}/stdout/${filename}.output
Queue
EOM
done

condor_submit $output_file
rm $output_file
        

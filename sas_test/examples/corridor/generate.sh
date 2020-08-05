#!/usr/bin/bash
## This script executes two tasks:
# (i) generates corridor pddl files from 1 till n using problem_generator;
# (ii) generates SAS for these PDDL using FastDownward PDDL to SAS translator

n="$1"
translator="../../../src/translate/translate.py"
time_limit=100

# check command line argument for size
if [ -z "$n" ];  then
  echo "Please pass the size"
  exit 0
fi

echo "Generating PDDL and corresponding SAS files for 1 till $n"
for (( i=1; i<=n; i++ ))
do
  python ./problem_generator.py "$i"
done

echo "Moving PDDL files to output folder"
mv generalized_problem_*.pddl ./output/pddl
mv generalized_domain_*.pddl ./output/pddl


echo "Generating SAS for the PDDL files"
for (( i=1; i<=n; i++ ))
do
  python $translator "$time_limit" "./output/pddl/generalized_domain_$i.pddl" "./output/pddl/generalized_problem_$i.pddl" "./output/sas/generalized_sas_$i.sas"
done

echo "Printing the number of conditional effects in move-right"
printf "%s\t%s\n" "n" "conditional-effects"
for (( i=1; i<=n; i++ ))
do
  num=$(sed -n '/move-right/,/end_operator/p' "./output/sas/generalized_sas_$i.sas" | sed -n '3p')
  printf "%s\t%s\n" $i $num
done
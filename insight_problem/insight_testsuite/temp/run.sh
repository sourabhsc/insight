#!/bin/bash

proj_path=$PWD
echo "=========================================================="
echo "1) Please enter the name of input file without directory name."
echo "==========================================================="
echo "...a) File is expected to be in $PWD/input/ directory"
echo "...b) File is expectd to be in csv format [ENTER]:"
read user_input
input_file=$proj_path/input/$user_input
echo "Your input file is :" $input_file



echo "=============================================================="
echo "2) Based on information from file structure file enter the following information. "
echo "============================================================"

echo "...a) SOC_NAME key word [ENTER]"
read soc
echo "...b) WORKSITE_STATE keyword [ENTER]"
read work
echo "...c) CASE_STATUS keyword [ENTER]"
read case_status

python $PWD/src/h1b_counting_v2.py $input_file $soc $work $case_status
echo "=============================================================="
echo "3) Output is stored in :" $PWD/output/
echo "=============================================================="





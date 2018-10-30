README.md contains Problem, Approach and Run instructions sections

# This file evaluates and sorts the H1B applications for diffeent years


## Problem 
Create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

## Approach 
	* First of all user is asked to enter the name of input file that is stored in csv format in the designated folder
	* Next user is asked to enter the keyword infromation that can be obtained using File structure docs on the website.
		* keyword informaitons asked ---
			* SOC keyword ... e.g. SOC_NAME
			* WORKSITE_STATE keyword e.g. WORKSITE_STATE
			* CASE_STATUS keyword ... e.g. CASE_STATUS
		* e.g. #### For year 2014 keys are defined by ,  'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE', 'STATUS' respetively
	* Once the above information is provided, we read the input file for all the columns ( *I can improve upon this by readin only the columns necessary instead of reading all the columns* )
	* After reading the file we call the function sorting to count the number of certified applicants for each occupations and and then sort them according to the rule specified in instructions.
	* We save the results in the file '/output/top10_occupations.txt' .
	* Same process is repeated to find the results for top 10 states.

## Run instructions
here are
'''
 just run using ./run.sh 


'''






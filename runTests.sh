#!/bin/bash
shopt -s nullglob
for script in test*.txt
do
	echo $script 
	gtimeout 4s ./silly < $script > output.txt	
	if [[ $? = 124 ]]; then
		echo "Timeout"
	else 
		time ./silly < $script > output.txt
		if [[ $? = 0 ]]; then
			echo "Passed"
		elif [[ $? = 1 ]]; then
			echo "Failed"
		fi
	fi
done


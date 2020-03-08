#!/bin/bash
while true
do
	python3 r6proc.py
	echo "Sleeping for 10 minutes before requesting new data."
	sleep 600 # 10 minutes
done

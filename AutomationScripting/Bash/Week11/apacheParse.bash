#!/bin/bash
# Parse log

# 101.236.44.127 - - [24/Oct/2017:04:11:14 -0500] "GET / HTTP/1.1" 200 225 "-" 
# "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/27.0.1453.94 Safari/537.36"


#Read in file
#Arguments using the position, they start at $1
APACHE_LOG="$1"

#check if file exists
if [[ ! -f ${APACHE_LOG} ]]
then

	echo "Please specify the path to a log file."
	exit 1

fi

# Use sed to remove the extraneous characters [ and "
sed -e "s/\[//g" -e "s/\"//g" ${APACHE_LOG}

# Then search for known bad stuff in our log file


# Then use awk to create a header for columns


# Then create a purdy report.

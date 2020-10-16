#!/bin/bash
# Parse an apache web Log


# Read in the file from the commandline
# Arguments using the position. Arguments start at $1.
APACHE_LOG="$1"

# check if the logfile exists
if [[ ! -f ${APACHE_LOG} ]]
then

    echo "Please specify the path to a log file."
    exit 1
fi

# Parse iptables Log
sed -e "s/\[//g" -e "s/\"//g" ${APACHE_LOG} | \
awk ' BEGIN { format = "%-16s %-25s %-8s %-8s %-9s %-50s %-50s \n"
printf format, "IP", "Date", "Method", "Status", "Size", "URI", "UA"
printf format, "---------------", "---------------", "-------", "-------", "-----", "------", "------"}

{

	if ($12 == "-") {	

		# print the results
		printf format, $1, $4, $6, $9, $10, $7, "No User Agent"
	
	} else {

		# Start at field $12
		start = 12

		# Initialize an empty variable which is a placeholder for $12 (called msg)
		# Start at field $12 using the "start" variable
		# Count the number of fields left in the line
		msg = ""; for (i = start; i <= NF; i++)

		# Start the user agent formatting
		# Print from field $12 until the end of the line
		msg = msg " " $i;

		# print the results with the user agent
		printf format, $1, $4, $6, $9, $10, $7, msg

	}

}'

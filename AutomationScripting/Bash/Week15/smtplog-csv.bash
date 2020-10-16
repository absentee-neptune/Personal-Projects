#!/bin/bash

# Check to see if the file smtp.log exists. We've used -f several times to determine if a file exists.
# NOTE: Remember that the gzip -d will remove .gz extension from the filename so the file you work with
# will be named: smtp.log

FILE="$1"

if [[ -f "${FILE}" ]] ;
then

	# If the file exists, ask the user if they want to delete the file or keep it.
	echo "[D]elete file or [K]eep file"
	read option

	case ${option} in

		[Dd]) # If delete, then delete the file
			rm -f smtp.log

			#Download the file
			wget https://www.secrepo.com/maccdc2012/smtp.log.gz
			gzip -d smtp.log.gz

		;;

		[Kk]) # otherwise, if they want to keep the existing file, then let the user know.
			echo "Okay, keeping the existing file"
			sleep 2

	esac

elif [[ ! -f "${FILE}" ]] ;
then

	# If the file doesn't exist, then download it.
	wget https://www.secrepo.com/maccdc2012/smtp.log.gz
	gzip -d smtp.log.gz

fi


# Use awk to create a header
awk ' BEGIN { FORMAT = "%-15s %-15s %s\n"
printf FORMAT, "SRC IP,", "DST IP,", "Message"}

{

	q = "\""
	cq = "\","

	# print the results
	printf FORMAT, q$3cq, q$5cq, q$21cq

}'

#!/bin/bash
# Script to view Apache logs via a GUI and generate a block list for bad IPs.

function view_logs() {

# Present the apache access log screen

# Count the number of rules.
num_rules=$(echo ${block_ip} | awk -F"|" ' { print NF } ')


# If no rules are selected, the value of ${num_rules} will be 0.
if [[ ${num_rules} -eq 0 ]]
then

	# Prompt for finding no IPs selected

		# Get the value of the exit status, we set above with the buttons
		no_ip=$?
	
		# Allow the user to see the logs again
		if [[ ${no_ip} -eq 10 ]]
		then

			view_logs

		else

			# Or exit if they select No.
			exit 0

		fi

else 

	# Get the IP address (field $2) from the yad output and format the results into an IPTables drop rule

	# File save dialog will 

	# Save the IPs to the file specified.
	echo "${the_rules}" |& tee ${save_ip}

	# Prompt to view the logs again.
	yad --text="Would you like to view the logs again?" \
		--button="Yes":10 \
		--button="No":20

		# Get the value of the buttons (:10 or :20) from the bash environment
		allDone=$?

		
		# Process the buttons.
		if [[ ${allDone} -eq 10 ]]
		then

			view_logs

		else

			exit 0

		fi


fi

} # end view_logs function
# Display the main menu
view_logs

#!/bin/bash
# Week 9 Assignment - Security Checks
# Create a script that performs local security checks.


function checks() {

	# Check if set to one year
	if [[ $3 != $2 ]]
	then

		# print if it is not compliant
		echo -e "\e[1;31m$1 is not compliant. It should be: $2"
		echo -e "The current value is: $3\e[0m"
		echo ""

	else

		# print if it is compliant
		echo -e "\e[1;32m$1 is compliant. The current value is: $3\e[0m"
		echo ""
	fi

} # closing checks function

# Get password policies
pass_check=$(egrep -i "^pass" /etc/login.defs)

# Get PASS_MAX_DAYS policy
pmax=$(echo "${pass_check}" | egrep -i "pass_max_days" | awk ' { print $2 } ')

# Get PASS_MIN_DAYS policy
pmin=$(echo "${pass_check}" | egrep -i "pass_min_days" | awk ' { print $2 } ')

# Get PASS_WARN_AGE policy
pwarn=$(echo "${pass_check}" | egrep -i "pass_warn_age" | awk ' { print $2 } ')

# Call our checks function
# 	     $1	       $2      $3
checks "PASSWORD MAX" "365" "${pmax}"
checks "PASSWORD MINIMUM" "14" "${pmin}"
checks "PASSWORD WARN AGE" "7" "${pwarn}"


# SSH Protocol check
chkSSHProto=$(egrep "^Protocol" /etc/ssh/sshd_config | awk ' { print $2 } ')
checks "The SSH Protocol" "2" "${chkSSHProto}"

# UsePAM setting check
chkUsePAM=$(egrep "^UsePAM" /etc/ssh/sshd_config | awk ' { print $2 } ')
checks "The UsePAM setting" "no" "${chkUsePAM}"

# PermitRootLogin setting check
chkPermitRootLogin=$(egrep "^PermitRootLogin" /etc/ssh/sshd_config | awk ' { print $2 } ')
checks "The PermitRootLogin setting" "prohibit-password" "${chkPermitRootLogin}"

# sftp_subsystem setting check
chkSFTP=$(egrep "^Subsystem" /etc/ssh/sshd_config | awk ' { print $3 } ')
checks "The SFTP Subsystem setting" "/usr/lib/openssh/sftp-server" "${chkSFTP}"


# Check direcotry Permissions
for eachDir in $(ls -l /home/ | grep '^d' | awk ' { print $3 } ')
do

	# Check if the user is sys320
	if [[ ${eachDir} == "sys320" ]]
	then
	
		# Don't check the directory
		continue
	
	fi

	getDirPerms=$(ls -l /home/${eachDir} | awk ' { print $1 } ')
	checks "The home directory for ${eachDir}" "drwx------" "${getDirPerms}"

done

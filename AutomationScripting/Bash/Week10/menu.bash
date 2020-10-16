#!/bin/bash
# Admin and Security admin menu.


# Incident Response Collection submenu function
function IRC_menu() {

	# Clear the screen
	clear

	# Create menu options
	echo "| Incident Response Collection |"
	echo ""
	echo "1. Show all root users"
	echo "2. Open ssh_config file"
	echo "3. Check command history"
	echo "4. Check attached devices"
	echo "5. Check mounted devices"
	echo "6. Show all USB buses and devices"
	echo "7. Show CPU information"
	echo "8. Show all PCI busses and devices"
	echo "9. Check netowrk connections"
	echo "10. Network Statistics command"
	echo ""
	echo "[R]eturn to Security Admistration Menu"
	echo "[E]xit"

	# Prompt for the menu option
        echo ""
        echo -n "Please enter an option: "

        # Read in the user input
        read option

	# Case statement to process options
	case ${option} in

		1) cat /etc/sudoers | less

		# command that shows users that have root access
		# this is a good command as it can reveal compromised 
		#security through users that aren't supposed to be sudoers

		;;

		2) cat /root/etc/ssh/ssh_config | less

		# command that opens ssh_config file
		# this is a good command as it lets the admin 
		#search for any changed security settings that 
		#would allow for unauthorized access

		;;

		3) history

		# allows access to command history
		# this is good as if you want to check 
		#the command history of a certain user 
		#and see if there were any suspicious activity 
		#within their account

		;;

		4) locate rhosts

		# defines which remote hosts can invoke 
		#certain commands on the local host 
		#without supplying a password
		# This is a good command as the admin can determine 
		#if there are any security compromises with romote host access

		;;

		5) lsblk | less

		# lists attached devices
		# this is a good command as it gives the admin 
		#an overview what what is mounted to the system 
		#that is being evaluated

		;;

		6) lsusb | less

                # prints all USB buses and devices
                # This is a good command as you can determine if there is 
                #an unauthorized device connected to the system 
                #preventing any system and security issues

		;;

		7) lscpu | less

                # prints CPU information
                # This is a good command as the admin can easily view a 
                #systems cpu information and look for any issues

		;;

		8) lspci | less

                # prints all PCI buses and devices
                # This is a good command as the admin can easily view a 
                #systems PCI information and look for any issues and see
                #if there are any unauthorized device connected to the system 
                #preventing any system and security issues

		;;

		9) ipconfig -a

		# check the system's network connections
		# this is a good command as if the incident involved 
		#the system network the admin can check the 
		#network connections for any security compromises

		;;

		10) netstat -anop | less

		# network utility that displays network connections for 
		#TCP, routing tables, and a number of network interface 
		#and network protocol statistics
		# This is a good command as it can check for 
		#suspicious connections and if the system is listening 
		#for unauthorized connections as well

		;;

		[Rr]) security_menu

		;;

		[Ee]) exit 0

                ;;

                *) echo "| Invalid input |"
                        sleep 3
                        IRC_menu

                ;;

	# Stops the case statement
	esac

# Call IRC_menu
IRC_menu

} # end IRC_menu function


# Admin Menu function
function admin_menu() {

	# Clear the screen
	clear

	# Create menu options
	echo "| System Administration Menu |"
	echo ""
	echo "1. List Running Processes"
        echo "2. Show Open Network Sockets"
        echo "3. Check Logged in Users"
	echo "4. Show current username and groups"
	echo "5. Show last users logged on"
	echo "6. Show all USB buses and devices"
	echo "7. Show CPU information"
	echo "8. Show all PCI buses and devices"
	echo ""
	echo "[R]eturn to Main Menu"
        echo "[E]xit"

	# Prompt for the menu option
	echo ""
	echo -n "Please enter an option: "

	# Read in the user input
	read option

	# Case statement to process options
	case ${option} in

                1) ps -ef | less

                ;;

                2) netstat -an --inet | less
                        # lsof -i -n | less

		;;

		3) w | less

		;;

		4) id | less

		# Print real and effective user id (uid) and group id (gid), 
		#prints identity information about the given user
		# This is a good command as is gives current identity information about the user 
		#to make sure they are in the right account and such

		;;

		5) last -a | less

		# Prints the last users who logged on
		# This is a good command as if an issue with the system arose 
		#the administrator can check who was last logged on and 
		#investigate their actions

		;;

		6) lsusb | less

		# prints all USB buses and devices
		# This is a good command as you can determine if there is 
		#an unauthorized device connected to the system 
		#preventing any system and security issues 

		;;

		7) lscpu | less

		# prints CPU information
		# This is a good command as the admin can easily view a 
		#systems cpu information and look for any issues

		;;

		8) lspci | less

		# prints all PCI buses and devices
		# This is a good command as the admin can easily view a 
                #systems PCI information and look for any issues and see
		#if there are any unauthorized device connected to the system 
                #preventing any system and security issues

		;;

		[Rr]) main_menu

		;;

                [Ee]) exit 0

                ;;

                *) echo "| Invalid input |"
                        sleep 3
                        admin_menu

                ;;

	# Stops the case statement
        esac

# Call admin_menu
admin_menu

} # End admin_menu function


#Security Menu
function security_menu() {
	
	# Clear the screen
	clear

	# Create menu options
	echo "| Security Administration Menu |"
	echo ""
	echo "1. Show last logged in users"
	echo "2. Check installed packages"
	echo "3. Check all users and their ID"
	echo ""
	echo "[R]eturn to Main Menu"
	echo "[I]ncident Response Collection"
	echo "[E]xit"

	# Prompt for the menu option
        echo ""
	echo -n "Please enter an option: "

        # Read in the user input
        read option

	# Case statement to process options
	case ${option} in
	
		1) last -adx | less

		;;

		2) dpkg -l | less

		;;

		3) cut -d: -f1,3 /etc/passwd

		;;

		[Rr]) main_menu

		;;

                [Ii]) IRC_menu

		;;

		[Ee]) exit 0

		;;

		*) echo "| Invalid input |"
                        sleep 3
                        admin_menu

                ;;

	# Stops the case statement
	esac

# Call security menu
security_menu

} # End security_menu function


# Main Menu
function main_menu() {

	# Clear the screen
	 clear

	# Create menu options
	echo "| Administration |"
	echo ""
	echo "1. System Admin Menu"
        echo "2. Security Admin Menu"
	echo ""
        echo "[E]xit"

	# Prompt for the menu option and read in the option
	echo ""
	echo -n "Please select a menu: "
	read menuOption

	if [[ ${menuOption} -eq 1 ]]
        then

		# Call the admin_menu function
                admin_menu

        elif [[ ${menuOption} -eq 2 ]]
        then
		
		# Call the security_menu function
                security_menu

        else
		
		# Exit the program
                exit 0

        fi

} # End main_menu function


# Call main_menu function
main_menu

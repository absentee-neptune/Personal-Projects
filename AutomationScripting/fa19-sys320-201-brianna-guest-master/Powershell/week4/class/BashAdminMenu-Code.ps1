# Create menus for sys admin and sec admin task

function mainMenu {

    # Clear the screen
    clear

    # Create our menus
    write-host "1) System Admin Tasks."
    write-host "2. Security Admin Tasks."
    write-host "[E]xit"
    
    # Prompt the user for a selection
    $u_select = read-host -Prompt "Please select one of the options above"

    # Process the user response
    if ($u_select -eq 1) {
    
        # Call the sysadmin function
        sysAdmin
    
    } elseif ($u_select -eq 2 ) {

        # Call the secAdmin function
        secAdmin

    } elseif ($u_select -eq "E") {

        # exit the program
        exit

    } else {
    
        write-host -backgroundcolor Red -foregroundcolor white "Invalid value"
        sleep 3
        mainMenu
    
    }

} # ends the mainMenu function


# This function will provide a prompt to the user to hit Enter when they are done reviewing the results
# and take them back to the menu they were in.
function allDone  {

    read-host -prompt "Press [Enter] when done."

}

# Process sys admin tasks.
function sysAdmin {

    # Clear the screen
    clear

    # Build our menu
    write-host -BackgroundColor Red "System Admin Menu"
    Write-Host "1. List all running processes."
    write-host "2. List all services."
    write-host "3. List only running services."
    write-host "[R]eturn to Main Menu"
    Write-host "[E]xit this program"  

    # Prompt the user
    $sysAdminTask = read-host -Prompt "Please select an option above"
   
    #Process the user's input
    if ($sysAdminTask -eq "R") {
        
        mainMenu

    } elseif ($sysAdminTask -eq "E") {

        exit
    
    } elseif ($sysAdminTask -eq 1) {
    
        ps | out-host

    } elseif ($sysAdminTask -eq 2) {
    
        Get-Service | out-host
        
   
    } elseif ($sysAdminTask -eq 3) {
    

        Get-Service | where { $_.Status -eq "Running" } |out-host
        
   
    } else {
    
        write-host "Invalid option"
        sleep 4

        # Call the system admin menu so the user can start again.
        sysAdmin
    
    } # end if statement

    # Allow the user to review the results
    allDone

    # Call the sysAdmin menu, because they are currently working in this menu.
    sysAdmin

} # end sysAdmin Function


# TASK: Create a "secAdmin" function with the options:
'''
List all Users
List all services, including path
Liast all processes, including path
Return
Exit


'''


# call the mainMenu function
mainMenu
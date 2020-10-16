# Create menus for sys admin and sec admin task

function mainMenu {

    # Clear the screen
    clear

    # Create our menus
    Write-Host "1. System Admin Tasks."
    Write-Host "2. Security Admin Tasks."
    Write-Host "[E]xit"

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
    
        write-host -BackgroundColor Red -ForegroundColor White "Invalid value"
        sleep 5
        mainMenu
    
    }


} # end mainMenu function

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
    Write-Host "1. List All Running Processes."
    Write-Host "2. List All Services."
    Write-Host "3. List Only Running Services."
    Write-Host "[R]eturn to Main Menu."
    Write-Host "[E]xit"
   
    # Prompt the user
    $sysAdminTask = Read-Host -Prompt "Please select one of the options above"
   
    #Process the user's input
    if ($sysAdminTask -eq "R") {

        mainMenu

    } elseif ($sysAdminTask -eq "E") {

        break
    
    
    } elseif ($sysAdminTask -eq 1) {

        Get-Process | Out-Host 
    
    } elseif ($sysAdminTask -eq 2) {

        Get-Service | Out-Host
   
    } elseif ($sysAdminTask -eq 3) {

        Get-Service | where {$_.Status -eq "Running"} | Out-Host
   
    } else {
    
        write-host -BackgroundColor Red -ForegroundColor White "Invalid option!"
        sleep 4

        # Call the system admin menu so the user can start again.
        sysAdmin
    
    } # end if statement

    # Allow the user to review the result.
    allDone

    # Call the sysAdmin menu, because they are currently working in this menu.
    sysAdmin

} # end sysAdmin menu

# call the mainMenu function

mainMenu
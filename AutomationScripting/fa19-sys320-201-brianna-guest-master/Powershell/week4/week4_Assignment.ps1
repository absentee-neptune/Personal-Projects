# Week 4 - Powershell Assignment 1

# Download the CVE file
#Invoke-WebRequest -URI http://192.168.1.32/cve-test.csv -OutFile "C:\Users\bguest\fa19-sys320-201-brianna-guest\week4\cve-test.csv"

# Import the cve file into powershell.
$CVE_File = Import-Csv "C:\Users\bguest\fa19-sys320-201-brianna-guest\week4\cve-test.csv" -header Name,Status,Description

# Main Menu function for the CVE Entry Search
function mainMenu {

    # clear the screen
    clear

    # main menu
    Write-Host "| CVE Entry Search |"
    Write-Host "1. Search by CVE Entry Name."
    Write-Host "2. Search by CVE Entry Description."
    Write-Host "[E]xit"
    Write-Host ""

    # read-host prompts for the user to select an option from the menu
    $userChoice = Read-Host -Prompt "Choose an option"
    
    # Process the user response
    if ($userChoice -eq 1) {
    
        # Call the searchName function
        searchName
    
    } elseif ($userChoice -eq 2 ) {

        # Call the searchDescription function
        searchDescription

    } elseif ($userChoice -eq "E") {

        # exit the program
        exit

    } else { # if another value is entered besides those listed within the if statement`
    
        write-host -BackgroundColor Red -ForegroundColor White "| Invalid Value |"
        sleep 5
        mainMenu
    
    } # end if statement

} # end mainMenu function

# This function will provide a prompt to the user to hit Enter when they are done reviewing the results and take them back to the menu they were in.
function allDone  {
    
    write-host ""
    read-host -prompt "Press [Enter] when done"
    mainMenu

}

# Search by CVE Entry Name function
function searchName {
    
    # read-host prompts for the user to enter a name to search by CVE Entry Name
    $searchName = Read-Host -Prompt "Please enter a CVE Entry Name"

    foreach ($cveEntry in $CVE_File) {
  
        # User prompt that allows the user to specify an arbitrary keyword.
        if ($cveEntry.Name -eq "$searchName") {
    
            # Print that the CVE was found.
            write-host "Found."

            # Print the results for the CVE.
            $entryName = $cveEntry.Name
            $entryDesc = $cveEntry.Description
            $entryStatus = $cveEntry.Status
            Write-Host "CVE NAME: $entryName"
            Write-Host "CVE DESC: $entryDesc"
            Write-Host "CVE STAT: $entryStatus"

            # Set value to false to denote the entry was found.
            $notFound = "false"
        
            # Stops the foreach loop
            # This reduces memory and file read operations and get the results faster.
            break
    
        } else {
        
            # If at least one occurence of the keyword is found, there is a match.
            if ($notFound -eq "false") {
            
                continue

            } else {

                # Set value to "true" if no entry is found.
                $notFound = "true"

            }
    
        } # end check for CVE
    
    } # end foreach loop

    # Print if there was no entry found.
    if ($notFound -eq "true" ) {
        write-host "CVE not found."

    } # end if statement

    # allow the user to review the results then go back to the previous menu
    allDone

} # End searchName function

function searchDescription {

    # read-host prompts for the user to enter a keyword to search by a keyword in the Description
    $searchKeyword = read-host -Prompt "Please enter a keyword"

    foreach ($cveEntry in $CVE_File) {
  
        # User prompt that allows the user to specify an arbitrary keyword.
        if ($cveEntry.Description -ilike "$searchKeyword") {
    
            # Print that the CVE was found.
            write-host "Found."
            # Print the results for the CVE.
            $entryName = $cveEntry.Name
            $entryDesc = $cveEntry.Description
            $entryStatus = $cveEntry.Status
            Write-Host "CVE NAME: $entryName"
            Write-Host "CVE DESC: $entryDesc"
            Write-Host "CVE STAT: $entryStatus"
            # Set value to false to denote the entry was found.
            $notFound = "false"
        
            # Stops the foreach loop
            # This reduces memory and file read operations and you get the results faster.
            break
    
        } else {
        
            # If at least one occurence of the keyword is found, there is a match.
            if ($notFound -eq "false") {
            
                continue
            } else {
                # Set value to "true" if no entry is found.
                $notFound = "true"
            }
    
        } # end check for CVE
    
    } # end foreach loop

    # Print if there was no entry found.
    if ($notFound -eq "true" ) {
        write-host "CVE not found."
    } # end if statement

    # allow the user to review the results then go back to the previous menu
     allDone

} # end searchName function

# call the mainMenu function
mainMenu
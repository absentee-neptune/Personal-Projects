#Brianna Guest
#Powershell Final Project

#Main Menu Function
function mainMenu {
    
    # Clears the screen
    clear 

    # Create Menu
    write-Host "1. System Admin Tasks"
    write-Host "2. Security Admin Tasks"
    write-Host "[E]xit"
    
    $u_select = read-host -prompt "Please select one of the options above"

    if ($u_select -eq 1) {

        # Call the sysAdmin function
        sysAdmin

    } elseif ($u_select -eq 2) {

        # Call the secAdmin
        secAdmin

    } elseif ($u_select -eq "E") {

        # Exit the program
        exit

    } else {

        write-Host -backgroundcolor red -foregroundcolor white "| Invalid Value |"
        sleep 5
        mainMenu

    } # end if statement

} # Ends the mainMenu function



# This function will provide a prompt to the user to hit Enter when they are done reviewing the results
# and take them back to the menu they were in.
function allDone {

    read-Host -prompt "Press [Enter] when done"

}



# Function that lists all running processes and asks the user if they want to save the output to a file
function task1 {

    $csv = read-host -prompt "Would you like to save results to a CSV file? (Y/N)"

        # If the user wishes to save the results as a CSV file
        if ($csv -eq "Y"){

            $path = read-host -prompt "Enter file path to save (ex. C:\users\bguest\desktop)"
            $name = read-host -prompt "Enter file name (ex. processes.csv)"
            $process = read-host -prompt "Would you like to search for a specific process? (Y/N)"
            
            # If the user wishes to search for a specific process
            if ($process -eq "Y"){
                
                $whichProcess = read-host -prompt "Name the Process"
                $there = Test-Path $path\$name

                if ($there -eq "True") {

                    Get-Process $whichProcess | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"

                } else {

                    Write-Host "| Error of Saving File to $path\$name |"

                } # end if statement, start of elseif statement
                
            # if the user does not want to search for a specific process
            } elseif ($process -eq "N") {

                $there = Test-Path $path\$name
                
                if ($there -eq "True") {
                    
                    Get-Process | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"
                
                } else {

                    Write-Host "| Error of Saving File to $path\$name |"
                
                } # end if statement

            } else {

                break

            } # end if statement

        # If the user does not wish to save the file as a CSV
        } elseif ($csv -eq "N") {

            $process = read-host -prompt "Would you like to search for a specific process? (Y/N)"
            
            # If the user wishes to search for a specific process
            if ($process -eq "Y") {

                $whichProcess = read-host -prompt "Name the Process"

                Get-Process $whichProcess | out-host
            
            # if the user does not want to search for a specific process
            } elseif ($process -eq "N") {

                Get-Process | out-host

            } else {

                break

            } # end if statement

        } else {

            break

        } # end if statement

} # End of task1 function



# Lists all running services and the user can save to a CVE if they want
function task2 {

    $csv = read-host -prompt "Would you like to save results to a CSV file? (Y/N)"
        
        # If the user wishes to save the results as a CSV file
        if ($csv -eq "Y") {

            $path = read-host -prompt "Enter file path to save (ex. C:\users\bguest\desktop)"
            $name = read-host -prompt "Enter file name (ex. services.csv)"
            $service = read-host -prompt "Would you like to search for a specific Service? (Y/N)"
           
            # If the user wishes to search for a specific service
            if ($service -eq "Y") {

                $whichService = read-host -prompt "Name the Service"
                $there = Test-Path $path\$name
                
                if ($there -eq "True") {
                
                    Get-Service $whichService | where {$_.Status -eq "Running"} | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"
                
                } else {

                    Write-Host "| Error of Saving File to $path\$name |"
                
                } # end if statement
            
            # If the user does not wish to search for a specific service
            } elseif ($service -eq "N") { 
                
                $there = Test-Path $path\$name
                
                if ($there -eq "True") {
                
                    Get-Service | where {$_.Status -eq "Running"} | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"
                
                } else {

                    Write-Host "| Error of Saving File to $path\$name |"
                
                } # end if statement

            } else {

                break

            } # end if statement

        # If the user does not wish to save the file as a CSV
        } elseif ($csv -eq "N") {

            $service = read-host -prompt "Would you like to search for a specific service? (Y/N)"

            # If the user wishes to search for a specific service
            if ($service -eq "Y") {
                
                $whichService = read-host -prompt "Name the Service"
                Get-Service $whichService | where {$_.Status -eq "Running"} | out-host

            } elseif ($service -eq "N") {

                Get-Service | where {$_.Status -eq "Running"}

            } else {

                break

            } # end if statement

        } else {

            break

        } # end if statement

} # End of task2 function



# Lists installed packages and the user can save to a CVE file if they want to
function task3 {
    
    $csv = read-host -prompt "Would you like to save results to a CSV file?(Y/N)"
        
        # If the user wishes to save the results as a CSV file
        if ($csv -eq "Y") {
            
            $path = read-host -prompt "Enter save path(ex. C:\users\bguest\desktop)"
            $name = read-host -prompt "Enter file name(ex. services.csv)"
            $package = read-host -prompt "Would you like to search for a specific Package? (Y/N)"
            
            # If the user wishes to search for a specific package
            if ($package -eq "Y") {
                
                $whichPackage = read-host -prompt "Which Package?"
                $there = Test-Path $path\$name
                
                if ($there -eq "True") {

                    Get-Package | where {$_.Name -ilike "*$whichPackage*"} | Select Name, Version, InstallDate | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"

                } else {
                    
                    Write-Host "| Error of Saving File to $path\$name |"

                } # end if statement

            # If the user does not wish to search for a specific package
            } elseif ($package -eq "N") {
                
                $there = Test-Path $path\$name
                
                if ($there -eq "True") {

                    Get-Package | Select Name, Version, InstallDate | Export-Csv -NoTypeInformation -Path $path\$name
                    Write-Host "| File saved to $path\$name |"
                
                } else {

                    Write-Host "| Error of Saving File to $path\$name |"

                } # end if statement

            } else {

                break

            } # end if statement

        # If the user does not wish to save the results as a CSV file
        } elseif ($csv -eq "N") {

            $package = read-host -prompt "Would you like to search for a specific package? (Y/N)"
            
            # If the user wishes to search for a specific package
            if ($package -eq "Y") {
                
                $whichPackage = read-host -prompt "Name the Package"
                Get-Package | where {$_.Name -ilike "*$whichPackage*"} | Select Name, Version, InstallDate | out-host
            
            # If the user does not wish to search for a specific package
            } elseif ($package -eq "N") {
                
                Get-Package | Select Name, Version, InstallDate
            
            } else {

                break

            } # end if statement

        } else {

            break

        } # end if statement

} # End of task3 function



# Lists the processor, RAM, and disk information and the user can save to a CSV file
function task4 {

    $processor = Get-WmiObject Win32_Processor
    $ram = [math]::Round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory/1GB)
    $disks = Get-PhysicalDisk
    $diskSpaceAvailable = [math]::Round((get-wmiobject -class win32_logicaldisk -Filter "DeviceID = 'C:'").FreeSpace/1GB)

    $csv = read-host -prompt "Would you like to save results to a CSV file? (Y/N)"
        
        # If the user wishes to save the results as a CSV file
        if ($csv -eq "Y") {

            $path = read-host -prompt "Enter save path (ex. C:\users\bguest\desktop)"
            $name = read-host -prompt "Enter file name (ex. services.csv)"
            $there = Test-Path $path\$name
            
            if ($there -eq "True") {
                
                $processor, $ram, $disks, $diskSpaceAvailable | Export-Csv -NoTypeInformation -Path $path\$name
                Write-Host "| File saved to $path\$name |"
            
            } else {

                Write-Host "| Error of Saving File to $path\$name |"

            } # end if statement

        # If the user does not wish to save the results as a CSV file
        } elseif ($csv -eq "N") {
            
            Get-WmiObject Win32_Processor
            Write-Host "Ram:"
            [math]::Round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory/1GB)
            
            Get-PhysicalDisk
            Write-Host "Free Disk Space:"
            [math]::Round((get-wmiobject -class win32_logicaldisk -Filter "DeviceID = 'C:'").FreeSpace/1GB)

        } else {

            break

        } # end if statement

} # End of task4 function



# Lists Windows Event Logs and the user can save to a CVE if they want
function task5 {

    Get-EventLog -list
    $logSearch = read-host -prompt "What event log would you like to search?"
    $amount = read-host -prompt "How many events would you like to display?"
    $keyWord = read-host -Prompt "Enter a keyword/timeframe"
    Get-EventLog $logSearch -Newest $amount | where {$_.Message -ilike "*$keyword*"}

    $csv = read-host -prompt "Would you like to save results to a CSV file? (Y/N)"
        
        # If the user wishes to save the results as a CSV file
        if ($csv -eq "Y") {

            $path = read-host -prompt "Enter save path(ex. C:\users\bguest\desktop)"
            $name = read-host -prompt "Enter file name(ex. services.csv)"

            Get-EventLog -list
            $logSearch = read-host -prompt "What event log would you like to search?"
            $amount = read-host -prompt "How many events would you like to display?"
            $keyWord = read-host -Prompt "Enter a keyword/timeframe"
            
            $there = Test-Path $path\$name
            
            if ($there -eq "True") {

                Get-EventLog $logSearch -Newest $amount | where {$_.Message -ilike "*$keyword*"} | Export-Csv -NoTypeInformation -Path $path\$name
                Write-Host "The file has been saved to $path\$name"

            } else {

                Write-Host "There has been an error saving the file"

            } # end if statement

        # If the user does not wish to save the results as a CSV file
        } elseif ($csv -eq "N") {

            Get-EventLog -list
            $logSearch = read-host -prompt "What event log would you like to search?"
            $amount = read-host -prompt "How many events would you like to display?"
            $keyWord = read-host -Prompt "Enter a keyword/timeframe"
            Get-EventLog $logSearch -Newest $amount | where {$_.Message -ilike "*$keyword*"}

        } else {

            break
        
        } # end if statement

} # End of task5 function



# Function to email information
function email{

    $subject = Read-Host -Prompt "Enter a subject:"
    $message = Read-Host -Prompt "Enter a message:"
    $who = Read-Host -prompt "Enter your e-mail:"
    $toWho = Read-Host -Prompt "Enter the e-mail of the person you want to send this to:"
    $msg = "CVE NAME: $entryName", "CVE DESC: $entryDesc", "CVE STAT: $entryStatus"

    Send-MailMessage -from $who -to $toWho -Subject $subject -body $message, " ", $msg
        
} # End of email function



# Asks to download or load file for use. Searches CVE file for name of file or description keyword
function task6 {

    $download = read-host -prompt "Would you like to download the allitems.csv file? (Y/N)"
        
        # If the user wishes to download the file
        if ($download -eq "Y") {
           
            Invoke-WebRequest -URI https://cve.mitre.org/data/downloads/allitems.csv -OutFile C:\Users\bguest\Desktop\allitems.csv
            Write-Host "The CSV file has been downloaded to C:\Users\bguest\Desktop\allitems.csv"
        
        # If the user does not wish to download the file
        } elseif ($download -eq "N") {
            
            $cveFile = import-csv C:\Users\bguest\Desktop\allitems.csv -header Name,Status,Description
            $nameDesc = Read-Host -Prompt "Would you like to search the CVE by [N]ame or [D]escription"
            
            # If the user wishes to search the CVE by name
            if ($nameDesc = "N") {
                
                $name = Read-Host -Prompt "Enter Name (Ex. CVE-1999-0001)"
           
                # Searches through the CVE file    
                foreach ($cveEntry in $cveFile) {
            
                    # If the entry is found "found" will get printed and the data will be printed    
                    if ($cveEntry.Name -eq "$name") {
                        Write-Host "| Found |"
                       
                        $entryName = $cveEntry.Name
                        $entryDesc = $cveEntry.Description
                        $entryStatus = $cveEntry.Status
                        write-host "CVE NAME: $entryName"
                        Write-Host "CVE DESC: $entryDesc"
                        Write-Host "CVE STAT: $entryStatus"     
                        
                        $notFound = "false"
                       
                        email

                        break

                    } else {
                    
                        #If not found the script will continue
                        if ($notFound -eq "false") {

                            continue

                        } else {

                            # Set value to "true" if no entry is found.
                            $notFound = "true"

                        } # end if statement

                    } # end if statement

                } # end if statement

            # If the user wishes to search the CVE file by description
            } elseif ($nameDesc = "D") {

                $keyword = Read-Host -Prompt "Enter Keyword"
                
                foreach ($cveEntry in $cveFile) {

                    if ($cveEntry.Description -ilike "*$keyword*") {
    
                        # Print that the CVE was found.
                        write-host "| Found |"

                        # Print the results for the CVE.
                        $entryName = $cveEntry.Name
                        $entryDesc = $cveEntry.Description
                        $entryStatus = $cveEntry.Status

                        write-host "CVE NAME: $entryName"
                        Write-Host "CVE DESC: $entryDesc"
                        Write-Host "CVE STAT: $entryStatus"

                        # Set value to false to denote the entry was found.
                        $notFound = "false"

                        email

                    } else {

                        if ($notFound -eq "false") {

                            continue

                        } else {

                            # Set value to "true" if no entry is found.
                            $notFound = "true"

                        } # end if statement

                    } # end if statement

                } # end if statement

            } else {

                Write-Host "| Please enter a Valid Option |"
                task6

            } # end if statement

        } else {
            
            task6

        } # end if statement

} # End of task6 function



# SysAdmin menu
function sysAdmin {
    
    # clears the screen
    clear

    write-host "| SYSTEM ADMIN MENU |"
    write-host ""
    write-host "1. List All Running Processes."
    write-host "2. List All Running Services"
    write-host "3. Installed Packages."
    Write-Host "4. Processor, Ram, and Disks"
    Write-Host "5. Windows Event Logs"
    write-host "[R]eturn to Main Menu."
    write-host "[E]xit"

    $sysAdminTask = Read-Host -Prompt "Please select an Option"

    if ($sysAdminTask -eq "R") {

        mainMenu

    } elseif ($sysAdminTask -eq 1) {

        task1

    } elseif ($sysAdminTask -eq 2) {

        task2

    } elseif ($sysAdminTask -eq 3) {

        task3

    } elseif ($sysAdminTask -eq 4) {

        task4

    } elseif ($sysAdminTask -eq 5) {

        task5

    } elseif ($sysAdminTask -eq "E") {

        break

    } else {

        write-host -BackgroundColor Red -ForegroundColor White "| Invalid Option |"
        sleep 4

        # Call the menu so the user can start again.
        sysAdmin

    } # end if statement

    # Allow the user to review the results
    allDone

    # Call the sysAdmin menu, because they are currently working in this menu.
    sysAdmin

} # End of sysAdmin function



# SecAdmin Menu
function secAdmin {
    
    # clears the screen
    clear

    write-host "| SECURITY ADMIN MENU |"
    write-host ""
    write-host "1. List All Running Processes."
    write-host "2. List All Running Services"
    write-host "3. Installed Packages."
    Write-Host "4. Processor, Ram, and Disks"
    Write-Host "5. Windows Event Logs"
    Write-Host "6. Recent Security Vulnerabilities"
    write-host "[R]eturn to Main Menu."
    write-host "[E]xit"

    $secAdminTask = Read-Host -Prompt "Please select an Option"

    if ($secAdminTask -eq "R") {

        mainMenu

    } elseif ($secAdminTask -eq 1) {

        task1

    } elseif ($secAdminTask -eq 2) {

        task2

    } elseif ($secAdminTask -eq 3) {

        task3

    } elseif ($secAdminTask -eq 4) {

        task4

    } elseif ($secAdminTask -eq 5) {

        task5

    } elseif ($secAdminTask -eq 6) {

        task6

    } elseif ($secAdminTask -eq "E") {
        
        break

    } else {

        write-host -BackgroundColor Red -ForegroundColor White "| Invalid Option |"
        sleep 4

        # Call the  menu so the user can start again
        secAdmin

    } # end if statement

    # Allow the user to review the results
    allDone

    # Call the secAdmin menu, because they are currently working in this menu
    secAdmin

} # End of secAdmin function

# Call the mainMenu function
mainMenu
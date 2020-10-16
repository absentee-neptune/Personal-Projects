# Get Security event logs

# Get the security events using Get-EventLog
#Get-EventLog -List
#Get-EventLog security | where {$_.Message -ilike "*success*"

# List running processes and search for specific ones
#ps | where {$_.ProcessName -ilike "*calc*" -or $_.ProcessName -eq "notepad" }

# Get the process to run from the user:
#$user_input = read-host -Prompt "Please enter the process name to search for"

#Write-Host -backgroundcolor Red -ForegroundColor White $user_input

#$the_cmd = ps | where {$_.ProcessName -ilike "*$user_input*" }

# Prompt the user what to do with the results
#$to_save = Read-Host -Prompt "Do you want to save the results? [Y|N]"

# process the results
#if ($to_save -eq "Y") {

    # Save the results of $the_cmd to a csv
#    $the_cmd | Export-Csv -NoTypeInformation -Path "c:\users\bguest\desktop\ps-output.csv"

#} else {
    
    # If they select N or some other option
    # Print the results to the screen
#    $the_cmd

#}

#####################################################################################################################

# Send an Email

# Create the message body
#$msg = "Hey Adam, 'n I'm spamming you because duane said I could. hehehe!"

# Create the email structure using send-MailMessage
#Send-MailMessage -BodyAsHtml -From "barack.obama@whitehouse.gov" -To "agoldstein@champlain.edu" -Subject "I'm learning stuff" -Body $msg -SmtpServer 192.168.1.32
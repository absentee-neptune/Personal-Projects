# Get Security event logs

# Get the events using Get-EventLog
Get-EventLog -List

# Get the process to run from the user:
$user_input = read-host -Prompt "Please enter the Event Log to search for"

Write-Host -backgroundcolor Red -ForegroundColor White $user_input

$the_cmd = Get-EventLog $user_input -Before "09/12/2019" | where { $_.Message -ilike "*success*" }

# Prompt the user what to do with the results
$to_save = Read-Host -Prompt "Would you like to save the results or Email them? [Save|Email]"

# process the results
if ($to_save -eq "Save") {

    # Save the results of $the_cmd to a csv
    $location = Read-Host -Prompt "Where do you want to save the results? (Remember to include the full path and file name)"

    Write-Host -BackgroundColor DarkGray -ForegroundColor White $location

    $the_cmd | Export-Csv -NoTypeInformation -Path $location

} if ($to_save -eq "Email") {

    # If they select Email
    Send-MailMessage -BodyAsHtml -From "brianna.guest@mymail.champlain.edu" -To "mini@miniBuntu" -Subject "Week 2 Assignment" -Body "$the_cmd" -SmtpServer 192.168.1.32

} else {
    
    # If they select some other option
    # Print the results to the screen
    $the_cmd

}
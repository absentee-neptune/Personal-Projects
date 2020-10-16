# Story Line: Download a CVE file and process it to look for vulnerabilities

# Download the CVE file
#Invoke-WebRequest -URI http://192.168.1.32/cve.csv -OutFile "C:\Users\bguest\Desktop\cve.csv"

# Import the cve file into powershell.
$CVE_File = Import-Csv "C:\Users\bguest\Desktop\cve.csv"

#$CVE_File |gm

$keyword = read-host -Prompt "Please enter a keyword"

# Then we will search for some data.
foreach ($cveEntry in $CVE_File) {

# read-host prompts for the user to select CVE Entry or Search by Description
     # For the description, which comparison operator will we use? -ilike
    #if ($cveEntry.Name -eq "CVE-1999-0001") {

    # TASK: Create a prompt that allows the user to specify an arbitrary keyword.
    if ($cveEntry.Description -ilike "*bsd*") {
    
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
        # Stops the foreach loop since the file only contains one CVE named "CVE-1999-0001"
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
}
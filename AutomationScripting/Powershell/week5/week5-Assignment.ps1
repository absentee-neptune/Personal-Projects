# Storyline: Download osint files and create an iptabeles ruleset.

# Array of websites containing threat intell
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list
foreach ($u in $drop_urls) {

    # Extract the filename
    # Split takes a string and converts it into an array.
    $temp = $u.split("/")

    $temp
    # The last element in the array plucked off is the filename
    $file_name = "./" + $temp[4]

    # Download the rules list
    #Invoke-WebRequest -Uri $u -OutFile $file_name

}

# Array containing the filename
$input_paths = @('.\fa19-sys320-201-brianna-guest\week5\compromised-ips.txt','.\fa19-sys320-201-brianna-guest\week5\emerging-botcc.rules')

# Extract the IP addresses.
# \d = digit
# \b = boundary
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list.
Select-String -Path $input_paths -Pattern $regex_drop -AllMatches | % { $_.Matches } | % { $_.Value } | sort | Get-Unique -AsString | Out-File -FilePath ".\fa19-sys320-201-brianna-guest\week5\ips-bad.txt"

# Get the IP addresses discovered, loop through and replace the beginning of the line with the IPTables syntax
# After the IP address, add the remaining IPTables syntax and save the results to a file.
(Get-Content -Path ".\fa19-sys320-201-brianna-guest\week5\ips-bad.txt") | % { $_ -replace "^", "iptables -A INPUT -s" -replace "$", " -j DROP" } `
#| Set-Content -Path ".\fa19-sys320-201-brianna-guest\week5\ips-bad-iptables.bash"

# Get IP addresses discovered, loop through and replace the beginning of the line with cisco ruleset syntax.
(Get-Content -Path ".\fa19-sys320-201-brianna-guest\week5\ips-bad.txt") | % { $_ -replace "^", "access-list deny host " } `
#| Set-Content -Path ".\fa19-sys320-201-brianna-guest\week5\ips-bad-iptables.bash"
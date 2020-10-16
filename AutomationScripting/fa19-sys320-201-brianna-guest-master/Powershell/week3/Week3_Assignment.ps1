# Week 3 Assignment - Incident Response Script
cls

# List Wmi-objects
#Get-WmiObject -list | sort

# Select the ProcessName, id, and path for the Process Lists class
Get-WmiObject -Class Win32_Process | Select Name, ID, Path | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\ProcessLists.csv"

# Select the ProcessName, id, and path for the Services class
Get-WmiObject -Class Win32_Service | Select Name, ID, Path | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\AllServices.csv"

# Select the ProcessName, id, and path for the Services class that are Running
Get-Service | where { $_.Status -eq "Running" } | Select Name, ID, Path | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\RunningServices.csv"

# Select the Name, PasswordRequired, InstallDate, Accounttype for the win32_account class
Get-WmiObject -Class Win32_userAccount | Select Name, PasswordRequired, Accounttype | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\Users.csv"

# Obtaining all Installed Software through the SoftwareFeature class
Get-WmiObject -Class Win32_SoftwareFeature | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\InstalledSoftware.csv"

# Obtaining all Current TCP Connections
Get-NetAdapter | Export-Csv -NoTypeInformation -Path "C:\Users\bguest\Desktop\CurrentTCPConnections.csv"

# Story line: Dig deeper into the Windows OS using WMI (Windows Management Instrumentation)

# List Wmi-objects
#Get-WmiObject -list

# Filter a specific WMI-Object
#Get-WmiObject -List | where { $_.Name -eq "Win32_Account" }


# Use Get-Member to list the properties for the wmi-object
#Get-WmiObject -Class Win32_Account | Get-Member

# TASK: Select the Name, PasswordRequired, InstallDate, Accounttype for the win32_account class
#Get-WmiObject -Class Win32_Account | Select Name, PasswordRequired, InstallDate, Accounttype

# Filter for WMI-object using regular expressions (regex)
#Get-WmiObject -List | where { $_.Name -ilike "win32_[a-c]*" } | sort

# TASK: Filter for the network adapter wmi-object using regex.
#Get-WmiObject -List | where { $_.Name -ilike "win32_[n]*" } | sort
# Story Line; Learn to use arrays and send an email to each person.

cls
# Create the body of the email
$msg = "hey there."

# create an array of email addresses
$emailAddresses = @('tupac@alypse.com','biggie@alypse.com','presley@alypse.com')

# Loop through the array
while ($true) {
    foreach ($email in $emailAddresses) {

        write $email
        Send-MailMessage -from "flavorflava@fatgoldchain.gov" -to $email -Subject "Hey There." -Body $msg -SmtpServer 192.168.1.32

    } # foreach loop

} # end while loop
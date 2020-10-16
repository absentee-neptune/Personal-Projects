#SECURE-SSH.SH
#AUTHOR TURTLE0910
#!/bin/bash

#Creates a new ssh user called $l
read l

sudo useradd $l
sudo usermod -aG wheel $l
sudo mkdir /home/$l/.ssh

#Adds a public key to that users authorized key file
sudo cp linux/public-keys/SYS265.pub /home/$l/.ssh/authorized_keys

#Removes roots ablility to ssh in
sudo chmod 700 /home/$l/.ssh
sudo chmod 644 /home/$l/.ssh/authorized_keys
sudo chown -R $l:$l /home/$l/.ssh

echo "testing 123"

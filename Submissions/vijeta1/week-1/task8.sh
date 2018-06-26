#!/bin/sh

echo "1.SSH Tunnelling"
echo "2.One liner script to copy a folder to a directory named week-1 on remote server/vagrant VM."
echo "3.SFTP Connection to remote server/vagrant VM."
echo "4.Proxy Setting using export command."
echo "5.Proxy Setting by addind in .bashrc file."
echo "Enter your choice from above option."


read Choice

case $Choice in 

(1) echo "Enter port number."
	read port
	echo "Enter local_host"
	read local_host
	echo "Enter remote_host"
	read remote_host

	ssh -L $port:$local_host:$port $remote_host;;

(2) echo "Enter the location of folder you want to copy"
	read folder_location
	echo "Enter the location of directory of vagrant vm"
	read dir_location
	echo "Enter port number for vagrant vm"
	read port
	echo "Enter location of private key of vagrant vm"
	read pkey_location
	echo "Enter username of vagrant vm"
	read username
	scp -i $pkey_location -P $port $folder_location $username@127.0.0.1:~$dir_location;;
(3) echo "Enter the location of vagrant vm private key"
	read pkey_location
	echo "Enter the port"
	read port
	echo "Enter the local host ip"
	read local_hostIP
	sftp -P $port -i $pkey_location vagrant@$local_hostIP;;
(4) echo "Enter the proxy server"
	read proxy_server
	echo "Enter the port number"
	read port
	export HTTPS_PROXY=http://$proxy_server:$port/;;
(5) echo "Enter proxy server"
	read proxy_server
	echo "Enter the port number"
	read port
	export https_proxy=http://$proxy_server:$port/ >> ~/.bashrc;;


esac


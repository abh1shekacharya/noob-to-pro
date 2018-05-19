#!/bin/bash
Tunnel()
{
	echo "Print enter the port yow want to forward and to which port you want to forward."
	read forwardport forwardedport
	echo "Enter the local host adress"
	read hst
	echo "Enter the username "
	read usr
	echo "Enter the server ip address"
	read ip
	ssh -L $forwardport:$hst:$forwardedport $usr@$ip
	exit
	
	
}
SCPCopy()
{
	echo "Enter the path of folder "
	read path1
	echo "Enter the username "
	read usr
	echo "Enter the server ip address"
	read ip
	echo "Enter the path of the directory where you want to copy the folder"
	read path2
	scp -r $path1 $usr@$ip:$path2
	if [ "$?" = "0" ]
	then
		echo "Copied successfully :-)"
	else
		echo "You made a mistake somewhere. Try again"
	fi
	exit
}
Connection()
{
	echo "Enter the username "
	read usr
	echo "Enter the server ip address"
	read ip
	sftp $usr@$ip
	if [ "$?" = "0" ]
	then
		echo "SFTP connection is successfull. :-)"
	else
		echo "You made a mistake somewhere. Try again"
	fi
	exit
}

etc()
{	
	host1=""
	host2=""
	host3=""
	port1=""
	port2=""
	port2=""
	echo "Enter the http_host"
	read host1
	echo "Enter the http_port"
	read port1
	echo "Same for ftp and https ? [y or n ]"
	read y
	
	if [[ "$y" = "Y" || "$y" = "y" ]];
	then
		host2=$host1
		port2=$port1
		host3=$host1
		port3=$port1
	else
		echo "Enter the https_host"
		read host2
		echo "Enter the https_port"
		read port2
		echo "Enter the ftp_host"
		read host3
		echo "Enter the ftp_port"
		read port3
	fi
	
	echo "You must be root user to change the settings"
	
	echo "Use authentication ? [Y or N ]"
	read y
	if [[ "$y" = "Y" || "$y" = "y" ]];
	then
		echo "Enter username"
		read usr
		echo "Enter password use %40 in place of @ "
		read -s pass
		touch gyani.txt
		echo "http_proxy=\"http://$usr:$pass@$host1:$port1\"" >> gyani.txt
		echo "https_proxy=\"http://$usr:$pass@$host2:$port2\"" >> gyani.txt
		echo "ftp_proxy=\"ftp://$usr:$pass@$host3:$port3\"" >> gyani.txt
		
		cat gyani.txt |sudo tee -a /etc/environment 
		rm gyani.txt
	else
		
		touch gyani.txt
		echo "http_proxy=\"http://$host1:$port1\"" >> gyani.txt
		echo "https_proxy=\"http://$host2:$port2\"" >> gyani.txt
		echo "ftp_proxy=\"ftp://$host3:$port3\"" >> gyani.txt
		
		cat gyani.txt |sudo tee -a /etc/environment  
		rm gyani.txt
	fi
	exit
}
bashrc()
{	
	host1=""
	host2=""
	host3=""
	port1=""
	port2=""
	port2=""
	echo "Enter the http_host"
	read host1
	echo "Enter the http_port"
	read port1
	echo "Same for ftp and https ? [y or n ]"
	read y
	
	if [[ "$y" = "Y" || "$y" = "y" ]];
	then
		host2=$host1
		port2=$port1
		host3=$host1
		port3=$port1
	else
		echo "Enter the https_host"
		read host2
		echo "Enter the https_port"
		read port2
		echo "Enter the ftp_host"
		read host3
		echo "Enter the ftp_port"
		read port3
	fi
	
	echo "You must be root user to change the settings"
	
	echo "Use authentication ? [Y or N ]"
	read y
	if [[ "$y" = "Y" || "$y" = "y" ]];
	then
		echo "Enter username"
		read usr
		echo "Enter password use %40 in place of @ "
		read -s pass
		touch gyani.txt
		echo "http_proxy=\"http://$usr:$pass@$host1:$port1\"" >> gyani.txt
		echo "https_proxy=\"http://$usr:$pass@$host2:$port2\"" >> gyani.txt
		echo "ftp_proxy=\"ftp://$usr:$pass@$host3:$port3\"" >> gyani.txt
		
		cat gyani.txt |sudo tee -a $HOME/.bashrc 
		rm gyani.txt
	else
		
		touch gyani.txt
		echo "http_proxy=\"http://$host1:$port1\"" >> gyani.txt
		echo "https_proxy=\"http://$host2:$port2\"" >> gyani.txt
		echo "ftp_proxy=\"ftp://$host3:$port3\"" >> gyani.txt
		
		cat gyani.txt |sudo tee -a $HOME/.bashrc  
		rm gyani.txt
	fi
	exit
}
echo "
Choose option 
1) Tunnel your port
2) Copy a folder to a server through scp
3) SFTP connection
4) Set Prxoy Settings for applications in /etc/environment
5) Set proxy variables in .bashrc file 

"
read i
case $i in
	1)
		Tunnel
		;;
	2)
		SCPCopy
		;;
	3)
		Connection
		;;
	4)
		etc
		;;
	5)
		bashrc
		;;	
esac	
		



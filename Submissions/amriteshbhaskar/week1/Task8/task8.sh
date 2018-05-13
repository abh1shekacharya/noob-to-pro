#!/bin/sh

cat<<END
Hey There! what you want to do?
1)SSH Tunneling
2)Copy folder to server or vagrant VM
3)SFTP connection to server or vagrant VM
4)Proxy setting using export command
5)Proxy Setting by adding in .bashrc file
END
read -p " Enter your choice:- " task


case $task in
	1) read -p "Enter the port you want to tunnel" port
		 read -p "Enter the Target Port " tport
	   read -p "Enter the IP address of server " ip
		 read -p "Enter the UserName " user
		 read -p "Enter the ssh Port " ssh
		 ssh -L $port:localhost:$tport $user@$ip -p $ssh
		 ;;
  2) read -p "Enter the folder address you want to copy to remote location" folder
	   read -p "Enter the directory where you want to copy" foldi
		 read -p "Enter the Remote Server IP " ip
		 read -p "If you want to copy a folder to vagrant(VM) press 'v' or 's' for remote server" ch
		 if [ $ch = "v" ]; then
		 		read -p "Enter the private key of Varant VM" pkey
				scp -r -P 2222 -i $pkey $folder vagrant@$ip:$foldi
		 else
		 		read -p "Enter the UserName of server" user
				scp -r $folder $user@$ip:$foldi
		 fi	 
		 ;;
	3) read -p "Enter the IP address " ip
	   read -p "Vagrant('v') or Remote Server('s') " ch
		 if [ $ch = "v" ]; then
		 		read -p "Enter the location of private key " pkey
				sftp -P 2222 -i $pkey vagrant@$ip
		 else
		 		read -p "Enter UserName " user
				sftp $user@$ip
		 fi		
		 ;;
	4) read -p "Enter proxy address " proxy
		 read -p "Enter proxy port " port
		 read -p "Enter proxy username " name
		 read -p "Enter proxy password " pass
	   export http_proxy="http://$name:$pass@$proxy:$port"
		 export https_proxy="http://$name:$pass@$proxy:$port"
		 export ftp_proxy="http://$name:$pass@$proxy:$port"
		 ;;
	5) read -p "Enter proxy address " proxy
     read -p "Enter proxy port " port
     read -p "Enter proxy username " name
     read -p "Enter proxy password " pass
		 echo "export http_proxy="http://$name:$pass@$proxy:$port"" >> ~/.bashrc
		 echo "export https_proxy="http://$name:$pass@$proxy:$port"" >> ~/.bashrc
		 echo "export ftp_proxy="http://$name:$pass@$proxy:$port"" >> ~/.bashrc
	   ;;
esac		 


#this is comment
echo "1.SSH tunnelling"
echo "2.One liner to copy a folder to a directory named week-1 on remote server/vagrant VM"
echo "3.SFTP connection to the remote server/ vagrant VM"
echo "4.Proxy Setting using export command"
echo "5.Proxy Setting by adding in .bashrc file"
echo "Enter your choice(1-5)"
read choice

case $choice in

1) echo "Enter the port number"
	read port
	echo "Enter the user name"
	read name
	echo "Enter the server ip"
	read ip 
	ssh -R $port:localhost:80 $name@$ip;;

2)		echo "Enter the address of folder you want to tranfer "
		read lfad
		echo "Enter the address of remote folder where local folder is to copy"
		read sfad
		echo "Enter the server ip "
		read ipv
echo "Do you want to connect to vagrant server ( y or n)"
	read ans
	if [ $ans = "y" -o $ans = "Y" ]
	then
		echo "Enter the address of vagrant private key"
		read key 
				
		scp -r -P 2222 -i $key $lfad vagrant@$ipv:$sfad
	else
		echo "Enter the user name"
		read name
		scp -r -P 2222 $lfad $name@$ipv:$sfad
	fi;;

3)echo "Enter the address of vagrant private key"
	read key 
	echo "Enter the server ip "
	read ipv
	sftp -P 2222 -i $key vagrant@$ipv;;

4)	echo "Enter username "
	read user_name
	echo "Enter password(If possword contains special characters kindly uses haxe code of that charater with % sigh instead of x )"
	read password
	echo "Enter the proxy server"
	read proxy_server
	echo "Enter the port number"
	read port
	export http_proxy="$user_name:$password@http://$proxy_server:$port"
	export https_proxy="$user_name:$password@http://$proxy_server:$port"	
	export ftp_proxy="$user_name:$password@http://$proxy_server:$port";;

5)	echo "Enter username "
	read user_name
	echo "Enter password(If possword contains special characters kindly uses haxe code of that charater with % sigh instead of x )"
	read password
	echo "Enter the proxy server"
	read proxy_server
	echo "Enter the port number"
	read port
	echo "export http_proxy=\"$user_name:$password@http://$proxy_server:$port\"" >> ~/.bashrc
	echo "export https_proxy=\"$user_name:$password@http://$proxy_server:$port\"" >> ~/.bashrc	
	echo "export ftp_proxy=\"$user_name:$password@http://$proxy_server:$port\"" >> ~/.bashrc;;

esac

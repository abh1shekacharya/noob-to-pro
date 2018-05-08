# Week-1 : Lab Setup and basics

**( Timeline : 8<sup>th</sup> May'18 - 12<sup>th</sup> May'18, this week's shorter )**
 
1. Bascis of SSH and SSH tunnelling,  SCP , SFTP ( how to connect to digital ocean/aws or any other VPSes )

2. Shell scripting , Automating as many tasks as possible.

3. Proxy setting up using different environment variables , like 
	* all_proxy
	* http_proxy
	* https_proxy
	* Setting in **/etc/environment** file etc

Needless to say write a script to do the same

4. Set up **2 VMs** ,
	1. Vagrant [EpicTreasure](https://github.com/ctfhacker/EpicTreasure) and change according to your needs ( like it has 8gb RAM and 4 cores assigned for the virtual box , change it accordingly to suit your system ).
	2. The 2nd being [Flare-VM](https://github.com/fireeye/flare-vm) windows virtual machine.

These two would contain moslty all the tools you would ever need for either Windows reversing or Linux reversing/pwning or basic maleware analysis.


|#| Task		| Points	|	Format To Submit	|
|--| ------------- 	| -------------	|	-------------------		|
|1| SSH tunnelling ( one liner script )<sup>1</sup>  | 50  |	C	|
|2| One liner to copy a _folder_ to a directory named **week-1** on remote server/vagrant VM  | 50  |	C	|
|3| SFTP connection to the remote server/ vagrant VM  | 50  |	S	|
|4| Proxy Setting using export command  | 50  |		C	|
|5| Proxy Setting by adding in .bashrc file  | 50  |	S	|
|6| Setting up vagrant VM<sup>2</sup>  | 100  |		G/V	|
|7| Setting up vagrant Flare-VM  | 100  |		G/V	|
|8| **BONUS** : Write a script for task 1-5	| 200	| C	|
|| **TOTAL** 	| **650**	|

1 : Show the output of `lsof` to show the port is opened and which program is running on this port.

**Sample Output ( I have tunnelled on port 8123 )**
![Sample output of lsof -i:8123](https://user-images.githubusercontent.com/17861054/39735433-2e224300-5299-11e8-87c9-101f0979a36b.png)

2 : Modify epictreasure's VagrantFile, any subtle change would do, like changing the no. of cores in the VM ( you would surely want to change that )

Index	|	|
--------|-------|
C	| Code	|
S	| Screenshot	|
G/V	| Gif/Video	|


### enjoy hacking :)
### try harder

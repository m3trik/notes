# Linux Command Line notes






# HELP -----------------------------------------------------------------

#keyboard shortcuts:
#autocomplete.  tab key twice to get all possible suggestions.

history	#returns all history.
history 0 #commands can be ussued by history index

apropos	<keyword> #list available commands relating to a keyword. #ex. apropos time

which <command> #get the location of a command.

whatis <command> #get the description of a command.

man <command> #manual for a command.







# VARIABLES -------------------------------------------------------------

#user assigned:
#set
VARIABLE="value"
#get
$VARIABLE


#environment variables:
#set env var
JAVA_HOME="/usr/lib/jvm/java-8-oracle/" #add a new line in the env file.
#using command line:
export CATALINA_HOME=/opt/catalina #set global variable
#get
sudo nano /etc/environment #user env file
env #list current user env variables
env | grep PATH #prints info on the PATH variable
#
$PATH #returns a colon separated list of file paths.
$HOME #home directory
$USER #name of the current user
$PS1 #prompt style #ex. export PS1=">> "






# OWNERSHIP ------------------------------------------------------------

#enviroment settings
~/.bash_profile	# '~' represents the user's home directory. '.' indicates a hidden file.


#change user name
sudo usermod -l <newname> <oldname> #kill <PID-number> #kill a process.
#change home folder name
sudo usermod -d /home/<newname> -m <newname> #after username change.
#change password
sudo passwd <username>


#get root privileges for the session
sudo -s


#list all groups
sudo cat /etc/group
#get a group's members
getent group <groupname>
#create group
groupadd <groupname>
#create new user and add to group
sudo useradd <username> -G <groupname>
#add user to group
usermod -a -G <groupname> <username> #-a=append, -G=comma-separated list of additional groups to assign the user to.
#
adduser <username> <groupname>
#
sudo groupmod --new-name <newname> <oldname>
#delete group
groupdel <groupname>


#change ownership (as root)
chown -R <user>:<group> <dir> #ex. sudo chown -R admin:admin /mnt/Storage


#check permissions
ls -l <dir>
stat <dir>
stat -c %a dir #permissions in numeric (octal) format
#change permissions
# change home folder permissions:
chmod 0755 /home/m3trik
chmod 0644 /home/m3trik/.bashrc
chmod 0644 /home/m3trik/.profile


#change dir permissions recursively (default: 755|644)
#u=users, g=group, o=others, a|ugo=all
chmod -R g+rw <dir> #set group privaleges to read write.
#using binary values. #5=rx, 6=rw, 7=rwx
chmod -R 775 <dir> #ex. sudo chmod -R 777 /mnt/Storage






# DIRECTORIES & NAVIGATION ---------------------------------------------

#get current directory
pwd #current working directory.

#create new directory
mkdir <dir> #takes directory name(s) as arguments. #ex. mkdir newfolder additionalfolder 


#change directory
cd <dir>
#
pushd <dir> #change directorys with the ability to jump back to original using popd
popd #go back to where you were previously

#move up 
cd .. #move up one direcory level
cd ../../ #ect to move up two or more directories



#list directory contents
ls -a -t <dir> #flags [-a] all including hidden, [-l] long (table) format, [-t] order by last modified.


#search directory
locate fstab
#
sudo updatedb #manually update search database if search item is new or fresh install of linux. search db is auto-updated peridically.


#list contents
ls -la

#create a directory
mkdir <dir>
#create a symbolic link
ln -s <newdir> <olddir> #ex. sudo ln -s "/mnt/Storage/Linux/home [-j]/admin"  /home/admin
#list symbolic links
find . -type l -ls #all
find . -type l -maxdepth 1 -ls #current directory:
#remove a symbolic link
rm <link> #the file it points to is not affected.



#rename
mv <from> <to> #rename more than one file using additional <from> arguments.


#copy a directory
cp <from> <to> #[-p][--preserve] mode,ownership,timestamps. Use additional <from> arguments to copy multiple files. 
cp * <dir> #copys all files in the directory.
cp m*.txt <dir> #(m*.txt copies all files in the working directory starting with "m" and ending with ".txt")


#move a dir
mv <from> <to> #move more than one file using additional <from> arguments.
mv * <destinationdir> #wildcard for move.  selects all files in directory.
mv m*.txt <destinationdir>  #(m*.txt moves all files in the working directory starting with "m" and ending with ".txt")


#zip dir
zip -r -m <dir>.zip <dir> #-r=recursive, -m=delete the orig file
#unzip dir
unzip <dir>.zip #unzip <what> <where>



#delete a directory
rm -r -f <dir> #[-r] recursive. [-f] force. Delete a directory and all of its child directories.
#delete empty directories
remdir * #safe way to clean up all empty sub-directories in a directory













# FILES ----------------------------------------------------------------

#create a new file
touch <filename>



#edit a text based file
#using gedit
sudo gedit <dir>
#using nano
sudo nano <dir>
#using vim
sudo vi <dir>


less filename.txt #scroll through text file using arrow keys. or search for keywords.


#text
echo "" #print to terminal as standard output.   
cat >> <file> #anything typed into the terminal will be added to 'file'     #concatenate. can be used to output the contents of a file to the terminal or vice versa.

wc <file> #outputs the number of lines, words, and characters in .txt file
sort <file> #sorts lines of text alphabetically.
uniq <file> #filter adjacent duplicate lines in a file (non-adjacent files are not filtered out, calling a 'sort' command then piping in the standard output to 'uniqu' will place all duplcates adjacent before filtering)



#search
#regular expressions
#search files for lines that match a pattern and returns the results. 
grep <dir> #[-i] case insensitive. #[-R] Recursive #[-l] files with matches.

#find and replace
#using stream editor     
sed 's/search string/replacement string/g' #expressions: 's' substitution, 'g' global



#copy the contents of a text file to another text file
cp textFromThisFile.txt toThisFile.txt



#zip file
sudo zip -m <dir>.zip <dir> #-m=delete the orig file
#unzip file
unzip <dir>.zip #unzip <what> <where>




#delete a file
rm <dir> #[-f][--force] force.
#all
rm <dir> * #delete all files of the dir that start with the given file name. Used alone it removes all files in a directory.








# DISK -----------------------------------------------------------------

#list all drives
fdisk -l
#list physical drive
pvs -a
#display logical volumes
lvscan
lvmdiskscan -l #-l=return only physical volumes
lvdisplay -m #-m=also display information about how the logical volume is broken down and distributed
#display volume groups
vgscan
vgdisplay -v
#display physical volumes
pvscan
pvdisplay -m #-m=logical extents that have been mapped to each volume.



#mount a partition
mount <dir>
#mount an LVM logical volume
mount /dev/<groupname>/<volumename> /mnt/<volumename>
#unmount
umount <dir>
#unmount an LVM logical volume
umount /dev/<groupname>/<volumename>


#perform a disk check (fsck [OPTIONS] [FILESYSTEM])
fsck <dir> #run disk check
#check and attempt repair
fsck -y <dir>
#
fsck -p <dir>



#create LVM
#install lvm2
apt update
apt install lvm2

#mark the storage devices as LVM physical volumes
pvcreate <dir> <dir>
#create a new volume group from LVM physical volumes
vgcreate <groupname> <dir> <dir>
#create a logical volume of a given size
lvcreate -L 10G -n <volumename> <groupname> #creates a 10gig volume.
#create a volume using remaining free space
lvcreate -l 100%FREE -n <volumename> <groupname>

#activate volume group(s)
vgchange -ay


#resize the filesystem
resize2fs -p /dev/<groupname>/<volumename> 3G #resize to 3 gig
#resize the logical volume
lvresize -L 3G <groupname>/<volumename> #-L=logical volume


#delete the entire volume group
vgremove <groupname> #be sure that you unmount any logical volumes that the volume group contains.
#remove a logical volume
lvremove <groupname>/<volumename>
#remove a pysical volume
pvmove <dir> #relocate the extents to peer volumes.
vgreduce <groupname> <dir> #remove the physical volume from the volume group
pvremove <dir> #remove the physical volume marker from the storage device







# SCRIPTING --------------------------------------------------------------

#create a script
#shell header
#!/bin/sh
#bash header
#!/bin/bash --
#run a script
chmod u+x <script> #set permissions
./<script> #execute




# combine languages in a single shell file using heredoc import.sh
#!/bin/bash --
sqlite3 -batch $1 <<"EOF"
CREATE TABLE log_entry ( <snip> );
.separator "\t"
.import logfile.log log_entry
EOF
#run it:
import.sh database.db


#using bash variables:
#!/bin/bash --
table_name=log_entry

sqlite3 -batch $1 <<EOF
CREATE TABLE ${table_name} ( <snip> );
.separator "\t"
.import logfile.log ${table_name}
EOF


#Or even do a trick like this:
#!/bin/bash --
table_name=$2

sqlite3 -batch $1 <<EOF
CREATE TABLE ${table_name} ( <snip> );
.separator "\t"
.import logfile.log ${table_name}
EOF
#run it: 
import.sh database.db log_entry






# I/O REDIRECTION -------------------------------------------------------

Redirection #reroutes standard input, standard output, and standard error.

#The common redirection commands are:
stdin   #standard input:   information inputted into the terminal through the keyboard or input device.  
stdout  #standard output:  the information outputted after a process is run.
stderr  #standard error:   an error message outputted by a failed process.

>       #redirects the standard output to a file & overwrites (left to right)   ex.  echo "string" > textdoc.txt   ("string" is entered as the standard input. The standard output "string" is redirected by > to the file textdoc.txt.)  
>>      #takes the standard output of the command & appends  (left to right)
        <    <<     #to redirect right to left
|       #pipe.  command to command redirection.  
				#takes the standard output of the command on the left, and pipes it as standard input to the command on the right.  
				#ex.
				cat volcanoes.txt | wc | cat > islands.txt


 







# SCREEN SHARING -------------------------------------------------------

#Install xRDP
apt-get update
apt-get install xrdp
#Install XFCE4
apt-get install xfce4
#Configure xRDP
echo xfce4-session > ~/.xsession
nano /etc/xrdp/startwm.sh
#Restart xRDP
service xrdp restart









# NETWORK --------------------------------------------------------------

#get ip address
hostname -I
#get IPv4 and IPv6 addresses
ip addr show
#alt
ip a
#public ip
curl ifconfig.me
#
ip a | egrep "inet "














# APPS ----------------------------------------------------------------


#ubuntu software
install gnome-software
#snap-store
sudo snap install snap-store


#windows linux subsystem
#install
lxrun /install #from command prompt


#update local apt package cache
sudo apt-get update




#Terminal
clear #clears the terminal window, moving the command prompt to the top of the screen
source #activates the changes in ~/.bash_profile for the current session. Instead of closing the terminal and needing to start a new session    ex.  source ~/.bash_profile
exit




#remote desktop
#install
sudo apt update #update local apt package cache
sudo apt install ubuntu-desktop #gnome | or sudo apt install xubuntu-desktop #xfce
sudo apt install xrdp
sudo adduser xrdp ssl-cert
#restart
sudo systemctl restart xrdp
#status
sudo systemctl status xrdp


#net-tools
#install
sudo apt install net-tools
#
sudo netstat -lnp | grep redis



#redis
#connect to the server using Redis’s command-line client
redis-cli
#password (set: sudo nano /etc/redis/redis.conf '# requirepass your_redis_password')
auth your_redis_password #enter password
#config
sudo nano /etc/redis/redis.conf
#restart
sudo systemctl restart redis



#samba
#install
sudo apt install samba samba-common-bin
#add user to sambashare
sudo gpasswd -a <user> sambashare
#set samba user password
sudo smbpasswd -a <user>
#get version
smbd --version
#services
systemctl status smbd nmbd #check if service is running
sudo systemctl start smbd nmbd #start services
#samba share config
sudo nano /etc/samba/smb.conf
#retart
sudo service smbd restart
#reset widows share
net use \\<server>\<share> /delete


#firewall
#server profiles
sudo ufw app list
sudo ufw status verbose #get current state
less /etc/services #list services by name and port
sudo ufw status numbered #ex. sudo ufw delete 2
#config
sudo nano /etc/ufw/ufw.conf
#add rules
sudo ufw allow Apache #(Apache, Apache Full, Apache Secure, etc)
sudo ufw allow Samba
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow proto tcp from any to any port 80,443 #http|https
sudo ufw allow from 192.168.1.1/24 to any port 3389 proto tcp #remote desktop (xrdp)
#network interface
sudo ufw allow in on eth0 to any port 80
#port ranges
sudo ufw allow 6000:6007/tcp
sudo ufw allow 6000:6007/udp
#ip
sudo ufw allow from 203.0.113.4
sudo ufw allow from 203.0.113.0/24 #subnet
sudo ufw allow from 203.0.113.4 to any port 22 #specific port
#remove rules
sudo ufw delete allow 22/tcp
#block port
sudo ufw deny http
#state
sudo ufw disable
sudo ufw enable
sudo ufw reload
#
sudo ufw reset #disable UFW and delete any rules that were previously defined.
sudo ufw default allow outgoing
sudo ufw default deny incoming



#apache
sudo systemctl stop apache2      #stop apache2
sudo systemctl start apache2     #start apache2
sudo systemctl restart apache2   #restart apache2 #sudo service apache2 restart #sudo /etc/init.d/apache2 restart
sudo systemctl reload apache2    #reload apache2 #sudo service apache2 reload
sudo systemctl disable apache2   #disable apache2
sudo systemctl enable apache2    #enable apache2
#config files
ls /etc/apache2/*
/etc/apache2/apache2.conf #The main Apache global configuration file, that includes all other configuration files.
/etc/apache2/conf-available #stores available configurations.
/etc/apache2/conf-enabled #contains enabled configurations.
/etc/apache2/mods-available #contains available modules.
/etc/apache2/mods-enabled #contains enabled modules.
/etc/apache2/sites-available #contains configuration file for available sites (virtual hosts).
/etc/apache2/sites-enabled #contains configuration file for enabled sites (virtual hosts).
#enable|disable vitual host config
sudo a2ensite default-ssl.conf #enable host config
sudo a2dissite default-ssl.conf #disable host config



#nautilus
#open file explorer as root
sudo -H nautilus
#enable|disable address bar
gsettings set org.gnome.nautilus.preferences always-use-location-entry true




#mariadb
sudo apt-get install mariadb-server mariadb-client #install MariaDB server
sudo mysql_secure_installation #allows; Setting a strong password for the root user of our MariaDB,remove anonymous usersdisallow root login andremove test databases

sudo mysql -u root -p #login to your MariaDB server and enter your password when prompted.

#create db
CREATE DATABASE owncloud; #Create OwnCloud database user and password by typing the commands below. Replace ‘PASSWORD’ with a strong value.
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL ON owncloud.* TO 'admin'@'localhost' IDENTIFIED BY 'your_password' WITH GRANT OPTION; 
FLUSH PRIVILEGES;
EXIT;

#open db
USE <database>;

#list
SHOW DATABASES;
SHOW TABLES;

#visualize
DESCRIBE <table>;




#php
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update #update local apt package cache
sudo apt install php7.4

sudo apt-get install php7.4-cli php7.4-common php7.4-mbstring php7.4-gd php7.4-intl php7.4-xml php7.4-mysql php7.4-zip php7.4-curl php7.4-xmlrpc #install related PHP modules

sudo nano /etc/php/7.4/apache2/php.ini #Open the default 'php.ini' amd adjust default PHP settings.
'''memory_limit = 256M
upload_max_file_size = 100M
'''
sudo apt update #update local apt package cache
sudo apt install php-smbclient #install smbclient




#owncloud
#install from zip
cd /tmp 
wget https://download.owncloud.org/community/owncloud-10.0.3.zip
unzip owncloud-10.0.3.zip
sudo mv owncloud /var/www/owncloud/
#Set directory and file permissions
sudo chown -R www-data:www-data /var/www/owncloud/
sudo chmod -R 755 /var/www/owncloud/


#manual update (https://memoriaferroviaria.rosana.unesp.br/pmf2/owncloud/core/doc/admin/maintenance/enable_maintenance.html#)
cd /var/www/owncloud #run it as your HTTP user to ensure that the correct permissions are maintained.
sudo -u www-data php occ maintenance:mode --on #maintenence mode
sudo service apache2 stop #stop the web server
sudo -u www-data php ./occ upgrade
sudo -u www-data php occ maintenance:mode --off #maintenence mode

#Create a file named owncloud.conf in this directory with the following contents:
cd /etc/apache2/sites-available/
'''Alias /owncloud "/var/www/owncloud/"

<Directory /var/www/owncloud/>
  Options +FollowSymlinks
  AllowOverride All

 <IfModule mod_dav.c>
  Dav off
 </IfModule>

 SetEnv HOME /var/www/owncloud
 SetEnv HTTP_HOME /var/www/owncloud

</Directory>
'''
sudo a2ensite owncloud #Enable the new configuration.
sudo a2enmod rewrite #enable an apache module needed for ownCloud.

#enable SSL using ubuntu self-signed cert
sudo a2enmod ssl
sudo a2ensite default-ssl
sudo service apache2 restart

#background jobs
sudo crontab -u www-data -e #edit background jobs
sudo crontab -u www-data -l #list background jobs
#tasks
sudo -u www-data php occ background:cron #set the schedular. schedulers: cron|ajax|webcron
sudo -u www-data php ./occ system:cron #manually run cron jobs.
sudo -u www-data php occ trashbin:expire #remove any file in the ownCloud trash bin which is older than the specified maximum file retention time.
sudo -u www-data php occ versions:expire #expire versions of files which are older than the specified maximum version retention time.
sudo -u www-data php occ dav:cleanup-chunks #clean up outdated chunks (uploaded files) more than a certain number of days old.
#add task to crontab
*  *  *  *  * /usr/bin/php -f /path/to/your/owncloud/occ versions:expire

#set strict Transport Security HTTP Header
sudo nano /etc/apache2/sites-available/default-ssl.conf
'''Header always add Strict-Transport-Security "max-age=15768000; includeSubDomains; preload"
''' #Add the following snippet of code to the SSL.conf

#configure APCu memory cache
sudo nano /var/www/owncloud/config/config.php
"""'memcache.local' => '\OC\Memcache\APCu',
""" #Add the following line of text to the config.php

#repair 423 locked db error (sudo mysql -u root -p; USE owncloud;) #log into mariadb.
truncate oc_file_locks
#or
DELETE FROM oc_file_locks WHERE 1





#certbot
#create auto-renew timer
sudo nano /etc/systemd/system/certbot-renewal.service
'''#Executes the certbot renew command and restarts the httpd service after the renewal process has completed.
[Unit]
Description=Certbot Renewal

[Service]
ExecStart=/usr/bin/certbot renew --post-hook "systemctl restart httpd"
'''

sudo nano /etc/systemd/system/certbot-renewal.timer
'''#Timer unit files contain information about a timer controlled and supervised by systemd.
#By default, a service with the same name as the timer is activated.
#The configuration will activate the service weekly, and 300 seconds after boot-up.

[Unit]
Description=Timer for Certbot Renewal

[Timer]
OnBootSec=300
OnUnitActiveSec=1w

[Install]
WantedBy=multi-user.target
'''

sudo systemctl start certbot-renewal.timer #start the timer.
sudo systemctl enable certbot-renewal.timer #enable the timer to be started on boot-up.
systemctl status certbot-renewal.timer #show status information for the timer
journalctl -u certbot-renewal.service #show journal entries for the timer.






#perforce server
#Add the Perforce packaging key to your APT keyring. For example,
wget -qO - https://package.perforce.com/perforce.pubkey | sudo apt-key add -
#Add the Perforce repository to your APT configuration.
sudo nano /etc/apt/sources.list.d/perforce.list #add the line: deb http://package.perforce.com/apt/ubuntu {distro} release (distro = the ubuntu version ie. focal).
#install helix p4d server
sudo apt-get update
Install the package by running sudo apt-get install helix-p4d
#configure p4d (as root):
sudo /opt/perforce/sbin/configure-helix-p4d.sh
#
sudo -u perforce p4dctl <cmd> 
#set the P4PORT and P4USER environment variables.
# export P4PORT=ssl:1666
export P4PORT=ssl:192.168.1.240:1666 #To connect to this p4d service from another machine, include this machine's name or IP address in the P4PORT
export P4USER=m3trik
#login
p4 login
#add fingerprint
p4 -p ssl:m3trik.com:1666 trust -i 5B:B7:7A:38:AB:9D:CC:36:8F:B7:E6:82:A3:45:E5:ED:FA:B1:03:61
#create user (no whitespace)
p4 user -f "<username>" #option(-i) takes input from the standard input instead of the forms editor. To quickly create a large number of users, write a script that reads user data, generates output in the format used by the p4 user form, and then pipes each generated form to p4 user -i -f.
#rename user
p4 renameuser



#delete a package
dpkg --list #determine a package name
sudo apt-get remove <packagename> && sudo apt-get autoremove #remove a program.
sudo apt-get --purge remove <packagename> #completely uninstall the app if you plan not to reinstall.

#Using aptitude (sudo apt-get install aptitude)
sudo aptitude remove <package> #automatically removes everything and provides an interactive command line interface.

#uninstall by keyword
# First, a list of packages is generated using this series of commands: dpkg -l | grep php| awk '{print $2}' |tr "\n" " ".
# Hint: You can run this part of the command in your terminal to see what packages would get removed. You should get something like: libapache2-mod-php5 php5 php5-cli php5-common php5-json
# Finally, when you run the full command, this list of packages gets passed to sudo apt-get purge, removing all of the packages.
sudo apt-get purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`
















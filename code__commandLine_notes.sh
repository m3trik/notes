# Unix command notes

# ---------------------------------------------------------
'help'

#keyboard shortcuts:
#autocomplete.  tab key twice to get all possible suggestions.

#history				up/down arrows to scroll through recent commands.
								#also:
								history #returns all history.  commands can be ussued by history index#


apropos			#list available commands relating to a keyword
						# ex.
						apropos time

which				#location of a command
						#ex.
						which command

whatis			#description of a command
						#ex.
						whatis command

man 				#manual for a command
						#ex.
						man command




# ---------------------------------------------------------
'directories & navigation'                                                       


~/.bash_profile		#file used to store enviromental settings
				~ #represents the user's home directory
        . #indicates a hidden file


cd      #change directory   
				#ex. 
				cd c:/
cd ..   #move up one directory  
				#ex.  
				cd ..  
				#or 
				cd ../../ #ect to move up two or more directories

				#external drives
				cd /mnt/<drive letter>

pushd		#change directorys with the ability to jump back to original using popd 
				pushd /ect #change directory to ect
				popd #go back to where you were previously


locate	#search
				locate fstab
				#manually update search database if search item is new or fresh install of linux. search db is auto-updated peridically.
				sudo updatedb

ls      #list directory (folder) contents
				#flags
				#[-a] lists all contents, including hidden files and directories 
				#[-l] lists all contents of a directory in long (table) format (table format: access rights, number of hard links, owner username, group, file size, last modified, name of file or dir)  
				#[-t] order files and directories by the time they were last modified.
				# ex.
				ls -a -t

pwd     #present working directory. print (name of) working directory (working directory = current dir)

mkdir   #create new directory (folder)  takes directory name as an argument 
				#ex. 
				mkdir newfolder additionalfolder 

touch   #create new file   takes file name & extension as an argument.
				#ex. 
				touch new text document.txt

cp      #copy file or directory (source file as the first argument and the destination directory as the second argument) 
				#ex.
				cp folder one/textdoc.txt destinationfolder    
				#or copy more than one file 
				#ex.  
				cp folder one/text doc one.txt folder/one text doc two.txt destunationfolder

				#copy the contents of a text file to another text file
				cp textFromThisFile.txt toThisFile.txt

 *      #wildcard for copy.  selects all files in directory    
 				#ex. 
 				cp * destinationfolder/
 				#or 
 				#ex.  
 				cp m*.txt destinationfolder/  #(m*.txt copies all files in the working directory starting with "m" and ending with ".txt")

mv      #move file or directory (source file as the first argument and the destination directory as the second argument) 
				#ex.
				mv folder one/textdoc.txt destinationfolder
				#or copy more than one file 
				#ex.
				mv folder one/text doc one.txt folder/one text doc two.txt destinationfolder

 *      #wildcard for move.  selects all files in directory
				#ex.
				mv * destinationfolder/
				#or
				#ex.
				mv m*.txt destinationfolder/  #(m*.txt moves all files in the working directory starting with "m" and ending with ".txt")

rm      #remove/ delete file or directory
				#flags
				# remove a directory
				#[-r] "recursive". delete a directory and all of its child directories.  
				#ex.
				rm -r directory
				# remove a file
				#ex.
				rm file.txt

*      #wildcard for remove. 
			 #used alone it removes all files in a directory.
			 #remove all files that start with specified string.
			 #ex.
			 rm fileName * #delete all files that start with 'fileName'


rmdir	#remove empty directories
			 #safe way to clean up all empty sub-directories in a directory
			 #ex.
			 remdir * 


ln		#create a hard link or a symbolic link (symlink) to an existing file or directory.
			#create a symbolic link
			ln -s `pwd`/django-trunk/django /path/to/python_site_packages/django




# ---------------------------------------------------------
'I/O redirection'


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


 



# ---------------------------------------------------------
'Variables'

#user assigned:
export variable="value"






#environment variables:
env 			#list current user environment variables
					# info on a single variable:
					# ex.
					env | grep PATH #prints info on the PATH variable

$PATH 		#returns a colon separated list of file paths.
$HOME 		#home directory

$USER 		#name of the current user


$PS1 			#prompt style
					#ex.
					export PS1=">> "


# ---------------------------------------------------------
'file editing'


nano    #simple text editor
        #commands:
        ^O #WriteOut     save file
        ^J #Justify
        ^R #Read File
        ^W #Where Is
        ^Y #Prev Page
        ^V #Next Page
        ^K #Cut Text
        ^U #UnCut Text
        ^C #Cur Pos
        ^T #TO Spell



# text
echo    #The echo command accepts the string "your string" as standard input, and echoes the string "your string" back to the terminal as standard output.   
cat     #concatenate. can be used to output the contents of a file to the terminal or vice versa.
				# ex.
				cat >> file #anything typed into the terminal will be added to 'file'

wc 			#outputs the number of lines, words, and characters in .txt file
sort    #sorts lines of text alphabetically.
uniq    #filter adjacent duplicate lines in a file (non-adjacent files are not filtered out, calling a 'sort' command then piping in the standard output to 'uniqu' will place all duplcates adjacent before filtering)

grep    #global regular expression print. searches for a text pattern and outputs it.
				#searches files for lines that match a pattern and returns the results.      
				#[-i] case insensitive. (default grep search is case sensitive)    
				#[-R] Recursive: check first element for key, return position if found, otherwise search the remaining elements of the array
				#[-l]  files with matches.
        #Iterative: start at one end, scanning the data for the value, and if found, stop and return the position.
        
sed     #stream editor. searches for a text pattern, modifies it, and outputs it. 
				#(find & replace) accepts input & modifies it based on an expression, before displaying it as output data.                 
				#ex.  
				sed 's/search string/replacement string/g'    
				#expressions: 's' stands for substitution  'g' meaning global

less		#scroll through text file using arrow keys. or search for keywords.
				#ex.
				less filename.txt
 





# ---------------------------------------------------------

'terminal'


$					#at prompt means, user is logged in as with standard (non-admin) privilages

clear 		#clear the terminal




#commands:
clear   #clears the terminal window, moving the command prompt to the top of the screen

source  #activates the changes in ~/.bash_profile for the current session. Instead of closing the terminal and needing to start a new session    ex.  source ~/.bash_profile






















# install notes

#on windows
lxrun /install #from command line



# change home folder permissions:
chmod 0755 /home/m3trik
chmod 0644 /home/m3trik/.bashrc
chmod 0644 /home/m3trik/.profile
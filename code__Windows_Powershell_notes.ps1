Powershell notes----------------------
exit #prevent executing this file as a script.





# COMMENTING -------------------------
#single line

<# multi-
	line #>





# DIRECTORIES & NAVIGATION -----------


#make a folder case sensitive
fsutil.exe file setCaseSensitiveInfo "C:\my folder" enable #doesn't affect subfolders.
#recursive
(Get-ChildItem "<dir>" -recurse -directory).FullName | ForEach-Object {fsutil.exe file setCaseSensitiveInfo $_ enable}


# un-block only the contents of a single folder:
#get-childitem "full path of folder" | unblock-file -confirm
#recursive
cd O:\Cloud #
get-childitem "<dir>" -recurse | unblock-file -confirm #get-childitem "full path of folder" -recurse | unblock-file -confirm








# EDITOR -----------------------------
change remote script execution policy:
Set-ExecutionPolicy RemoteSigned
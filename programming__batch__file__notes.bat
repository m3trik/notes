﻿@ECHO OFF
EXIT




::	command reference A-Z: https://technet.microsoft.com/en-us/library/bb490890.aspx
:: get help on a command: ex. command /?


:: general syntax ---------------------------
:: print statement
ECHO.	print blank line
ECHO	print


:: commenting
REM comment
:: comment


:: escape characters
%%
^

:: ignoring whitespace
:: use quotes around entire command,
"C:\Program Files (x86)\WinRar\Rar.exe"
::  or quotes around areas with whitespace
C:\"Program Files (x86)"\WinRar\Rar.exe
:: alternatively, use command:
dir /X ~1 c:\
:: to print a list of alternative dir names.  eg:
DEFAUL~1.XML Default Desktop Policy.xml
PROGRA~1     Program Files 
PROGRA~2     Program Files (x86)



::set tab variable to visably show tab space
set "TAB=	"
echo %TAB%if not tk.isVisible(^): tk.show(^)





GOTO
::(spaces allowed but not other separators (semicolons,equal signs). Uses only the first eight characters)
go to :exit

:exit
CLS	#clears the screen



BREAK=ON	:: stop if the user presses < Ctrl >-< Break >
BREAK=OFF	:: continue until done









:: operands ---------------------------------

*multiply		:: ex. set /a sum1="num1 * num2"










:: variables --------------------------------

:: **the space before and after = is interpreted as part of the value.
:: variable=value   not varible = value unless a whitespace before the value is intended

:: assign variable:
set "variable=.proj"

:: assign empty variable:
set variable=

:: prompt user assigned
set /p variable= Printed text prompt string

:: expression result as variable
set /a variable=expression 

:: call variable:
%variable%



:: Windows environment variables:

%userprofile%	=C:\Users\<username>
%systemroot%	=C:WINDOWS
%temp% or %tmp%	=%USERPROFILE%\AppData\Local\Temp
%username%	=<username>
%homedrive%	=C:
%homepath%	=\Users\<username>
%systemdrive%	=C:
%public%	=C:Users\Public
%appdata%	=C:Users\<username>\AppData\Roaming
%localappdata%	=C:Users\<username>\AppData\Local
%programdata%	=C:ProgramData
%programfiles%	=C:Program Files
%programfiles(x86)%
%computername%









:: strings ----------------------------------

:: concatenate:
set combinedString= str1 str2 str3





:: strip chars (in this case '!')
set string=%string:!=%


:: strip trailing backslash by redefining 'var'
IF %var:~-1%==\ SET var=%var:~0,-1%
:: alt: check if there IS a backslash on the end: 
IF NOT "%var:~-1%"=="\" SET "var=%var%\"
:: alt: if 'var' contains whitespaces:
IF "%var:~-2,-1%"=="\" SET var="%var:~1,-2%"


:: strip multiple chars (from 1.2.3.4 to 1,2,3,4) 
setlocal 
set string=1.2.3.4 
set string=%string:.=,%








:: conditionals -----------------------------

:: if statement:
if %choice%==[%1]==[] goto start
if /i %choice%==one goto one
if /i %choice%==two goto two
if /i %choice%==end goto end


:: if/else:
if not exist %object% (
	:: do something
) else (
	:: do something else
)







directory navigation -------------------------

:: change directory
CD %dir%
:: alt:
CHDIR %dir%
:: change directory and drive
CD /d %dir%

:: current file location
%~dp0

:: current file location w/filename
%~f0

:: set path two levels up
for %%a in ("%~dp0..\..") do set "PATH_TWO_LEVELS_UP=%%~fa"
echo %PATH_TWO_LEVELS_UP%
:: alt:
..\..\bin\file.txt







:: external files ---------------------------

:: check if file exists
if exist file.txt


:: create and write single line to file:
echo some text > file.txt


:: write multiple lines to a file:
(
echo line of text
echo.
echo another line
echo escape char(^)
)> file.txt



:: rename a file



:: create juction to directory
mklink /J "%JUNC%" "%DIR%"

:: create symbolic link to a file
mklink "%SYM%" "%DIR%\file.ini"



:: zip a file
compact /c /s:C:\Templates

:: using java:
:: c = Creates a new archive file.
:: M = Specifies that a manifest file should not be added to the archive.
:: f = Indicates target file name.
jar -cMf targetArchive.zip sourceDirectory

:: using powershell:
:: compress
Compress-Archive -Path C:\Test -DestinationPath C:\result
:: expand
Expand-Archive -Path result.zip -DestinationPath C:\Test
:: from batch file
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('foo.zip', 'bar'); }"

:: convert to cab:
makecab <source> <dest>.cab
:: to decompress
expand <source>.cab <dest>
:: example: Create a self extracting archive containing movie.mov:
C:\> makecab movie.mov "temp.cab"
C:\> copy /b "%windir%\system32\extrac32.exe"+"temp.cab" "movie.exe"
C:\> del /q /f "temp.cab"

:: using 7zip:
"C:\Program Files\7-Zip\7z.exe" a  -r myzip.zip -w foo -mem=AES256
:: unzip to current directory ./
"C:\Program Files\7-Zip\7z.exe" x  myzip.zip  -o./ -y -r

:: using WinRar:
:: 'a' command. Adds to the archive
:: '-r'  switch. recursively archive/compress all files and subdirectories
:: '-ep' switch. Adds files to the archive without including the path information. Multiple can exist in the archive with the same name.
:: '-u' switch. Equivalent to the “u” command when combined with the “a” command. Adds new files and updates older versions of the files already in the archive'
:: '-df' switch. Deletes files after they are moved to the archive
:: '-x' switch. Excludes the specified files from the operation
:: '-idq' enable quiet mode to display only error messages
:: '-ep1' exclude base directory from specified file/folder names
:: '-y' assume Yes on all queries
"%ProgramFiles%\WinRAR\Rar.exe" a -r -y -df "%dir%\%file%.rar" "%dir%\%file%"
:: extract to current dir
:: 'x' command. Extracts with full paths
:: 'e' command. Extracts and ignores paths
if exist "%dir%\%file%.rar" "%ProgramFiles%\WinRAR\Rar.exe" x -y "%dir%\%file%.rar"
:: or to perform an operation on only certain files: 
:: extracts *.gif files from yourfile.rar to c:\extractfolder\ -trailing backslash required:
"%ProgramFiles%\WinRAR\Rar.exe" x c:\yourfile.rar *.gif c:\extractfolder\





:: reg keys ---------------------------------

:: delete key
reg delete "HKCU\Some\Registry\Path" /f
:: alt:
[-HKEY_LOCAL_MACHINE\SOFTWARE\YourSoft\MyKey]
:: to remove an entry, place a minus "-" after the = char
[HKEY_LOCAL_MACHINE\SOFTWARE\YourSoft\MyKey]
"MyEntry"=-







:: time -------------------------------------

PAUSE				:: stop execution of the batch file until someone presses a key, then continue.

SLEEP				:: ex. SLEEP 10 (In seconds)

TIMEOUT			:: ex. TIMEOUT 10 or TIMEOUT /t 10 (in seconds). If the user does press a key at any point, execution will resume immediately.








:: errors -----------------------------------

:: error: XXXX is not regognized as an internal or external command
:: solution: check if a system variable ie. %path% has been redefined.





EXIT
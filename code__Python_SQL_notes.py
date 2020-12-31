# Python SQL notes ____________________________________________






' OPERATORS ___________________________________________________'

# mathematical
+
-
*
/
%
<<
>>
&
|

# comparators
=
==
<
<=
>
>=
!=
IN
NOT IN
BETWEEN
IS
IS NOT






' DATA TYPES __________________________________________________'

# storage classes:
NULL 		#The value is a NULL value.
INTEGER 	#The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
REAL 		#The value is a floating point value, stored as an 8-byte IEEE floating point number.
TEXT 		#The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
BLOB 		#The value is a blob of data, stored exactly as it was input.

# boolean:
#Boolean values are stored as integers 0 (false) and 1 (true).

# date & time
TEXT 		#as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
REAL 		#as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
INTEGER 	#as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.






' SYNTAX ______________________________________________________'

# Creating an SQLite database:
conn = sqlite3.connect(<file>) #<file> can be an absolute path, a filename (use current working directory), or ':memory:' (database in RAM).
cur = conn.cursor()


#tables
#SQLITE_MASTER: (table that defines the schema for the database)
CREATE TABLE sqlite_master (
  type TEXT,
  name TEXT,
  tbl_name TEXT,
  rootpage INTEGER,
  sql TEXT
);

# Get table names:
tableNames = '''
	SELECT name FROM sqlite_master
	WHERE type='table'
	ORDER BY name;
	'''

# Create table:
table = '''
	CREATE TABLE <table> (
		<column1> <datatype>,
		<column2> <datatype>,
	);'''
#
table = '''
	CREATE TABLE IF NOT EXISTS projects (
		id integer PRIMARY KEY,
		name text NOT NULL,
		begin_date text,
		end_date text
	);'''
<cur>.execute(table)



# Insert data:
sql = '''
	INSERT INTO projects (name,begin_date,end_date) #INSERT INTO <table> (<columns>)
	VALUES ("SQLite App", "2015-01-01", "2015-01-30") #VALUES (<values>);
	'''
<cur>.execute(sql)
<conn>.commit()

#insert using use (?) as a placeholder for each argument.
sql = '''
	INSERT INTO projects (name,begin_date,end_date) #INSERT INTO <table> (<columns>)
	VALUES (?,?,?) #VALUES ("values");
	'''
project = ('SQLite App', '2015-01-01', '2015-01-30');
<cur>.execute(sql, project)
<conn>.commit()



# Update data:
sql = '''
	UPDATE tasks #UPDATE <table>
	SET priority = 2 , #SET <column> = <value>
		begin_date = '2015-01-04' ,
		end_date = '2015-01-06'
	WHERE id = 2 #WHERE id = <row id>
	'''
<cur>.execute(sql)
<conn>.commit()

#update using use (?) as a placeholder for each argument.
sql = '''
	UPDATE tasks #UPDATE <table>
	SET priority = ? , #SET <column> = <value>
		begin_date = ? ,
		end_date = ?
	WHERE id = ? #WHERE id = <row id>
	'''
task = (2, '2015-01-04', '2015-01-06', 2)
<cur>.execute(sql, task)
<conn>.commit()



#join
<cur>.execute("SELECT <column> FROM <table1> JOIN <table2> ON <table1>.<column> <comparator> <table2>.<column>") #sql comparators: =, >, <, >=, <=, <>


#union
<cur>.execute("SELECT <columns> FROM <table1> UNION SELECT <columns> FROM <table2> #column names and data type must match")


#group
<cur>.execute("SELECT <columns> FROM <table> GROUP BY <column>")



# Selecting data:
# SELECT <column> FROM <table> WHERE <column> <comparator> <value> #ie. WHERE column1 <> Dark Red
<cur>.execute("SELECT * FROM <table>")
#by priority
<cur>.execute("SELECT * FROM <table> WHERE priority=1")
#select using use ? as a placeholder for each argument.
<cur>.execute("SELECT * FROM <table> WHERE priority=?", (priority,))



# query data:
[row for row in <cur>] #rows are read only as needed.
[row for row in <cur>.fetchall()] #returns a list of all the elements remaining in the initial query (all elements if you haven't selected anything).


# Delete table:
sql = 'DROP TABLE <table>;' #DROP TABLE database_name.table_name;
<cur>.execute(sql)
<conn>.commit()
# Delete row:
sql = 'DELETE FROM <table>'
<cur>.execute(sql)
<conn>.commit()
#delete using use ? as a placeholder for each argument.
sql = 'DELETE FROM <table> WHERE id=?'
<cur>.execute(sql, (id,))
<conn>.commit()






' COMMAND LINE ________________________________________________'
#sqlite3 tool is a terminal based frontend to the SQLite library

#hotkeys
Ctrl+D 		#quit
Ctrl+L 		#clear
Ctrl+U 		#clear current line


#launch sqlite:
sqlite3

#show all available commands:
.help

#history
#.sqlite_history file. archived commands. (located in the home directory)
$ tail -5 ~/.sqlite_history #Using the tail command, we show the last five entries.

#resource file
#.sqliterc. The resouce file can contain meta commands, or regular SQL statements. However, we should avoid using SQL in the file. (located in the home directory. If it doesnt exist, simply create it)
$ cat .sqliterc 
.mode column
.headers on
.nullvalue NULL 


#prompt
#set the prompt style:
.prompt "> " ". " 
#line continuation:
#the default continuation prompt is ...>
#close line continuation with a semi-colon ";".


#connect
<absolute path>/<database>.db #creates a database if it does not already exist.
#
.open <absolute path>/<database>.db #if the database does not exist, a new one will be created.


#format the output:
#
.show			#lists current settings.
#set the output formatting style
.mode column

.separator :	#the default separator is |
.header on
.width 15 18	#<first column> <second>. (column mode only)


#query the currently connected database
.database 


#Tables
#show the name of every table inside the database.
.tables #shows the available tables.
#only those matching a conditon:
.table '%es' #returns the table that ends with the string 'es'.
#display all the tables in the current database:
SELECT * FROM sqlite_master; #the SQLITE_MASTER table defines the schema for the database.
#all tables with the given column
SELECT <column> FROM sqlite_master WHERE type='table';

#display the structure of a table
.schema #show the structures of all tables.
.schema <table> #show the structure of a given table.
.schema %es #show indexes of the tables whose names end with 'es'.
.fullschema #show the schema and the content of the sqlite_stat tables.

#display data from a table
SELECT * FROM <table>;

#show all indexes
.indexes
.indexes <table> #show the indexes of a specific table.
.indexes %es #show indexes of the tables whose names end with 'es'.


#save the result of a query into a file:
.output file.txt #all the results of the subsequent queries will be saved to the file.
SELECT title FROM <table>; #select the title from the albums table and write the result to the albums.txt file.
.once file.txt #save the result of the next single query only to the file
SELECT title FROM <table>; #select the title from the albums table and write the result to the albums.txt file.
#dump tables in SQL format to the disk:
.output <filename>.sql
.dump <table>
#redirect to an existing file.
$ cat <filename>.sql #We show the contents of the cars2.sql file with the cat command.

#read from a file:
.read <filename>.sql

#execute SQL statements from a file
.mode column
.header on
.read c:/sqlite/commands.txt #To execute the SQL statements in the commands.txt file, you use the .read <FILENAME> command (with optional formatting)

#
.quit

#exit the sqlite3 program
.exit

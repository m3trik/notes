# Python SQL notes ____________________________________________






# Creating an SQLite database:
conn = sqlite3.connect(<file>) #<file> can be an absolute path, a filename (use current working directory), or ':memory:' (database in RAM).
cur = conn.cursor()


#tables _______________________________________________________

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



# Delete row:
sql = 'DELETE FROM <table>'
<cur>.execute(sql)
<conn>.commit()
#delete using use ? as a placeholder for each argument.
sql = 'DELETE FROM <table> WHERE id=?'
<cur>.execute(sql, (id,))
<conn>.commit()






# COMMAND LINE ________________________________________________


#Connection
#launch sqlite:
sqlite3

#show all available commands:
.help

#connect to a database:
.open #O:\Cloud\_Code\SQL\_editor\database\pythonsqlite.db #if the database does not exist, a new one will be created.

#query the currently connected database
.database 

#add an additional database in the current connection
ATTACH DATABASE "c:\sqlite\db\chinook.db" AS chinook;


#Tables
#display all the tables in the current database:
SELECT * FROM sqlite_master; #the SQLITE_MASTER table defines the schema for the database.
SELECT <table> FROM sqlite_master WHERE type='table'; #
.tables #show the name of every table inside the database.
#only those matching a conditon:
.table '%es' #returns the table that ends with the string 'es'.
#format the output:
.header on
.mode column

#display the structure of a table
.schema #show the structures of all the tables.
.schema <table> #show the structure of a given table.
.schema %es #show indexes of the tables whose names end with 'es'.
.fullschema #show the schema and the content of the sqlite_stat tables.

#show all indexes
.indexes
.indexes <table> #show the indexes of a specific table.
.indexes %es #show indexes of the tables whose names end with 'es'.

#display data from a table
SELECT * FROM <table>;

#save the result of a query into a file
.output file.txt #all the results of the subsequent queries will be saved to the file.
SELECT title FROM <table>; #select the title from the albums table and write the result to the albums.txt file.
.once file.txt #save the result of the next single query only to the file
SELECT title FROM <table>; #select the title from the albums table and write the result to the albums.txt file.

#execute SQL statements from a file
.mode column
.header on
.read c:/sqlite/commands.txt #To execute the SQL statements in the commands.txt file, you use the .read <FILENAME> command (with optional formatting)




#exit the sqlite3 program
.exit

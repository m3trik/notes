# SQL notes ____________________________________________






# Comparison Operators
=		#Equal to
>		#Greater than	
<		#Less than	
>=		#Greater than or equal to	
<=		#Less than or equal to	
<>		#Not equal to

# Compound Operators
+=		#Add equals
-=		#Subtract equals
*=		#Multiply equals
/=		#Divide equals
%=		#Modulo equals
&=		#Bitwise AND equals
^-=		#Bitwise exclusive equals
|*=		#Bitwise OR equals

# Logical Operators
ALL		#TRUE if all of the subquery values meet the condition	
AND		#TRUE if all the conditions separated by AND is TRUE	
ANY		#TRUE if any of the subquery values meet the condition	
BETWEEN	#TRUE if the operand is within the range of comparisons	
EXISTS	#TRUE if the subquery returns one or more records	
IN		#TRUE if the operand is equal to one of a list of expressions	
LIKE	#TRUE if the operand matches a pattern	
NOT		#Displays a record if the condition(s) is NOT TRUE	
OR		#TRUE if any of the conditions separated by OR is TRUE	
SOME	#TRUE if any of the subquery values meet the

# Mathmatical Operators:
sum(<columns>) as var
max(< >) as var

# Bitwise Operators
&		#Bitwise AND
|		#Bitwise OR
^		#Bitwise exclusive OR



#select
Select <column> From <table> Where <column> <comparator> <value> #ie. Where column1 <> Dark Red


#join
Select <column> From <table1> Join <table2> On <table1>.<column> <comparator> <table2>.<column>

#left join
Select <columns> From <table1> Left Join <table2> On <table1>.<column> = <table1>.<column>

#union
Select <columns> From <table1> Union Select <columns> From <table2> #column names and data type must match.


#group
Select <column> <column operation> From <table> Group By <column>






# Creating an SQLite database:
CREATE DATABASE IF (
)


# Create tables:
CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	begin_date text,
	end_date text
);

CREATE TABLE IF NOT EXISTS tasks (
	id integer PRIMARY KEY,
	name text NOT NULL,
	priority integer,
	status_id integer NOT NULL,
	project_id integer NOT NULL,
	begin_date text NOT NULL,
	end_date text NOT NULL,
	FOREIGN KEY (project_id) REFERENCES projects (id)
);

# Inserting data into the SQLite database:



# Updating data in the SQLite database:



# Selecting data: 



# query data:


#Delete column
ALTER TABLE <table> DROP COLUMN <column>






# COMMAND LINE -----------------------------------------------

#Connection
#launch sql:


#show all available commands:


#connect to a database:


#show the currently connected database


#add an additional database in the current connection



#Tables
#display all the tables in the current database:

#format the output:

#display the structure of a table

#show all indexes


#query data from a table


#save the result of a query into a file


#execute SQL statements from a file




#exit the sqlite3 program

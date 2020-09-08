# Python SQL notes ____________________________________________





#select
# Select <column> From <table> Where <column> <comparator> <value> #ie. Where column1 <> Dark Red


#join
# Select <column> From <table1> Join <table2> On <table1>.<column> <comparator> <table2>.<column>


#union
# Select <columns> From <table1> Union Select <columns> From <table2> #column names and data type must match.


#group
# Select <columns> From <table> Group By <column>


# sum(<columns>) as var




# Creating an SQLite database:
# <file> can be an absolute path, a filename (use current working directory), or ':memory:' (database in RAM).
connection = sqlite3.connect(<file>)


# Create tables in SQLite database:



# Inserting data into the SQLite database:



# Updating data in the SQLite database:



# Selecting data: 



# query data:



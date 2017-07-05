import sqlite3 as lite
import json


DEBUG = True
db_file = 'landings_data.db'    # name of the database file
landings_data_table = 'LandingsData'   # name of the table to be queried
name_column = 'name'
some_name = ''
id_column = 'is'
mass_column = 'mass'
year_column = 'year'
# Connecting to the database file
conn = sqlite3.connect(db_file)
c = conn.cursor()

# Check if a certain name exists and print its column contents
c.execute("SELECT * FROM {tn} WHERE {idf} LIKE '{my_id}'".\
       format(tn=landings_data_table, cn=id, idf=name_column, my_id=some_name))
name_exists = c.fetchone()
if name_exists:
    print('{}'.format(name_exists))
else:
    print('{} does not exist.'.format(some_name))

# Closing the connection to the database file
conn.close()
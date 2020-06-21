# an script to select from database using sqlalchemy
# with a where caluse and

# from census data we want to get all states and pop2000
# where states is one the states in the list
# ['New York', 'California', 'Texas']


# import packages
from sqlalchemy import create_engine, MetaData, Table, select
from paths import *

# get connection string and create engine
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)

# create a metadata object
metadata = MetaData()

# create a Table object to reflect the census table
# from census SQLite database
census = Table('census', metadata, autoload=True, autoload_with=engine)

# define a connection
connection = engine.connect()

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)

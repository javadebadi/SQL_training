# an example of count recored with group by in sqlalchemy
# import packages
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, func
from paths import *

# create engine and connection to database
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)
connection = engine.connect()

# create metadata
metadata = MetaData()

# reflect census table
census = Table('census', metadata, auto_load=True, autoload_with=engine)

# create select statement with aggregate function
# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())

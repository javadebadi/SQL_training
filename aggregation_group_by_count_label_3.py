# an example of count recored with group by in sqlalchemy
# and label the result of aggregation with new name instead
# of alchemys default name
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
# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
# compare the result of below code with previous script
print(results[0].keys())

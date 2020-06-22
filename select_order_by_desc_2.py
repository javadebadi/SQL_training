# example of select and order by results in sqlalchemy
# an in addition order by descending order
# import packages
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, desc
from paths import *

# read data base with engine
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)

# create a MetaData object
metadata = MetaData()

# reflect census table
census = Table('census', metadata, autoload=True, autoload_with=engine)

# create a connection
connection = engine.connect()

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])

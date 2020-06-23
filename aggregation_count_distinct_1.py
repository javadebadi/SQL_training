# count number of distinct states in census table from census database
# import packages
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, func
from paths import *

# create engine and connection
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)
connection = engine.connect()

# create a metadata objec
metadata = MetaData()

# reflect table
census = Table("census", metadata, auto_load=True, autoload_with=engine)

# select statement with aggreation
# count distinct states
# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)

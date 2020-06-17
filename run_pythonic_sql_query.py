from sqlalchemy import create_engine, MetaData, Table
from paths import *
# Import select
from sqlalchemy import select

# create engine
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)

# create a MetaData object
metadata = MetaData()

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# create connection to engine
connection = engine.connect()

# Pythonic SQL: Build select statement for census table: stmt
stmt = select([census])
# Print the emitted statement to see the SQL string
print(stmt)

# get result proxy by executing sql qurey on database
result_proxy = connection.execute(stmt)

# fetch 10 records: result_set
result_set = result_proxy.fetchmany(size=10)

# print result_set
print(result_set)

# Get the first row of the results by using an index: first_row
first_row = result_set[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])

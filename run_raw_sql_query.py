from sqlalchemy import create_engine, MetaData, Table
from paths import *

# create engine
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)

# create connection to engine
connection = engine.connect()

# build SQL statement
stmt = "SELECT * FROM census"

# get result proxy by executing sql qurey on database
result_proxy = connection.execute(stmt)

# get results set
result_set = result_proxy.fetchall()

# print result_set
print(result_set)

# Import create_engine, MetaData, Table
# the MetaData object will be filled with metadata of a table
# the Table object will get the metadata of a table from database
from sqlalchemy import create_engine, MetaData, Table
from paths import *

# path to databases location in windows
driver_database_name = "sqlite:///"
db_name = "census.sqlite"
connection_string = driver_database_name + path_to_SQLite_dbs + db_name

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine(connection_string)

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)


# Print table names and information about table
print("Database: {}".format(db_name))
print("Tables in the database:")
print(engine.table_names())



# Print census table metadata
print("Print metadata:")
print(repr(census))

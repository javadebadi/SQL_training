# Import create_engine, MetaData, Table
# the MetaData object will be filled with metadata of a table
# the Table object will get the metadata of a table from database
from sqlalchemy import create_engine, MetaData, Table

# path to databases location in windows
driver_database_name = "sqlite:///"
path_to_dbs = "C:\\Users\\Javad\\github\\SQL_training\\databases\\"
db_name = "census.sqlite"
connection_string = driver_database_name + path_to_dbs + db_name

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


# print columns names
print("columns names : {}".format(census.columns.keys()))

# print metadata with another method (using Metadata attributes)
print("Print metadata with antoher method: ")
print(repr(metadata.tables['census']))

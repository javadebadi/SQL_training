# Import create_engine
from sqlalchemy import create_engine
from paths import *

# path to databases location in windows
driver_database_name = "sqlite:///"
db_name = "census.sqlite"
connection_string = driver_database_name + path_to_SQLite_dbs + db_name

# Create an engine that connects to the census.sqlite file: engine
print("Database: {}".format(db_name))
print("Tables in the database:")
engine = create_engine(connection_string)

# Print table names
print(engine.table_names())

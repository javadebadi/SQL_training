# an script which shows how to insert values in table
# import packages
from paths import *
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, insert

# create engine
connection_string = get_connection_string("new_db.sqlite")
engine = create_engine(connection_string)

# create a meatadata object
metadata = MetaData()

# reflect table
new_data = Table("new_data", metadata, autoload=True, autoload_with=engine)

# create connection
connection = engine.connect()

# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': False},
    {'name': 'Taylor', 'count': 2, 'amount': 750.00, 'valid': False}
]

# Build an insert statement
insert_stmt = insert(new_data)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt, values_list)

# Print result rowcount
print(results.rowcount)

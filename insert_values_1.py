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

# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(new_data).values(name='Haleh', count=1, amount=1000.00, valid=True)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert: select_stmt
select_stmt = select([new_data]).where(new_data.columns.name == "Haleh")

# Print the result of executing the query.
print(connection.execute(select_stmt).first())

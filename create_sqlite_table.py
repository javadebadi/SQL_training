from paths import *
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# get connection string
connection_string = get_connection_string("new_db.sqlite")
# create engine
engine = create_engine(connection_string)

# create metadata objec
metadata = MetaData()

# Define a new table with a name, count, amount, and valid column: data
new_data = Table('new_data', metadata,
            Column('name', String(255), unique=True),
            Column('count', Integer(), default=1),
            Column('amount', Float()),
            Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(new_data))

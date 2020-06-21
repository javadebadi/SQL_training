# an script to select from database using sqlalchemy
# with a where caluse and

# from census data we want to get all age and sex
# where states is 'California' and sex is not male 'M'

# We need to import and_() function from sqlalchemy to do this
# sqlalchemy has other sql operators such as or_()


# import packages
from sqlalchemy import create_engine, MetaData, Table, select
from paths import *

# Import and_
from sqlalchemy import and_


# get connection string and create engine
connection_string = get_connection_string("census.sqlite")
engine = create_engine(connection_string)

# create a metadata object
metadata = MetaData()

# create a Table object to reflect the census table
# from census SQLite database
census = Table('census', metadata, autoload=True, autoload_with=engine)

# define a connection
connection = engine.connect()

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)

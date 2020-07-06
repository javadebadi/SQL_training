# import packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from paths import *

# create engine
connection_string = get_connection_string("new_db.sqlite")
engine = create_engine(connection_string)
if not database_exists(engine.url):
    create_database(engine.url)

print(engine.url)
print(database_exists(engine.url))

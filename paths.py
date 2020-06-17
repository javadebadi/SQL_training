path_to_dbs = "C:\\Users\\Javad\\github\\SQL_training\\databases\\"
path_to_SQLite_dbs = path_to_dbs + "SQLite\\"
path_to_MySQL_dbs = path_to_dbs + "MySQL\\"

SQLite_driver_database_name = "sqlite:///"
MySQL_driver_database_name = "mysql:///"

SQLite_db_extension = ".sqlite"
MySQL_db_extension = ".mysql"

def get_SQLite_connection_string(db_name):
    return SQLite_driver_database_name + path_to_SQLite_dbs + db_name + SQLite_db_extension

def get_MySQL_connection_string(db_name):
    return MySQL_driver_database_name + path_to_MySQL_dbs + db_name + MySQL_db_extension

def get_connection_string(db_name_with_extension = "census.sqlite"):
    db_name = db_name_with_extension.split(".")[0]
    db_ext = "." + db_name_with_extension.split(".")[1]
    if db_ext == SQLite_db_extension:
        return get_SQLite_connection_string(db_name)
    elif db_ext == MySQL_db_extension:
        return get_MySQL_connection_string(db_name)
        

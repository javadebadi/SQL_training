# SQL training
## Using MySQL
Author: Javad Ebadi      
Website: https://www.datacademia.com      
Email: javad.ebadi.1990@gmail.com      
Data: June, 2020

Download MySQL installer for your operating system from [here](https://dev.mysql.com/downloads). Make sure to install MySQL serever, MySQL workbench and MySQL documentation if you choose custom installation.     
The examples in this repository are written and executed using **MySQL v8.0**.

# SQL Queries
- SELECT: keyword to do queries
- FROM: keyword to determine which entity is wanted to be queried
- LIMIT: limits the number of rows in output
  - LIMIT 5: show first 5 results
  - LIMIT 100, 5: shows first 5 result starting from result number 100
- WHERE: restricts queries
- INSERT INTO: inserts new row to tabel
  - INSERT INTOR table_1 (col_1, col_2) VALUES ('val_1', val_2);
- UPDATE: updates rows of existing table
  - UPDATE table_1 SET col_1 = 'val_1', col_2 = val_2 WHERE col_3 LIKE 'Java%';
- DELETE: delete rows from a table
  - DELETE * FROM table_1 WHERE col_1 = 2;
-

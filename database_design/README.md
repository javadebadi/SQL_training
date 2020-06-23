# Database Design

<a href="#data-processing-approaches">Data processing approaches</a>

<h2 id='data-processing-approaches'>Data processing approaches</h2>
Two approaches to processing data:

- OLTP (Online transaction processing):
  - In Online transaction processing (OLTP), information systems typically facilitate and manage transaction-oriented applications
  - system responds immediately to user requests
  - query focus is on `insert` and `update`
  - example:
    - ATM for a bank
  - example of task:
    - find price of a book in bookshop
    - update latest books which is sold
    - keep track of number of customers in regular time interval
- OLAP (Online analytical processing)
  - used for purpose of business analytics or reporting
  - all kind of queries such as `read`, `delete`, `insert`, `update`
  - mostly optimized for read only purposes
  - example of task:
    - find optimized price among books in a topic
    - find books which are sold most in each month
    - find the time period in which the number of customers is highest

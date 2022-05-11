### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

An Open Source relational database.

- What is the difference between SQL and PostgreSQL?

SQL server is a database management system which is mainly used for e-commerce and providing different data warehousing solutions. PostgreSQL is an advanced version of SQL which provides support to different functions of SQL like foreign keys, subqueries, triggers, and different user-defined types and functions.

- In `psql`, how do you connect to a database?

\c database name.

- What is the difference between `HAVING` and `WHERE`?

The main difference between them is that the WHERE clause is used to specify a condition for filtering records before any groupings are made, while the HAVING clause is used to specify a condition for filtering values from a group.

- What is the difference between an `INNER` and `OUTER` join?

The diffence between inner and outer joins is that inner joins result in the intersection of two tables, whereas outer joins result in the union of two tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

The difference between a left outer join and a right outer join is that in a left outer join it's the table in the FROM clause whose all rows are returned. Whereas, in the right outer join we are returning all the rows from the table specified in the join clause.

- What is an ORM? What do they do?

Object -reational mapper.  It is a code library that automates the transer of data stored in relational database tables into objects that are more commonly used in applicaton code.


- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

AJAX uses javascript to load data after the browser request has finished. Using HTTP requests using a library simply is used to tranfer data.

- What is CSRF? What is the purpose of the CSRF token?

 A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. The tokens are generated and submitted by the server-side application in a subsequent HTTP request made by the client. A CSRF secure application assigns a unique CSRF token for every user session. It's purpose is to keep communications in secrets.

- What is the purpose of `form.hidden_tag()`?

    The form.hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the FLASK configuration.

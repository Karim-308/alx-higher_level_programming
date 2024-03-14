# 0x0E. SQL - More queries

## Description
This project involves executing various SQL queries and tasks aimed at enhancing your skills in MySQL database management. It includes tasks such as creating users, managing privileges, understanding primary and foreign keys, utilizing constraints, retrieving data from multiple tables, working with subqueries, joins, and unions.

## Learning Objectives
By the end of this project, you should be able to:

- Create a new MySQL user
- Manage privileges for a user to a database or table
- Understand the concepts of PRIMARY KEY and FOREIGN KEY
- Use NOT NULL and UNIQUE constraints effectively
- Retrieve data from multiple tables in a single request
- Utilize subqueries, JOIN, and UNION operations

## Resources
To aid in completing this project, you can refer to the following resources:
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-adminsitration/mysql-grant-as-sql-command/)
- [MySQL constraints](https://www.mysqltutorial.org/mysql-constraints/)
- [SQL technique: subqueries](https://www.tutorialspoint.com/sql/sql-sub-queries.htm)
- [Basic query operation: the join](https://www.w3schools.com/sql/sql_join.asp)
- [SQL technique: multiple joins and the distinct keyword](https://www.geeksforgeeks.org/sql-join-query/)
- [SQL technique: join types](https://www.sqlshack.com/sql-joins-types-examples/)
- [SQL technique: union and minus](https://www.techonthenet.com/sql/union.php)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [The Seven Types of SQL Joins](https://www.sqlshack.com/sql-joins-types-examples/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Requirements
- Editors: vi, vim, emacs
- Operating System: Ubuntu 20.04 LTS
- MySQL Version: 8.0.25
- Files must end with a new line
- SQL queries should have a comment just before them
- File names should start with a comment describing the task
- All SQL keywords should be in uppercase
- Include a README.md file at the root of the project folder

## Installation
To install MySQL 8.0 on Ubuntu 20.04 LTS, follow these steps:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
````

## Usage
To connect to your MySQL server:

```bash
$ sudo mysql
```

## To start MySQL in a container-on-demand:

```bash
$ service mysql start
````
## To list databases:
```bash
$ cat 0-list_databases.sql | mysql -uroot -p
````

## To import a SQL dump:
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
````






--  a script that creates a table called first_table in the current database in your MySQL server.
-- Exceute: cat 4-first_table.sql | database_name -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

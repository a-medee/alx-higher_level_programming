-- a script that lists all rows of the table first_table from the
-- database hbtn_0c_0 in your MySQL server.

USE hbtn_0c_0;

table_name = $argv[1];

SELECT *
FROM first_table;

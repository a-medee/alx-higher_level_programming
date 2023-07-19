-- a script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server.

create_table_statement = SHOW CREATE TABLE table_name;

SELECT create_table_statement;

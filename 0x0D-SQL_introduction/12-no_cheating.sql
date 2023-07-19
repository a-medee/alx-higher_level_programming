-- This script updates the score of Bob to 10 in the table second_table
-- of the database hbtn_0c_0 in the MySQL server.
-- The database name will be passed as an argument of the mysql command

USE hbtn_0c_0;

database_name = $argv[1];

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

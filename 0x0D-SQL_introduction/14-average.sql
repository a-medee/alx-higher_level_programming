-- a script that computes the score average of all records in
-- the table second_table of the database hbtn_0c_0 in your MySQL server.

USE hbtn_0c_0;

database_name = $argv[1];

SELECT AVG(score) AS average
FROM second_table;

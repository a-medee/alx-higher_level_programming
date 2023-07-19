-- a script that lists all the tables of a database in your MySQL server.

USE mysql;
database_name = $argv[1];

SELECT table_name
FROM information_schema.tables
WHERE table_schema = database_name;

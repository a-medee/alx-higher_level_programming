-- Write a script that creates a table called first_table in
-- the current database in your MySQL server.
-- The database name will be passed as argument of mysql command.

CREATE TABLE IF NOT EXISTS `first_table`(
		`id` int,
		`name` varchar(256)
);

-- Write a script that creates a table called first_table in
-- the current database in your MySQL server.
-- The database name will be passed as argument of mysql command.

IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_name = 'first_table'
    AND table_schema = DATABASE()
)
THEN

CREATE TABLE first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);

END IF;

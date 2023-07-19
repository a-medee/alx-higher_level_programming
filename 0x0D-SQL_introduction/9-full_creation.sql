--  a script that creates a table second_table in the database
-- hbtn_0c_0 in  MySQL server and add multiples rows.

-- This script creates a table second_table in the database hbtn_0c_0
-- in MySQL server and adds multiple rows.
-- The database name will be passed as an argument to the mysql command.
-- If the table second_table already exists, the script should not fail.
-- You are not allowed to use the SELECT and SHOW statements.
-- the script should create these records:
--    id = 1, name = “John”, score = 10
--    id = 2, name = “Alex”, score = 3
--    id = 3, name = “Bob”, score = 14
--    id = 4, name = “George”, score = 8

IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_name = 'second_table'
    AND table_schema = DATABASE()
)
THEN


CREATE TABLE second_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
);


INSERT INTO second_table (name, score)
VALUES ('John', 10),
('Alex', 3),
('Bob', 14),
('George', 8);

END IF;

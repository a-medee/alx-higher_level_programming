-- a script that creates the table unique_id on  MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  name VARCHAR(256),
  PRIMARY KEY (id)
);

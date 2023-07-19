-- a script that creates the table force_name on  MySQL server.

CREATE TABLE IF NOT EXISTS force_name (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE force_name ALTER COLUMN name SET DEFAULT '';

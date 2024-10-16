-- Create a table users below attributes
-- id, integer, prime key
-- email, string (255 characters)
-- name, string (255 characters)
-- country, enum of countries
-- If tabble exists, script will not fail

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL
);
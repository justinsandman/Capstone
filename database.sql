--
CREATE DATABASE IF NOT EXISTS my_database;

--
USE my_database;

--
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL, 
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--
INSERT INTO users (username, email) VALUES
    ('Justin', 'justinsandstedt@gmail.com'); 


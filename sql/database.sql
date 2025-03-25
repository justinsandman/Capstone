-- Create a test database
CREATE DATABASE IF NOT EXISTS my_database;

-- Create a user and grant privileges
CREATE USER IF NOT EXISTS 'my_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';
FLUSH PRIVILEGES;

USE my_database;

-- CREATE THE USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    email VARCHAR(100) UNIQUE, 
    password_hash VARCHAR(255), 
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    account_created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activity_level ENUM('Sedentary', 'Lightly Active', 'Active', 'Very Active')
);

-- Insert test users first to ensure foreign key references are valid
INSERT IGNORE INTO users (first_name, last_name, email, password_hash, date_of_birth, gender, activity_level) VALUES
    ('Justin', 'Sandstedt', 'justinsandstedt@gmail.com', 'hashedpw', '2002-09-25', 'Male', 'Active'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'hashedpw2', '1995-06-15', 'Female', 'Lightly Active'),
    ('Bob', 'Smith', 'bob.smith@example.com', 'hashedpw3', '1988-03-22', 'Male', 'Sedentary');

-- CREATE THE ACTIVITY LOG TABLE
CREATE TABLE IF NOT EXISTS activity_log (
    activity_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT, 
    activity_type ENUM('Cardio', 'Strength', 'Stretching'),
    duration INT, -- duration in minutes
    calories_burned INT,
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- CREATE THE NUTRITION LOG TABLE 
CREATE TABLE IF NOT EXISTS nutrition_log (
    nutrition_log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    food_item VARCHAR(255), 
    calories INT,
    proteins INT, -- In grams
    carbs INT, -- In grams
    fats INT, -- In grams
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- CREATE THE LIFESTYLE LOG TABLE
CREATE TABLE IF NOT EXISTS lifestyle_log (
    lifestyle_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    log_type ENUM('Sleep', 'Water Intake'),
    value VARCHAR(50), -- Store sleep hours or water intake
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- CREATE THE GOAL TABLE 
CREATE TABLE IF NOT EXISTS goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_type ENUM('Weight Loss', 'Muscle Gain', 'Hydration'),
    target_value INT, 
    current_value INT, 
    deadline DATE, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);    

-- CREATE THE BUG TRACKING TABLE 
CREATE TABLE IF NOT EXISTS bug_tracking (
    bug_id INT AUTO_INCREMENT PRIMARY KEY,
    reported_by INT, -- user_id if user, or dev name/id
    description TEXT,
    severity ENUM('Low', 'Medium', 'High'),
    status ENUM('New', 'Assigned', 'Reproduced', 'Fixed', 'Tested', 'Closed'),
    date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_resolved TIMESTAMP,
    FOREIGN KEY (reported_by) REFERENCES users(user_id) ON DELETE SET NULL -- Assuming User is Reporter
);

-- CREATE THE SYSTEM LOG TABLE 
CREATE TABLE IF NOT EXISTS system_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    event_type ENUM('Performance Check', 'Security Audit'),
    event_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);

-- Insert test data into activity_log
INSERT INTO activity_log (user_id, activity_type, duration, calories_burned) VALUES
    ((SELECT user_id FROM users WHERE email = 'justinsandstedt@gmail.com'), 'Cardio', 30, 250),
    ((SELECT user_id FROM users WHERE email = 'alice.johnson@example.com'), 'Strength', 45, 300),
    ((SELECT user_id FROM users WHERE email = 'bob.smith@example.com'), 'Stretching', 20, 100);

-- Insert test data into nutrition_log
INSERT INTO nutrition_log (user_id, food_item, calories, proteins, carbs, fats) VALUES
    ((SELECT user_id FROM users WHERE email = 'justinsandstedt@gmail.com'), 'Chicken Breast', 200, 40, 0, 5),
    ((SELECT user_id FROM users WHERE email = 'alice.johnson@example.com'), 'Oatmeal', 150, 5, 27, 3),
    ((SELECT user_id FROM users WHERE email = 'bob.smith@example.com'), 'Avocado Toast', 250, 6, 30, 12);

-- Insert test data into lifestyle_log
INSERT INTO lifestyle_log (user_id, log_type, value) VALUES
    ((SELECT user_id FROM users WHERE email = 'justinsandstedt@gmail.com'), 'Sleep', '7 hours'),
    ((SELECT user_id FROM users WHERE email = 'alice.johnson@example.com'), 'Water Intake', '2 liters'),
    ((SELECT user_id FROM users WHERE email = 'bob.smith@example.com'), 'Sleep', '6 hours');

-- Insert test data into goals
INSERT INTO goals (user_id, goal_type, target_value, current_value, deadline) VALUES
    ((SELECT user_id FROM users WHERE email = 'justinsandstedt@gmail.com'), 'Weight Loss', 180, 200, '2025-06-01'),
    ((SELECT user_id FROM users WHERE email = 'alice.johnson@example.com'), 'Muscle Gain', 150, 140, '2025-09-01'),
    ((SELECT user_id FROM users WHERE email = 'bob.smith@example.com'), 'Hydration', 3, 2, '2025-04-01');

-- Select statements for verification
SELECT * FROM users;
SELECT * FROM activity_log;
SELECT * FROM nutrition_log;
SELECT * FROM lifestyle_log;
SELECT * FROM goals;
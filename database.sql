--
CREATE DATABASE IF NOT EXISTS my_database;

--
USE my_database;

-- Create the table of users
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    email VARCHAR(100), 
    password_hash VARCHAR(255), 
    dob DATE,
    gender VARCHAR(10),
    account_created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activity_level VARCHAR(20)
);

--
CREATE TABLE IF NOT EXISTS activity_log (
    activity_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT, 
    activity_type VARCHAR(20) CHECK (activity_type IN ('Cardio', 'Strength', 'Stretching')),
    duration INT, -- duration in minutes
    calories_burned INT,
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- 
CREATE TABLE IF NOT EXISTS nutrition_log (
    nutrition_log INT AUTO_INCREMENT PRIMARY KEY,
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
    log_type VARCHAR(50) CHECK (log_type IN ('Sleep', 'Water Intake')), 
    value VARCHAR(50), -- Store sleep hours or water intake
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- CREATE THE GOAL TABLE 
CREATE TABLE IF NOT EXISTS goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_type VARCHAR(50) CHECK (goal_type IN ('Weight Loss', 'Muscle Gain', 'Hydration')), 
    target_value INT, 
    current_value INT, 
    deadline DATE, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);    


INSERT INTO users (username, email) VALUES
    ('Justin', 'justinsandstedt@gmail.com'); 


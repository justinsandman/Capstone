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

-- CREATE THE BUG TRACKING TABLE 
CREATE TABLE IF NOT EXISTS bug_tracking (
    bug_id INT AUTO_INCREMENT PRIMARY KEY,
    reported_by INT, -- user_id if user, or dev name/id
    description TEXT,
    severity VARCHAR(10) CHECK (severity IN ('Low', 'Medium', 'High')), 
    status VARCHAR(20) CHECK (status IN ('New', 'Assigned', 'Reproduced', 'Fixed', 'Tested', 'Closed')),
    date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_resolved TIMESTAMP,
    FOREIGN KEY (reported_by) REFERENCES users(user_id) ON DELETE SET NULL -- Assuming User is Reporter
);

-- CREATE THE SYSTEM LOG TABLE 
CREATE TABLE IF NOT EXISTS system_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(50) CHECK (event_type IN ('Performance Check', 'Security Audit')),
    event_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);

INSERT INTO users (first_name, last_name, email, password_hash, dob, gender, activity_level) VALUES
    ('Justin', 'Sandstedt', 'justinsandstedt@gmail.com', 'hashedpw', '2002-09-25', 'Male', 'Active'); 


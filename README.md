
<p align="center">
  <img src="FTD%20LOGO.png" alt="FTD Logo" width="250">
</p>

# **Fuel Train Develop (FTD)** 

For our 2025 Computer Science Capstone, we are developing a comprehensive, web-based health and fitness tracker. The final product will allow users to log dietary, exercise, and lifestyle choices. As student-athletes, we value healthy living and want to help others on their wellness journey. We have chosen a web-based platform instead of a phone-based app to provide a greater level of accessibility across devices. 

While many fitness trackers require subscriptions for advanced features, our project will offer these tools free of charge. The application will have three layers: a frontend, a middle layer for communication, and a backend. We have chosen Tailwind CSS for the user interface, Python for backend communication, and MySQL for database management. To guide our design, we are using Figma to create a working prototype.

Our goal is to support users of all experience levels by providing an easy-to-use, accessible tool for tracking health and lifestyle habits. With a clean interface and intuitive features, our tracker will make monitoring progress simple and engaging, empowering users to make informed, healthier choices.

# **Feature List** 

* **Food Logging**
* **Sleep Tracking**
* **Habit Tracking**
* **Weight Tracking**
* **Journal Entries**
* **Program Custumization**
* **Settings & Account Management**

# **External API Used**

**USDA FoodData Central API**
* Official Documentation: https://fdc.nal.usda.gov
* This API was used to retrieve detailed food and nutrition information for the foodlogging features. 

# **Installation/Setup Instructions**

1. **Clone the Repository**
    * git clone https://github.com/justinsandman/Capstone/issues/26
2. **Setup Virtual Environment**
    * 
3. **Install the Required Packages**
    * 
4. **Configure the Database**
    * Ensure you have MySQL installed and running.
    * Create a new MySQL database (you can use database.sql for setup).
    * Update DATABASES settings in capstone/settings.py to match your MySQL credentials.
5. **Apply Database Migrations**
    * python manage.py makemigrations
    * python manage.py migrate
6. **Create a Superuser (for Admin Panel)**
    * python manage.py createsuperuser
7. **Run Development Server**
    * python manage.py runserver
    * Visit http://127.0.0.1:8000 in your web browser to view the app! 

 
# **Files**

## **HTML**
Front-End devlopment files

### **templates**
* **Expenditure.html** 
    * Interface for the expenditure feature which allows users to track their physical activity levels. (i.e weightlifting, running, cycling)
* **FoodLog.html**
    * Interface for the food log feature that allows users to track their food intake and monitor their daily caloric needs. 
* **HabitTracker.html**
    * Interface for habit tracking feature that users user to create and track new habits. Essentially a reminder for habits that reset daily.
* **Journal.html**
    * Interface for journaling feature that gives users the space to journal, write notes, etc.
* **Login.html**
    * Interface for the log-in page.
* **MainDashboard.html**
    * Interface for the home page of the application, this includes all the features and widget for daily nutrition.
* **Program.html**
    * Interface for users programs that are customizable. This is where users can set their program that determines their nutrition goals.
* **settings.html**
    * Interface for the settings pages that hold changable data about the users and support options.
* **Signup.html**
    * Interface for the sign-up page.
* **SleepLog.html**
    * Interface for sleep log feature that users manually input sleep data from wearables.
* **WeightLog.html**
    * Interface for weight logging where users can input their bodyweight manually that is visualized on a line plot
* **ActivityLevel.html**
    * Interface for the user to be able to change their activity level
* **ForgotPassword.html**
    * Interface for the user to be able to enter their email to reset password
* **MyAccount.html**
    * Interface for the user to be able to manage their account
* **ResetPassword.html**
    * Interface for once the user enters their email and it matches where they will be able to enter a new password
    
## SQL
Database Testing file
* database.sql
    * This file contains the SQL scripts used to initialize and populate the project's test database.
    * Responible for creating main database and user credintials. 
    * Defines database schema. 
    * Inserts test data into each table for intial testing and demonstration. 


## Python
Main logic for setting up Django framework

### **capstone**
* **settings.py**
    * Contains all project settings such as installed apps, database configurations, static files setup, and third-party API keys.
* **urls.py**
    * Defines the URL patterns that route web requests to the appropriate views across the project.
* **views.py**
    * Handles logic for processing requests, interacting with models, and rendering responses (HTML templates or JSON).
* **wsgi.py**
    * Entry-point for WSGI-compatible web servers to serve project; used in production deployment.

### **core**
* **admin.py**
    * Registers models for the Django admin interface, allowing data management through the built-in admin dashboard.
* **forms.py**
    * Defines custom forms used for user input and data validation (such as workout entries, food logs, etc.).
* **utils.py**
    * Contains helper functions or modules, such as functions that communicate with the USDA API or perform data processing.

### **nutrition**
* **models.py**
    * Defines the database schema (tables and fields) using Django's ORM; includes models like FoodLog or WeightLog. 

* **manage.py**
    * This is the command-line utility for interacting with the Django project.
    * Runs administrative tasks such as starting the server, migrating databases, creating apps, and managing users.
    * Sets up the correct Django settings module (capstone.settings) before executing commands.
    * Serves as the main entry point for Django's built-in management commands (runserver, migrate, createsuperuser, etc.).

---
## **Authors**
**Gabriel Morgan, Matthew Swandal, & Justin Sandstedt**






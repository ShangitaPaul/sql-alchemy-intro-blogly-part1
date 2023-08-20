# sql-alchemy-intro-blogly-part1
http://curric.rithmschool.com/springboard/exercises/flask-blogly/

# Blogly part 1 project description:

The code is for part 1 of an app called "Blogly," which is a simple blogging application using Flask, SQLAlchemy, and Bootstrap. This app allows users to perform CRUD (Create, Read, Update, Delete) operations on user profiles. Here's a breakdown of the main components and files in the app:

app.py: This file is the main application script that sets up the Flask app and defines the routes for various user operations.

models.py: This file defines the SQLAlchemy model for the User class, which represents user data in the database. It also includes a function to connect the database to the Flask app.

base.html: This is the base template for the app's UI. It provides the common layout and styling elements that are shared across different pages of the app (edit.html, index.html, new.html, show.html).
  /users:
    edit.html:This template is used to display a form for editing user information.
    new.html: 

requirements.txt: This file lists all the Python packages and their versions required to run the app. These packages include Flask, Flask extensions, SQLAlchemy, and others.

Overall, this app follows a standard Flask structure with routes defined for viewing, creating, updating, and deleting user profiles. The base template provides a consistent UI design, and the SQLAlchemy model is used to interact with the database.Any visitor to the site should be able to see all users, add a user, or edit any user.

# Routes
The purpose of the project is to build a blogging application called "Blogly" using Flask and SQLAlchemy. The application allows users to interact with user profiles without the need for authentication. The main routes defined in the Flask app corrospond to different URL paths that users can access to perform various actions (described above). The HTML files (edit.html, index.html, new.html, and show.html) are templates that are used to render the content of those routes. Each route typically corresponds to a specific template file.

**Breakdown how these routes relate to the HTML templates:**
1. GET /: Redirect to list of users. (We’ll fix this in a later step).
   
2. GET /users:
   
- This route displays a list of all users.
- Corresponding HTML Template: index.html
  
3. GET /users/new: 

- This route shows a form for adding a new user.
- Corresponding HTML Template: new.html
  
4. POST /users/new
   
- This route processes the submitted form for adding a new user and redirects back to the list of users or the user's detail page.
- No corresponding HTML Template. It involves data processing and redirection.
  
5. GET /users/[user-id]

- This route displays detailed information about a specific user.
- Corresponding HTML Template: show.html
  
6. GET /users/[user-id]/edit
 
- This route shows an edit form for a specific user.
- Corresponding HTML Template: edit.html

7. POST /users/[user-id]/edit

- This route processes the submitted form for editing a user's details and redirects back to the user's detail page.
- No corresponding HTML Template. It involves data processing and redirection.
  
8. POST /users/[user-id]/delete

- This route deletes a specific user from the database and redirects to the list of users.
- No corresponding HTML Template. It involves data processing and redirection.

**To summarize:**

- The index.html template is used to display the list of users (GET /users).
- The new.html template is used for the form to add a new user (GET /users/new).
- The show.html template is used to display detailed information about a user (GET /users/[user-id]).
- The edit.html template is used for the form to edit a user's details (GET /users/[user-id]/edit).
  
Routes that involve form submissions and data processing (POST methods) don't have a corresponding HTML template because they usually redirect back to another route, which then displays a template based on the updated data.



**To write tests for these routes, follow these steps:**

Create a Test Directory: Create a directory named tests in your project directory to store your test files.

Import Modules: In the test file, import necessary modules and classes including Flask, SQLAlchemy, and testing libraries.

Create a Test Class: Define a test class that inherits from a testing base class (e.g., TestCase from flask_testing).

Configure Testing Environment: Override the create_app method to configure your Flask app for testing.

Set Up and Tear Down: Implement the setUp and tearDown methods to set up and clean up the test environment (usually involving database setup and teardown).

Write Test Methods: Create test methods to simulate requests and verify responses for each route. Use self.client for request simulation and assertions to validate responses.

Run Tests: Open your terminal, navigate to the project directory, and run tests using the testing framework's command-line tools.

Interpret Test Results: Review the test results to see which tests passed and which ones failed. Fix any issues that arise.

Repeat for Other Routes: Follow a similar process to create tests for other routes and functionalities in your application.


# To generate a requirements.txt file for your Flask project using SQLAlchemy:

Activate Virtual Environment (Optional but Recommended): It's a good practice to work within a virtual environment to isolate your project's dependencies from the system-wide Python packages. You can create and activate a virtual environment like this:

1. Create a virtual environment:
python -m venv venv

2. Activate the virtual environment (on macOS/Linux)
source venv/bin/activate

3. Install Packages: Install the necessary packages for your Flask and SQLAlchemy project. You can do this using pip while your virtual environment is active. For example:

pip install flask sqlalchemy

4. Generate requirements.txt: After you've installed all the required packages for your project, you can generate the requirements.txt file using the pip freeze command. This command lists all installed packages and their versions:

pip freeze > requirements.txt

5.Deactivate Virtual Environment (Optional): When you're done working on your project, you can deactivate the virtual environment:

deactivate

6. Review and Edit: Open the requirements.txt file in a text editor to review its contents. It will list all the packages that were installed in your virtual environment.





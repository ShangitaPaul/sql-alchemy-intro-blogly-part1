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
The purpose of the project is to build a blogging application called "Blogly" using Flask and SQLAlchemy. The application allows users to interact with user profiles without the need for authentication. The main routes include:

GET /users: Displays a list of all users.

GET /users/new: Shows a form to add a new user.

POST /users/new: Processes the add user form and adds a new user to the database.

GET /users/[user-id]: Displays detailed information about a specific user.

GET /users/[user-id]/edit: Shows an edit form for a specific user.

POST /users/[user-id]/edit: Processes the edit user form and updates the user's details.

POST /users/[user-id]/delete: Deletes a specific user.



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





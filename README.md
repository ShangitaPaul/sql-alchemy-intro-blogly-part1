# sql-alchemy-intro-blogly-part1
http://curric.rithmschool.com/springboard/exercises/flask-blogly/

The code is for part 1 of an app called "Blogly," which is a simple blogging application using Flask, SQLAlchemy, and Bootstrap. This app allows users to perform CRUD (Create, Read, Update, Delete) operations on user profiles. Here's a breakdown of the main components and files in the app:

app.py: This file is the main application script that sets up the Flask app and defines the routes for various user operations.

models.py: This file defines the SQLAlchemy model for the User class, which represents user data in the database. It also includes a function to connect the database to the Flask app.

base.html: This is the base template for the app's UI. It provides the common layout and styling elements that are shared across different pages of the app (edit.html, index.html, new.html, show.html).

requirements.txt: This file lists all the Python packages and their versions required to run the app. These packages include Flask, Flask extensions, SQLAlchemy, and others.

Overall, this app follows a standard Flask structure with routes defined for viewing, creating, updating, and deleting user profiles. The base template provides a consistent UI design, and the SQLAlchemy model is used to interact with the database.





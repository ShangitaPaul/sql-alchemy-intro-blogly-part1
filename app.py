"""Blogly application."""

"""app.py: Set up the Flask App and Database"""

# import modules Flask, request, redirect, render_template from Flask and DebugToolbarExtension from flask_debugtoolbar 
from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
# import the db, connect_db, and User classes from models.py file.
from models import db, connect_db

# create Flask app
app = Flask(__name__)

# set the database URI to "postgresql:///blogly" in the app.config. This tells Flask to use a PostgreSQL database named "blogly". 
    # Replace this URI with your actual PostgreSQL database URI.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
# disable track modifications for performance reasons.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Replace 
# app.config['SQLALCHEMY_ECHO'] = True
# with
app.config['SECRET_KEY'] = 'secretkey'
    # Reason: Echoing SQL statements can potentially leak sensitive information about your database schema and operations, which could be exploited by attackers; while app.config['SECRET_KEY'] is essential for CSRF protection and session security.



# Debug Toolbar show redirects explicitly;
# If you want to enable the Flask Debug Toolbar to show  information about requests and redirects, uncomment the line app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False. This is useful for debugging during development but can be turned off in production.
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

# Define routs for user iperations using @app.route decorator
@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")


##############################################################################
# User route

@app.route('/users')
# users_index: Retrieves all users from the database and renders the 'users/index.html' template to display information about all users in alphabetical order by last name and first name.
def users_index():
    """Display a page with info on all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)


@app.route('/users/new', methods=["GET"])
# users_new_form: Renders the 'users/new.html' template to show a form for creating a new user.
def users_new_form():
    """Show a form to create a new user"""

    return render_template('users/new.html')


@app.route("/users/new", methods=["POST"])
# users_new: Handles the form submission for creating a new user. It retrieves form data from the request, creates a new User object, adds it to the database session, and commits the changes to the database.
def users_new():
    """Handle form submission for creating a new user"""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>')
# users_show: Retrieves a specific user from the database using the provided user_id, or shows a 404 error page if the user does not exist. It then renders the 'users/show.html' template to display information about the user.
def users_show(user_id):
    """Show a page with info on a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)


@app.route('/users/<int:user_id>/edit')
# users_edit: Retrieves a specific user from the database using the provided user_id and renders the 'users/edit.html' template to show a form for editing the user's information.
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
# users_update: Handles the form submission for updating an existing user. It retrieves form data from the request and updates the user's information in the database before redirecting to the user's detail page.
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
# users_destroy: Handles the form submission for deleting an existing user. It retrieves the user from the database and deletes it before redirecting to the list of users.
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


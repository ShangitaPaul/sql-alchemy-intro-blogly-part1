"""Models for Blogly: Defone the User model and created a connection between the database and the Flask app using SQLAlchemy. The User model will be used to represent user data in the "users" table, and we can perform database operations using the db object, such as adding, querying, updating, and deleting user records.."""


# Importing the SQLAlchemy class from flask_sqlalchemy module. S
    # SQLAlchemy is a powerful Object-Relational Mapping (ORM) library that simplifies working with databases in Flask applications.
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy Object
    # Create an instance of the SQLAlchemy class and name it db. This object will be used to interact with the database and define the models.
db = SQLAlchemy()

# Set default image URL
    # Define a constant variable DEFAULT_IMAGE_URL to store the default profile image URL for users. This URL will be used if a user does not provide a custom image URL.
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


# Define the User Model: 
    # We define the User model class, which represents the data structure of a user in the database. The model inherits from db.Model, which indicates that it is a SQLAlchemy model.
    # Add Full Name property 
        # define a property method full_name in the User model using the @property decorator.
        # The full_name property method returns the user's full name by combining their first and last names.
class User(db.Model):
    """
    User model for SQLAlchemy.

    Attributes:
        id (int): Autoincrementing integer number that is the primary key.
        first_name (str): User's first name.
        last_name (str): User's last name.
        image_url (str): Profile image URL for the user.
    """
    
    # We use __tablename__ = "users" to specify the name of the database table where the user data will be stored. In this case, the table name will be "users".
    __tablename__ = 'users'
    
    # We define three columns: id, first_name, and last_name, with their respective data types. id is the primary key for the table, and both first_name and last_name cannot be null because rhey are required fields).
    id = db.Column(db.Integer, primary_key=True, #autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Define the image_url column with a default value of DEFAULT_IMAGE_URL. This column will store the URL of the user's profile image, and the default URL will be used if the user does not provide a custom image URL.
    # Change
    # image_url = db.Column(db.String(200), default='default_profile_image.jpg')
    # to    
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    # Reason: using a constant variable like DEFAULT_IMAGE_URL ("https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png") is more flexible and maintainable than directly setting the default value to a specific string like 'default_profile_image.jpg'. Using a constant variable allows easy changes to the default image URL in the future, should the need arise.
    
    # Define the User Model:  
        # We define the User model class, which represents the data structure of a user in the database. The model inherits from db.Model, which indicates that it is a SQLAlchemy model.  
    class User(db.Model):
        """Site user."""\
    
    # Use __tablename__ = "users" to specify the name of the database table where the user data will be stored. In this case, the table name will be "users".
    __tablename__ = "users"
    
    # Define three columns: id, first_name, and last_name, with their respective data types. id is the primary key for the table, and both first_name and last_name cannot be null (i.e., they are required fields).
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    # Define the image_url column with a default value of DEFAULT_IMAGE_URL. This column will store the URL of the user's profile image, and the default URL will be used if the user does not provide a custom image URL.
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    # Define a @property method called full_name. This method returns the user's full name by combining their first_name and last_name.
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

 # Define Database connection function
    # define a function connect_db(app) that connects the db (SQLAlchemy) object to the Flask app.
def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """
    # set the app attribute of the db object to the provided Flask app, so SQLAlchemy knows which app is using it.
    db.app = app
    # initialize the db object with the Flask app using db.init_app(app). This step completes the connection between the database and the Flask app.
    db.init_app(app)

    # Optional: This method returns a string representation of the User object in the form of <User id=1 first_name=John last_name=Doe>, where id, first_name, and last_name are the actual values of the object's attributes. 
        # For this application, the provided routes and templates do not involve displaying the object's representation directly to users.
        # The __repr__ method can be useful for customizing the representation of objects in different contexts. For example, in an API, you might want to display only specific attributes or hide sensitive information. Since the provided solution focuses on buiding a basic blogging application without complex customizations, the inclusion of __repr__ might not be necessary for the current scope.
    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name}>"

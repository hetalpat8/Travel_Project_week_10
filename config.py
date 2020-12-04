# Import the os module
import os

# creation of base directory for application 
basedir = os.path.abspath(os.path.dirname(__file__)) 
# regardless of operating system, where to find the confing file

#we're telling the server, regardless of the file path, you can still find the information in this area:


# Config Class
# this will configure the database (when we have one) AND configure the
# secret key for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this....'
    # we want sqlalchemy to setup where our database is going to be: which will be local to this project in our class folder

    # TO_DO: Elimnated the or for SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
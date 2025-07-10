import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    # Use 'alumni.db' or 'database.db' as appropriate
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'alumni.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

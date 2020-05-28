import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SECRET_KEY= '6\xd5\xa5I\x88\xc0\x06\x11\xa1\x9d]k]]\xeeg\x80\xda\xbeL\xfa\xe7/\xbf'

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:HopeP2020@localhost:5432/fyyur2'

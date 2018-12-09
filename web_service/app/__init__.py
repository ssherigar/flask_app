"""
This script creates the application object as an instance 
of class Flask imported from the flask package
"""

from flask import Flask

# app - instance of class Flask
app = Flask(__name__)

from app import routes

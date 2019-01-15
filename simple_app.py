"""Flask simple example"""
from flask import Flask
APP = Flask(__name__)

@APP.route('/')
def hello_world():
    """Display: Hello, World! on the main page"""
    return 'Hello, World!'

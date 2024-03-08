import pytest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "Anula"
    return f'Hej jak sie masz? {my_name}!'


from flask import Flask
from mvc_flask import FlaskMVC
import torch
app = Flask(__name__)

FlaskMVC(app)

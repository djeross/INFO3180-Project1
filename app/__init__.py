from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

db = SQLAlchemy(app)

csrf = CSRFProtect(app)
app.config.from_object(Config)
from app import views
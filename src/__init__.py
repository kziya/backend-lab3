from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

from src.category import category_controller
from src.user import user_controller
from src.record import record_controller

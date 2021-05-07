from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.31.136/flask_db'
app.config["SECRET_KEY"] = "ytfd57id57dktctd5o7dc8c7d7ct"
db = SQLAlchemy(app)

from application import routes
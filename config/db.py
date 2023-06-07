# Importación de librerias a trabajar
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
# odontograma es el nombre de mi BDD
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/odontograma"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "JuanBarrios12"

bd = SQLAlchemy(app)
ma = Marshmallow(app)

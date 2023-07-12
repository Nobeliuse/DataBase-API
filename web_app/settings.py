from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roott:amkmskfla@db/postgres_db'
app.config['SECRET_KEY'] = 'JKANskaldkll21masasfdfaQW'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

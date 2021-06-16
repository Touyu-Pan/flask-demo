from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twittor.route import index, login

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:twittor.db:"
    db.init_app(app)
    migrate.init_app(app, db)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app
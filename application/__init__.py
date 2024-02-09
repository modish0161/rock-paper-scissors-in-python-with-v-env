##init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Externalize your configuration
    app.config.from_pyfile('config.py')

    db.init_app(app)
    Migrate(app, db)

    # Import models to ensure they are registered with SQLAlchemy
    from application import models

    # Import routes to register them with the app
    from application import routes

    return app

app = create_app()


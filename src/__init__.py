from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'dev-key-change-later'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'

    db.init_app(app)
    from .routes import main
    from .models import Entry
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)


    return app
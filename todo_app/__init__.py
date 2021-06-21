from flask import Flask
from .commands import create_tables
from .extensions import db, login_manager
from .models import User
from .routes.main import main
from .routes.user import user
from .routes.task import task
from todo_app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    app.register_blueprint(main)
    app.register_blueprint(user)  
    app.register_blueprint(task)     
    app.cli.add_command(create_tables)
    return app
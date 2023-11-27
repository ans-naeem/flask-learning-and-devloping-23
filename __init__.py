from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#imporitng database
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    
    #configurations
    app.config['secret_key']='ans_naeem'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.database'
    
    #now initializing database
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app





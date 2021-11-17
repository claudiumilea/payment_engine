from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


db = SQLAlchemy()
load_dotenv()
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    SERVER_NAME = os.environ['SERVER_NAME']

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    # app.run(debug=True, host=os.environ.get('APP_HOST'), port=os.environ.get('APP_PORT'))
    return app


app = create_app()
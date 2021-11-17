from dotenv import load_dotenv
from config import db, app
from flask import Flask
import os, sys, inspect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

load_dotenv()

try:
    from models import Transaction

except ImportError as e:
    print(e)



if __name__ == '__main__':
    db.create_all()
    db.session.commit()


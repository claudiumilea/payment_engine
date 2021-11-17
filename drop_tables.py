from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from config import db, app

load_dotenv()


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column('id', db.Integer, primary_key=True)


class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)


if __name__ == '__main__':
    db.drop_all()

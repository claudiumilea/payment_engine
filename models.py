from config import db
from datetime import datetime


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    type = db.Column('type', db.String, nullable=False)
    client = db.Column('client', db.Integer, nullable=False)
    tx = db.Column('tx', db.Integer, nullable=False)
    amount = db.Column('amount', db.Float, nullable=False)

    created_at = db.Column('created_at', db.TIMESTAMP, default=datetime.now, nullable=False)
    updated_at = db.Column('updated_at', db.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False)


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    available = db.Column('available', db.Float, nullable=False)
    held = db.Column('held', db.Float, nullable=False)
    total = db.Column('total', db.Float, nullable=False)
    locked = db.Column('locked', db.Boolean, nullable=False)

    created_at = db.Column('created_at', db.TIMESTAMP, default=datetime.now, nullable=False)
    updated_at = db.Column('updated_at', db.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self) -> str:
        return '<Client %r available: %r held: %r total: %r locked: %r>' % (self.id, self.available, self.held, self.total, self.locked)

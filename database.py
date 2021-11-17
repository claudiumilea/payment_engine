from app import db
from models import Transaction, Client


class Database:
    def upsert_client(self, app, client_dataclass):
        app.app_context().push()
        c = Client(id=client_dataclass.id,
                   available=client_dataclass.available,
                   held=client_dataclass.held,
                   total=client_dataclass.total,
                   locked=client_dataclass.locked)
        db.session.merge(c)
        db.session.commit()

    def select_client(self, app, client_id) -> Client:
        app.app_context().push()
        selected_client = db.session.query(Client).filter_by(id=client_id).first()
        c = Client(id=selected_client.id,
                   available=selected_client.available,
                   held=selected_client.held,
                   total=selected_client.total,
                   locked=selected_client.locked
                   )
        return c

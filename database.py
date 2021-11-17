from app import db
from models import Transaction, Client
import pandas as pd

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

    def select_all_clients(self, app) -> list:
        app.app_context().push()
        all_clients = db.session.query(Client).all()
        return all_clients

    def export_all_clients_to_csv(self, filename):
        clients_df = pd.read_sql('clients', db.session.bind)
        clients_df = clients_df.drop(['created_at', 'updated_at'], axis=1)
        clients_df.to_csv(filename,index=False)


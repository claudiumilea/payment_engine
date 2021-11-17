from app import db, create_app
from models import Client
import random


def random_client() -> dict:
    random_total = round(random.uniform(1, 100.0), 2)
    random_held = round(random.uniform(0, 10.0), 2)
    available = round(random_total - random_held, 2)

    return {'available': available, 'held': random_held, 'total': random_total, 'locked': False}


def insert_client_db(app):
    app.app_context().push()
    client = random_client()

    c = Client(available=client.get('available'),
               held=client.get('held'),
               total=client.get('total'),
               locked=client.get('locked'))
    db.session.add(c)
    db.session.commit()


if __name__ == "__main__":
    app = create_app()
    number_of_random_clients = 7
    for _ in range(0, number_of_random_clients):
        insert_client_db(app)

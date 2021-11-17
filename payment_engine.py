from enum import Enum
import pandas as pd
from database import Database
from app import create_app
from clients import Client


class ClientOperation(Enum):
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'
    DISPUTE = 'dispute'
    RESOLVE = 'resolve'
    CHARGEBACK = 'chargeback'


class InputHeadings(Enum):
    TYPE = 0
    CLIENT = 1
    TX = 2
    AMOUNT = 3

    def __str__(self):
        return 'Client operation: {0}'.format(self.value)


class PaymentEngine:

    def __init__(self):
        self.app = create_app()
        self.database = Database()

    def get_transactions_df(self) -> pd.DataFrame:
        return pd.read_csv("data/transactions.csv")

    def set_chargeback(self, client_id):
        pass

    def get_client(self, client_id) -> Client:
        client = self.database.select_client(self.app, client_id)
        print(client)
        return client

    def get_all_clients(self):
        self.database.export_all_clients_to_csv(filename='client_accounts.csv')



    def get_client_operation(self, df_row):
        return df_row[1][InputHeadings.TYPE.value]

    def set_client(self, client_id, available, held, total, locked):
        c = Client(id=client_id, available=available, held=held, total=total, locked=locked)
        self.database.upsert_client(self.app, c)

    def export_client_csv(self):
        pass

if __name__ == '__main__':
    payment_engine = PaymentEngine()

    csv_df = payment_engine.get_transactions_df()
    print(csv_df)
    for row in csv_df.iterrows():
        client_operation = payment_engine.get_client_operation(row)
        client = payment_engine.get_client(row[1][InputHeadings.CLIENT.value])
        client_id = row[1][InputHeadings.CLIENT.value]
        match client_operation:
            case ClientOperation.DEPOSIT.value:
                print('este depozit')
                amount = row[1][InputHeadings.AMOUNT.value]
                available = client.available + amount
                total = client.total + amount
                payment_engine.set_client(client_id=client_id, available=available, held=client.held, total=total, locked=client.locked)
            case ClientOperation.WITHDRAWAL.value:
                print('este WITHDRAWAL')
                amount = row[1][InputHeadings.AMOUNT.value]
                available = client.available - amount
                total = client.total - amount
                payment_engine.set_client(client_id=client_id, available=available, held=client.held, total=total, locked=client.locked)
            case ClientOperation.DISPUTE.value:
                print('este DISPUTE')
                amount = row[1][InputHeadings.AMOUNT.value]
                available = client.available - amount
                held = client.held + amount
                payment_engine.set_client(client_id=client_id, available=available, held=held, total=client.total, locked=client.locked)
            case ClientOperation.RESOLVE.value:
                print('este RESOLVE')
                amount = row[1][InputHeadings.AMOUNT.value]
                available = client.available - amount
                held = client.held + amount
                payment_engine.set_client(client_id=client_id, available=available, held=held, total=client.total, locked=client.locked)
            case ClientOperation.CHARGEBACK.value:
                print('este CHARGEBACK')
                amount = row[1][InputHeadings.AMOUNT.value]
                held = client.held - amount
                total = client.total - amount
                locked = True
                payment_engine.set_client(client_id=client_id, available=client.available, held=held, total=total, locked=locked)


    payment_engine.get_all_clients()
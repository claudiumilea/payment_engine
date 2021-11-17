from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Transaction:

    transaction_type: str
    client: int
    tx: int
    amount: Decimal


from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Client:

    id: str
    available: Decimal
    held: Decimal
    total: Decimal
    locked: bool


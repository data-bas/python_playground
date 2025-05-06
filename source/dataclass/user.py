from dataclasses import dataclass

""""Dataclass maakt een klasse welke automatisch __init__, __eg, __repr__ methoden genereert.
    Methode als Frozen of order breiden dit uit."""


@dataclass(order=True)
class User:
    username: str
    email: str
    age: int
    active: bool = True

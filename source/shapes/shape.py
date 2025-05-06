from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_opp(self):
        """Bereken en retourneer de oppervlakte"""
        pass  # Hier geen implementatie nodig, dit wordt afgedwongen in subklassen.

    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        """Retourneer het type van de vorm"""
        pass  # Dit moet ook worden geïmplementeerd door de subklassen.

from abc import ABC, abstractmethod

class Sujet(ABC):

    def __init__(self):
        self._observateurs = []

    def abonner(self, observateur) -> None:
        # À compléter

    def desabonner(self, observateur) -> None:
        # À compléter

    def notifier(self) -> None:
        # À compléter — quelle méthode appelle-t-on sur chaque observateur ?

    @abstractmethod
    def get_donnees(self) -> dict:
        pass
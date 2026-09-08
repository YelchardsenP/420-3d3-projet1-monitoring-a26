from observers.observer import Observateur
import tkinter as tk
 
class AlerteCPU(Observateur):
 
    def __init__(self, parent, seuil: float = 80.0):
        self._seuil = seuil

        self._label = tk.Label(parent, text="")
 
    def actualiser(self, sujet) -> None:
        donnees_metriques = sujet.get_donnees()
        cpu = donnees_metriques["cpu"]
        
        if cpu > self._seuil:
            self._label.config(text="CPU 80% AAHHVERTISSEMENT!!!", font=("Arial", 12, "bold"), fg="red")
            self._label.pack()
        else:
            self._label.forget()
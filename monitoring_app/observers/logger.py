from datetime import datetime
from observers.observer import Observateur

class Logger(Observateur):
    def __init__(self):
        pass
    
    def actualiser(self, sujet) -> None:
        
        donnees_metriques = sujet.get_donnees()
        cpu = donnees_metriques["cpu"]
        ram = donnees_metriques["ram"]
        disque = donnees_metriques["disque"]

        self.ecrire_ligne(cpu,ram,disque)

        
        
        
    
    def ecrire_ligne(self, valeur1, valeur2, valeur3):
        
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        ligne = (
            f"{horodatage} | "
            f"CPU: {valeur1}% | "
            f"RAM: {valeur2}% | "
            f"Disque: {valeur3}%\n "
        )

        with open("monitoring.log", "a") as f:
            f.write(ligne)

        print(ligne)


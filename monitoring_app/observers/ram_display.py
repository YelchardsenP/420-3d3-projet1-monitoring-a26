import tkinter as tk
from observers.observer import Observateur

class AffichageRAM(Observateur):

    def __init__(self, fenetre_parent: tk.Frame): #type hint
        # À compléter: Créez un LabelFrame "ram", un Label pour le pourcentage et un Canvas pour la barre de progression
        self.frame_ram = tk.LabelFrame(fenetre_parent, text="ram", padx=10, pady=10)
        self.frame_ram.pack(fill=tk.X, padx=10, pady=5)
        
        self.label_ram = tk.Label(self.frame_ram, text="0%", font=("Arial", 24, "bold"))
        self.label_ram.pack()
        
        self.canvas_ram = tk.Canvas(self.frame_ram, width=300, height=20, bg="white")
        self.canvas_ram.pack()


    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur ram depuis sujet.get_donnees()
        # À compléter: Mettez à jour le label et la barre
        
        # ram_value = sujet.get_donnees().get("ram") #version direct
        donnees_metriques = sujet.get_donnees() #Obtient donnes sujets
        donnees_ram = donnees_metriques["ram"]

        self.label_ram.config(text=f"{donnees_ram:.1f}%")

        self._dessiner_barre(donnees_ram)


       


    def _dessiner_barre(self, valeur: float) -> None:
        # À compléter: # Effacez le canvas# Calculez la largeur (300 * valeur / 100)# Choisissez la couleur : vert < 50%, orange < 80%, rouge sinon# Dessinez le rectangle
        
        
        self.canvas_ram.delete("all")
        
        largeur_ram = int(300 * valeur / 100)
        if valeur < 50:
            couleur_ram = "green"
        elif valeur < 80:
            couleur_ram = "orange"
        else:
            couleur_ram = "red"
        
        self.canvas_ram.create_rectangle(0, 0, largeur_ram, 20, fill=couleur_ram, outline="")

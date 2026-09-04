from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
import tkinter as tk

metriques = MetriquesSysteme()
root = tk.Tk()
cpu = AffichageCPU(root)
ram = AffichageRAM(root)
disque = AffichageDisque(root)

metriques.abonner(cpu)
metriques.abonner(ram)
metriques.abonner(disque)

def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()
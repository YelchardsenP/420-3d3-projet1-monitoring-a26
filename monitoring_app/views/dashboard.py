import tkinter as tk

from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
from observers.logger import LoggerFichier
from observers.alerte_cpu import AlerteCPU
 
class Dashboard(tk.Tk):
 
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
 
        # À compléter :
        # 1. Créez les observateurs (AffichageCPU, AffichageRAM,
        #    AffichageDisque, LoggerFichier)
        # 2. Abonnez-les tous au sujet
        # 3. Démarrez le rafraîchissement

        self._creer_observateurs()
        self._abonner_observateurs()
        self._rafraichir()
    
    
    def _creer_observateurs(self) -> None:
        
        self._cpu = AffichageCPU(self)
        self._ram = AffichageRAM(self)
        self._disque = AffichageDisque(self)
        self._logger = LoggerFichier()
        self._alerte_cpu = AlerteCPU(self)
 
    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self._cpu)
        self._metriques.abonner(self._ram)
        self._metriques.abonner(self._disque)
        self._metriques.abonner(self._logger)
        self._metriques.abonner(self._alerte_cpu)

 
    def _rafraichir(self) -> None:
        # À compléter :
        # Appelez actualiser_metriques() sur les métriques
        # Planifiez le prochain appel avec self.after()
        self._metriques.actualiser_metriques()
        self.after(self.INTERVALLE_MS, self._rafraichir)
class Gestion_Taches:

    def __init__(self):
        self.Table_taches = []

    def ajouter_tache(self, tache):
        self.Table_taches.append(tache)
        print(" ->  Tache ajoutee . ")

    def supprimer_tache(self, tache)  :
        if tache in self.Table_taches :
            self.Table_taches.remove(tache)
            print(" -> Tache supprimee  . ")

        else :
            print(" -> non tache  . ")  



          

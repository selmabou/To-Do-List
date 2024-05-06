import csv 

class GESTION_TACHES :
    def __init__(self):
        self.Table_Taches = []
        self.charger_donnees_csv()


    def Ajouter_tache(self):
        self.Afficher_Tache()
        tache = input(" -> SAISIR VOTRE TACHE : ")
        if tache :
            self.Table_Taches.append(tache)
            self.Sauvgarder_donnees_csv()
            print(" La tache ajoute avec succes .")
        else :
            print("Veuillez entrer une tache !! ") 


    def Supprimer_Tache(self):
        self.Afficher_Tache()
        tache = int(input(" -> ENTREZ L'INDEX DU TACHE A SUPPRIMER : "))
        if 0 <= tache and tache < len(self.Table_Taches) :
            del self.Table_Taches[tache]
            self.Sauvgarder_donnees_csv()
            
            print(" La tache supprimer avec succes .")
        else:
            print(" la tache non trouve !! ")
  



    def Afficher_Tache(self):
        if self.Table_Taches :
            print(" Liste des taches : ")
            
            for mon_tache in self.Table_Taches :
                print(mon_tache)

        else:
            print(" Aucun tache dans la liste !! ")

            
            

    def Modifier_tache(self , Ancien_Tache , nv_tache):
        if Ancien_Tache in self.Table_Taches:
            id = self.Table_Taches.index(Ancien_Tache)
            self.Table_Taches[id] = nv_tache 
            self.Sauvgarder_donnees_csv()

            print(" La tache a modifiee succes . ")   

        else :
            print(" La tache non trouve !! ")  



    def Sauvgarder_donnees_csv(self):
        with open('file_tasks.csv', 'w') as file:
            writer = csv.writer(file)
            for tache in self.Table_Taches :
                writer.writerow([tache])



    def charger_donnees_csv(self): 
        try:
            with open('file_tasks.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row :
                        self.Table_Taches.append(row[0])
        except FileNotFoundError:
            pass


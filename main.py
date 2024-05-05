import csv 

class GESTION_TACHES :
    def __init__(self):
        self.Table_Taches = []
        self.charger_donnees_csv()


    def Ajouter_tache(self):
        tache = input(" -> SAISIR VOTRE TACHE : ")
        if tache :
            self.Table_Taches.append(tache)
            self.Sauvgarder_donnees_csv()
            print(" La tache ajoute avec succes .")
        else :
            print("Veuillez entrer une tache !! ") 



    def Supprimer_Tache(self):
        tache = input(" -> ENTREZ LA TACHE A SUPPRIMER : ")
        if tache in self.Table_Taches :
            self.Table_Taches.remove(tache)
            self.Sauvgarder_donnees_csv
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

            print(" La tache a modifiee succes . ")   

        else :
            print(" La tache non trouve !! ")  



    def Sauvgarder_donnees_csv(self):
        with open('mes_taches.csv', 'w') as file:
            writer = csv.writer(file)
            for tache in self.Table_Taches :
                writer.writerow([tache])



    def charger_donnees_csv(self): 
        try:
            with open('mes_taches.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row :
                        self.Table_Taches.append(row[0])
        except FileNotFoundError:
            pass



if __name__ == "__main__" :

    user = input(" Entrez votre nom d'utilisateur : ")   
    password = input(" Entrez votre mot de pass   : ")     

    if user == 'root'  and password == '123':
        to_do_list = GESTION_TACHES()

        while True :    
            print("\n >>>   APP GESTION DES TACHES   <<< ") 
            print(" 1. AJOUTER UNE TACHE ")
            print(" 2. SUPPRIMER UNE TACHE ")
            print(" 3. AFFICHER LISTE DES TACHES ")
            print(" 4. MODIFIER UNE TACHE ")
            print(" 5. QUITTER ")


            choix = input(" \n => CHOISISSEZ UNE OPTION : ")

            if choix == "1":
                to_do_list.Ajouter_tache()

            elif choix == "2":
                to_do_list.Supprimer_Tache()

            elif choix == "3":
                to_do_list.Afficher_Tache()

            elif choix == "4":
                Ancien_Tache = input(" Entrez l'ancien tache : ")
                nv_tache = input(" Entrez la nouvelle tache  : ")
                to_do_list.Modifier_tache(Ancien_Tache, nv_tache)

            elif choix == "5":
                break

            else:
                print (" OPTION INVALIDE !! ")    

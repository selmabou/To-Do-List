import csv

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


    def afficher_taches(self):
        print("Liste des tâches :")
        for tache in self.Table_taches:
            print("-> ", tache)


    def csv_taches(self, nom_fichier):
        with open(nom_fichier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for tache in self.Table_taches:
                writer.writerow([tache])


def main():
    to_do_list = Gestion_Taches()

    while True:
        print("       MENU :     ")  
        print("------      ------")    
        print(" 1 ->  AJOUTEE UNE TACHE :  ") 
        print(" 2 ->  SUPPRIMEE UNE TACHE :  ") 
        print(" 3 ->  AFFICHER LA LISTE DES TACHES : ")
        print(" 4 ->  SORTIE !!  ")  


        nombre = input(" ENTREE VOTRE CHOIX :") 

        if nombre == "1" :
            Une_Tache = input("-> ENTRER VOTRE TACHE : ")
            to_do_list.ajouter_tache(Une_Tache)

        elif nombre == "2":
            Une_Tache = input("-> ENTRER LA TACHE A SUPPRIMER ")
            to_do_list.supprimer_tache(Une_Tache)

        elif choix == "3":
                to_do_list.afficher_taches()

        elif nombre == "4":
            print("-> QUITTER LE PROGRAMME .")
            break
        else:
            print("-> CHOIX INVALIDE !!!")



if __name__ == "__main__" :
    main()










          

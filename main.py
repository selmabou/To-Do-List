from class_tasks import GESTION_TACHES

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
                to_do_list.Modifier_tache()

            elif choix == "5":
                break

            else:
                print (" OPTION INVALIDE !! ")    




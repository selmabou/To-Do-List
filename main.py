from class_tasks import tasks_manager

if __name__ == "__main__" :

    user = input(" Entrez votre nom d'utilisateur : ")   
    password = input(" Entrez votre mot de pass   : ")     

    if user == 'root'  and password == '123':
        to_do_list = tasks_manager()

        while True :
            print("\n >>>   APP GESTION DES TACHES   <<< ") 
            print(" 1. AJOUTER UNE TACHE ")
            print(" 2. SUPPRIMER UNE TACHE ")
            print(" 3. AFFICHER LISTE DES TACHES ")
            print(" 4. MODIFIER UNE TACHE ")
            print(" 5. QUITTER ")


            choice = input(" \n => CHOISISSEZ UNE OPTION : ")

            if choice == "1":
                to_do_list.add_task()

            elif choice == "2":
                to_do_list.delete_task()

            elif choice == "3":
                to_do_list.show_task()

            elif choice == "4":
                to_do_list.update_task()

            elif choice == "5":
                break

            else:
                print (" OPTION INVALIDE !! ")    




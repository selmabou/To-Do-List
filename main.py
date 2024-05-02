Taches = []

def ajouter_tache() :
    tache = input(str("saisir une tache .. "))
    Taches.append(tache)
    print(f"La tache : '{tache} , ajoute a la list .'")



def supprimer_tache (Taches , index):
    if index >= 0 and index < len(Taches):
        del Taches[index]
        print ("tache est supprimer")

    else:
        print("list des taches vide !!") 



          

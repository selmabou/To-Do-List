import csv 

class tasks_manager :
    def __init__(self):
        self.all_tasks = []
        self.load_data_csv()


    def add_task(self):
        self.show_task()
        task = input(" -> SAISIR VOTRE tache : ")
        if task :
            self.all_tasks.append(task)
            self.save_data_csv()
            print(" La tache ajoute avec succes .")
        else :
            print("Veuillez entrer une tache!! ") 



    def delete_task(self):
        self.show_task()
        task = int(input(" -> ENTREZ L'INDEX DU tache A SUPPRIMER : "))
        if 0 <= task and task < len(self.all_tasks) :
            del self.all_tasks[task]
            self.save_data_csv()
            
            print(" La tache supprimer avec succes .")
        else:
            print(" la tache non trouve !! ")  



    def show_task(self):
        if self.all_tasks :
            print(" Liste des tache : ")
            
            for index, mon_task in enumerate(self.all_tasks) :
                print(index,".", mon_task)

        else:
            print(" Aucun tache dans la liste !! ")

            
            

    def update_task(self):
        self.show_task()
        id = int(input(" Entrez l'index de l'ancien tache : "))
        nv_task = input(" Entrez la nouvelle tache  : ")
        if 0 <= id  and id < len(self.all_tasks):
            #id = self.all_tasks.index(Ancien_task)
            self.all_tasks[id] = nv_task   
            self.save_data_csv()
            

            print(" La tache a modifiee succes . ")   

        else :
            print(" La tache non trouve !! ")  



    def save_data_csv(self):
        with open('file_tasks.csv', 'w') as file:
            writer = csv.writer(file)
            for task in self.all_tasks :
                writer.writerow([task])



    def load_data_csv(self): 
        try:
            with open('file_tasks.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row :
                        self.all_tasks.append(row[0])
        except FileNotFoundError:
            pass


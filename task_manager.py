import csv
import tkinter as tk
from tkinter import ttk, messagebox

class TasksManager:
    def __init__(self, root):
        self.root = root
        self.all_tasks = []
        self.load_data_csv()

        # Login Interface
        self.login_frame = ttk.Frame(self.root, padding=10, style="Login.TFrame")
        self.login_frame.pack(pady=20)
        self.user_label = ttk.Label(self.login_frame, text="Username:", foreground="blue", font=("Arial", 12), style="Login.TLabel")
        self.user_label.pack()
        self.user_entry = ttk.Entry(self.login_frame, font=("Arial", 12))
        self.user_entry.pack()
        self.password_label = ttk.Label(self.login_frame, text="Password:", foreground="blue", font=("Arial", 12), style="Login.TLabel")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.pack()
        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login, style="Accent.TButton")
        self.login_button.pack()

    def login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        if user == 'root' and password == '123':
            self.login_frame.destroy()
            self.create_main_interface()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def create_main_interface(self):
        self.main_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.main_frame.pack(pady=20)

        # Buttons
        self.add_button = ttk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.delete_button = ttk.Button(self.main_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        self.show_button = ttk.Button(self.main_frame, text="Show Tasks", command=self.show_task)
        self.show_button.pack(pady=5)
        self.update_button = ttk.Button(self.main_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

    def add_task(self):
        if hasattr(self, "add_frame"):
            self.add_frame.destroy()


        if hasattr(self, "delete_frame"):
            self.delete_frame.destroy()

        if hasattr(self, "update_frame"):
            self.update_frame.destroy()    

        self.add_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.add_frame.pack(pady=20)
        self.show_task()
        task_label = ttk.Label(self.add_frame, text="Enter your task:", foreground="blue", font=("Arial", 12), style="Main.TLabel")
        task_label.pack()
        self.task_entry = ttk.Entry(self.add_frame, font=("Arial", 12))
        self.task_entry.pack()
        add_button = ttk.Button(self.add_frame, text="Add", command=self.add_task_to_list, style="Accent.TButton")
        add_button.pack()

    def add_task_to_list(self):
        task = self.task_entry.get()
        self.add_frame.destroy()
        if task:
            self.all_tasks.append(task)
            self.save_data_csv()
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        if hasattr(self, "delete_frame"):
            self.delete_frame.destroy()

        if hasattr(self, "update_frame"):
            self.update_frame.destroy()

        if hasattr(self, "add_frame"):
            self.add_frame.destroy()    

        self.delete_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.delete_frame.pack(pady=20)
        self.show_task()
        task_label = ttk.Label(self.delete_frame, text="Enter the index of task to delete:", foreground="blue", font=("Arial", 12), style="Main.TLabel")
        task_label.pack()
        self.task_index_entry = ttk.Entry(self.delete_frame, font=("Arial", 12))
        self.task_index_entry.pack()
        delete_button = ttk.Button(self.delete_frame, text="Delete", command=self.delete_task_from_list, style="Accent.TButton")
        delete_button.pack()

    def delete_task_from_list(self):
        task_index = int(self.task_index_entry.get())
        self.delete_frame.destroy()
        if 0 <= task_index < len(self.all_tasks):
            del self.all_tasks[task_index-1]
            self.save_data_csv()
            messagebox.showinfo("Success", "Task deleted successfully.")
            self.show_task()
        else:
            messagebox.showwarning("Warning", "Invalid task index.")

    def show_task(self):
        if hasattr(self, 'show_frame'):
            self.show_frame.destroy()

        self.show_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.show_frame.pack(pady=20)
        if self.all_tasks:
            task_label = ttk.Label(self.show_frame, text="List of Tasks:", foreground="blue", font=("Arial", 12), style="Main.TLabel")
            task_label.pack()
            for index, task in enumerate(self.all_tasks):
                task_info = ttk.Label(self.show_frame, text=f"{index+1}. {task}", font=("Arial", 10), style="Task.TLabel")
                task_info.pack(pady=2)
        else:
            task_label = ttk.Label(self.show_frame, text="No tasks in the list.", font=("Arial", 12), style="Main.TLabel")
            task_label.pack()

    def update_task(self):
        if hasattr(self, "update_frame"):
            self.update_frame.destroy()

        if hasattr(self, "delete_frame"):
            self.delete_frame.destroy()

        if hasattr(self, "add_frame"):
            self.add_frame.destroy()    

        self.update_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.update_frame.pack(pady=20)
        self.show_task()
        task_index_label = ttk.Label(self.update_frame, text="Enter the index of task to update:", foreground="blue", font=("Arial", 12), style="Main.TLabel")
        task_index_label.pack()
        self.task_index_entry = ttk.Entry(self.update_frame, font=("Arial", 12))
        self.task_index_entry.pack()
        new_task_label = ttk.Label(self.update_frame, text="Enter the new task:", foreground="blue", font=("Arial", 12), style="Main.TLabel")
        new_task_label.pack()
        self.new_task_entry = ttk.Entry(self.update_frame, font=("Arial", 12))
        self.new_task_entry.pack()
        update_button = ttk.Button(self.update_frame, text="Update", command=self.update_task_in_list, style="Accent.TButton")
        update_button.pack()

    def update_task_in_list(self):
        task_index = int(self.task_index_entry.get())
        new_task = self.new_task_entry.get()
        self.update_frame.destroy()
        if 0 <= task_index < len(self.all_tasks):
            self.all_tasks[task_index-1] = new_task
            self.save_data_csv()
            messagebox.showinfo("Success", "Task updated successfully.")
            self.show_task()
        else:
            messagebox.showwarning("Warning", "Invalid task index.")

    def save_data_csv(self):
        with open('file_tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.all_tasks:
                writer.writerow([task])

    def load_data_csv(self):
        try:
            with open('file_tasks.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.all_tasks.append(row[0])
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("460x600")
    
    # Custom styles
    root.tk_setPalette(background='#f0f0f0')
    root.option_add('*TLabel.Font', ('Arial', 10))
    root.option_add('*TButton.Font', ('Arial', 10))
    
    style = ttk.Style(root)
    style.configure("Accent.TButton", foreground="white", background="#0078d4", font=('Arial', 10))
    style.configure("Main.TFrame", background="#f0f0f0")
    style.configure("Login.TFrame", background="#f0f0f0")
    style.configure("Main.TLabel", foreground="black", font=('Arial', 10))
    style.configure("Login.TLabel", foreground="black", font=('Arial', 10))
    style.configure("Task.TLabel", foreground="black", font=('Arial', 10))
    
    app = TasksManager(root)
    root.mainloop()
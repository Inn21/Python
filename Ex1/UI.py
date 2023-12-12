import tkinter as tk
from tkinter import messagebox 
from Database import WorkerDatabase,Worker

class Interface():
    def __init__(self,window:tk.Tk) :
        self.window = window
        self.window.title("---=Worker Database=---")
        self.window.geometry("600x350")
        self.window.wm_maxsize(600,350)

        
        
        self.text = tk.StringVar()
        self.text.set("Hello")

        

        self.lable = tk.Label(self.window, textvariable=self.text, font=("Arial",12) ,width=50, height=15,relief=tk.GROOVE,bg="white" ,justify="left")        
        
        self.lable.pack(side= tk.TOP)    

        self.read_data()

        self.print_button = tk.Button(self.window,text="Вивести данні на екран",command=self.read_data)     
        self.print_button.pack(side= tk.LEFT,padx= 5)
        
        
        self.add_button = tk.Button(self.window,text="Додати обєкт",command=self.add)     
        self.add_button.pack(side= tk.LEFT,padx= 5)

        self.find_button = tk.Button(self.window,text="Знайти обєкти",command=self.find_data)     
        self.find_button.pack(side= tk.LEFT,padx= 5)

        self.remove_button = tk.Button(self.window,text="Видалити обєкт",command=self.remove_data)     
        self.remove_button.pack(side= tk.LEFT,padx= 5)

        self.diagram_button = tk.Button(self.window,text="Показати діаграму",command=self.show_diagram)       
        self.diagram_button.pack(side= tk.LEFT,padx= 5)
        


   


    def show_diagram(self):
        WorkerDatabase.Chart()

    def read_data(self):
        self.text.set(WorkerDatabase.Read())

    def add(self):
        self.add_win = tk.Tk()
        self.add_win.title("Додати")
        self.add_win.geometry("350x250")
    
       

       
        self.add_name = tk.Entry(self.add_win)
        self.add_name.pack(side= tk.TOP)
        
        name_lable = tk.Label(self.add_win,text="Ім'я")
        name_lable.pack(side= tk.TOP)


        self.add_surname = tk.Entry(self.add_win)
        self.add_surname.pack(side= tk.TOP)
        
        surname_lable = tk.Label(self.add_win,text="Прізвище")
        surname_lable.pack(side= tk.TOP)     

        
        departments = ["Software","Management","Cybersecurity","Analytics"]

        self.add_department = tk.StringVar(self.add_win)
        self.add_department.set("Software")

        department_menu = tk.OptionMenu(self.add_win, self.add_department,*departments)
        department_menu.pack(side= tk.TOP)

        department_lable = tk.Label(self.add_win,text="Департамент")
        department_lable.pack(side= tk.TOP)

        
        self.add_selary = tk.Entry(self.add_win)
        self.add_selary.pack(side= tk.TOP)
        
        selary_lable = tk.Label(self.add_win,text="Зарплатня")
        selary_lable.pack(side= tk.TOP)

        find_start_butt = tk.Button(self.add_win,text="Додати",command=self.try_to_add)     
        find_start_butt.pack(side= tk.BOTTOM)

        
        


    def try_to_add(self):   

            try:
                a = Worker(self.add_name.get(),self.add_surname.get(),self.add_selary.get(),self.add_department.get())
                WorkerDatabase.Add(a)
                messagebox.showinfo("Успіх", f"Працівник {a.Name} доданий в базу")                
                self.read_data()   
                self.add_win.destroy()
                
            except Exception as e:
                messagebox.showerror("Помилка", f"Дані введені некоректно!") 
                print(e)

            


    def find_data(self):
        self.find_win = tk.Tk()
        self.find_win.title("Пошук")

        self.find_win.geometry("350x150")

        self.search_key = tk.StringVar(self.find_win)
        self.search_key.set("id")

        types = ["id","Name","Surname","Salary","Department"]
        key_menu = tk.OptionMenu(self.find_win, self.search_key,*types)
        key_menu.pack(side= tk.TOP)

        key_lable = tk.Label(self.find_win,text="Виберіть поле по якому шукати")
        key_lable.pack(side= tk.TOP)
        
        self.selary_value = tk.Entry(self.find_win)
        self.selary_value.pack(side= tk.TOP)
        
        value_lable = tk.Label(self.find_win,text="Введіть значення яке шукати")
        value_lable.pack(side= tk.TOP)

        find_start_butt = tk.Button(self.find_win,text="Пошук",command=self.try_to_find)     
        find_start_butt.pack(side= tk.BOTTOM)

        self.find_win.mainloop
        
    def try_to_find(self):   
            key = self.search_key.get()
            value = self.selary_value.get()

            result_text = f"----= Objects whore '{key}' = '{value}' =----\n"
            Workers = WorkerDatabase.Search(key,value)
            for i in Workers:                
                result_text+=(str(i.Name)+", "+str(i.Surname)+", "+str(i.Selery)+", "+str(i.Departmen)+'\n')            

            self.text.set(result_text)            
            self.find_win.destroy()
        
    def remove_data(self):
        self.remove_win = tk.Tk()
        self.remove_win.title("Видалення")

        self.remove_win.geometry("350x150")

        self.remove_index = tk.Entry(self.remove_win, width=5)
        self.remove_index.pack(side= tk.TOP)        

        key_lable = tk.Label(self.remove_win,text="Виберіть індекс елемента для видалення")
        key_lable.pack(side= tk.TOP)

        find_start_butt = tk.Button(self.remove_win,text="Видалити",command=self.try_to_remove)     
        find_start_butt.pack(side= tk.BOTTOM)

        self.find_win.mainloop
        
    def try_to_remove(self):   
            id = int(self.remove_index.get())

            if(WorkerDatabase.Remove(id)):
                messagebox.showinfo("Успіх", f"Елемент з id {id} видалено")
            else:
                messagebox.showerror("Помилка", f"Елемент з id {id} не існує!") 
            self.read_data()   
            self.remove_win.destroy()
        
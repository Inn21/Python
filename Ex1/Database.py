import csv
import pandas as pd
from worker import Worker
import matplotlib.pyplot as plt
import random

filename = 'Data.csv'

#UnitTests!!!

def GetMaxIndex():     
        global filename
        with open(filename,newline='') as csv_file:
            reafer = csv.DictReader(csv_file,delimiter=',')
            maxId = 0
            UsedID = []
            for row in reafer:
                if(row["id"].isnumeric()):
                    maxId = max(int(row['id']) , maxId ) 
                    UsedID.append(int(row['id']))

            freeId  = list(range(maxId+2))
            for i in UsedID:
                freeId.pop(freeId.index(i))                
            return freeId[0]


class WorkerDatabase():
    global filename



    def __dec_sort(func):
        def wrapper(Key):
            print(f"----= Sorted by header '{Key}' =----")
            func(Key)
            WorkerDatabase.Read()            
        return wrapper

    def __dec_serarch(func):
        def wrapper(Key,Vall):
            start = f"----= Objects whore '{Key}' = '{Vall}' =----"
            print(start)
            return   func(Key,Vall)
             
                    
        return wrapper
    
    @staticmethod
    def Add(worker:Worker):        
        global filename
        f = open(filename, 'a',newline='')
        writer = csv.writer(f)
        row =  [GetMaxIndex() , worker.Name, worker.Surname , worker.Selery , worker.Departmen]
        writer.writerow(row)        
        f.close()
            
    @staticmethod
    def Read():
        global filename        
        r = pd.read_csv(filename, index_col='id')  
        print(r)
        return r
        
    def Clear():
        f = open(filename, "w+")
        f.write("id,Name,Surname,Salary,Department\n")
        f.close()
   
    @staticmethod
    def Edit(id:int, key:str, value:str):
        global filename  
        with open(filename,newline='') as csv_file:
            r = pd.read_csv(filename, index_col='id')  
            reafer = csv.DictReader(csv_file,delimiter=',')
            for row in reafer:
                if(row["id"].isnumeric() and int(row["id"]) == id):
                    r.loc[id,key] = value                    
                    r.to_csv(filename,index=True)
    
    @staticmethod
    def Remove(id:int = -1):        
            global filename            
            r = pd.read_csv(filename, index_col='id') 
            try:
                if(id == -1):
                    r = r.drop(r.index[id]) 
                else:
                    r = r.drop(id)      
                r.to_csv(filename,index=True)
                return True
            except:
                print("Wrong ID")
                return False
 
    @__dec_sort
    def Sort(key:str = 'id'):   
        global filename     
        r = pd.read_csv(filename, index_col='id')  
        if(key == 'id'):
            r = r.sort_index()
        elif(key in r.keys()):    
            r = r.sort_values(key) 
        r.to_csv(filename,index=True)
  
    @__dec_serarch
    def Search(key:str, value:str):
        global filename
        with open(filename,newline='') as csv_file:
            r = pd.read_csv(filename, index_col='id')  
            reafer = csv.DictReader(csv_file,delimiter=',')
            i = 0
            Workers = []
            for row in reafer:
                if(row[key] == value):
                    i+=1
                    args = []
                    print(f"{i})",end="")
                    vals = list(row.values())
                    for i in range(1,len(vals)):
                        print(f"{str(vals[i])},",end=" ")
                        args.append(str(vals[i]))
                    a = Worker(args[0],args[1],args[2],args[3])
                    Workers.append(a)
                    print("") 
                    r.to_csv(filename,index=True)
            # csv_file.close()
            return Workers

    @staticmethod
    def Chart():
        r = pd.read_csv(filename, index_col='id')  
        items = {}
        for i in list(r.get("Department")):
            if i in items:
                items[i]+=1
            else: 
                items[i]=1

        print(items.values(),items.keys())
        


        series = pd.Series(list(items.values()), index=list(items.keys()))
       

        series.plot.pie(autopct="%.0f%%" ,explode = tuple([0.01]*len(items.values())),legend = True )
        plt.title("Departments")
        plt.show()
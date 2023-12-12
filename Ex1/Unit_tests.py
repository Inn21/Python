import unittest
import Database
from Database import WorkerDatabase

from worker import Worker



class Test(unittest.TestCase):

    def test_Search(self):
        res = WorkerDatabase.Search("Name","Atext")
        self.assertTrue(res==[])

    def test_Add(self):
        a = Worker("Atext")
        WorkerDatabase.Add(a)
        res = WorkerDatabase.Search("Name","Atext")
        self.assertTrue(res[0]==a)


    def test_Edit(self):
        res1 = WorkerDatabase.Search("id","0")
        WorkerDatabase.Edit(0,"Name","Btext")
        res2 = WorkerDatabase.Search("id","0")
        
        print(res1,res2)
        self.assertTrue(res1[0]!=res2[0])

    def test_Remove(self):
        res1 = WorkerDatabase.Search("id","0")
        WorkerDatabase.Remove(0)
        res2 = WorkerDatabase.Search("id","0")
        self.assertTrue(res1!=res2)

        
    

if __name__ == "__main__":    
    Database.filename = "Unit_tests.csv"
    WorkerDatabase.Clear()
    unittest.main()

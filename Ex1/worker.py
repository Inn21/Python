import Database as db

class Worker():

    _MaxId = 0
    def _GetMaxID(self):        
        self._MaxId =  db.GetMaxIndex()

    def __init__(self, name = "Name", Sur="Sur", Sel="Sel", Dep="Dep"):
        self._GetMaxID()
        # self._MaxId += 1
        self.__id = str(self._MaxId)
        self.Name = name
        self.Surname = Sur
        self.Selery = Sel
        self.Departmen = Dep

    def __eq__(self, __o: object) -> bool:
        return self.Name == __o.Name and self.Surname == __o.Surname and self.Selery == __o.Selery and self.Departmen == __o.Departmen
    
    def ID(self):
        return self.__id

    
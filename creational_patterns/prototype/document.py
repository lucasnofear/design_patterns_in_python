import copy 
from interface_prototype import IProtoType

class Document(IProtoType):

    def __init__(self, name, l):
        self.name = name
        self.list = l 
    
    def clone(self, mode):
        " This clone method uses different copy techniques"
        if mode == 1:
            # 1 level shallow copy 
            doc_list = self.list 
        if mode == 2:
            # 2 level shallow copy
            doc_list = copy.copy(self.list)
        if mode == 3:
            # recursive deep copy
            doc_list = copy.deepcopy(self.list)
        
        return type(self)(self.name, doc_list)
    
    def __str__(self):
        " Overriding the default __str__ method for our object."
        return f"{id(self)}\tname={self.name}\tlist={self.list}"

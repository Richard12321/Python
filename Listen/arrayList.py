class arrayList():
    def __init__(self):
        self.arrayList = []
    
    #O: 1
    def getLastElem(self):
        return self.arrayList[-1]

    #O: 1 
    def append(self, o):
        self.arrayList.append(o)
    
    #O: n
    def printAll(self):
        print(self.arrayList)

    #O: 1
    def getElem(self, index):
        return self.arrayList[index]
    
    #O: 1
    def length(self):
        return len(self.arrayList)
    
    #O: 1
    def clear(self):
        self.clear()
    
    #O: 1
    def delFirst(self):
        self.arrayList.pop(1)

    #O: 1
    def pop(self, index):
        self.arrayList.pop(index)

    #O: n
    def remove(self, value):
        self.arrayList.remove(value)
    
    #O: n
    def index(self, value):
        self.arrayList.index(value)

    #O: n
    def reverse(self):
        self.arrayList.reverse()
    
    #O: 1
    def copy(self):
        return self.copy()

    #O: n
    def count(self, value):
        self.arrayList.count(value)

    #O: length(iterable)
    def extend(self, iterable):
        self.arrayList.extend(iterable)

    #O: 1
    def insert(self, value, index):
        self.arrayList.insert(index, value)
    
    #O: n*log(n)
    def sort(self):
        self.arrayList.sort()
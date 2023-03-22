import copy

class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None
        self.prevElem = None

class DoppeltVerketteteListe:
    def __init__(self):
        self.firstElem = None
        self.lastElem = None

    #O: 1
    def getLastElem(self):
        return self.lastElem

    #O: 1 
    def append(self, o):
        le = ListElement(o)
        if self.firstElem == None:
            self.firstElem = le
            self.lastElem = le
        else:
            le.prevElem = self.lastElem
            self.lastElem.nextElem = le
            self.lastElem = le
    
    #O: n
    def printAll(self):
        le = self.firstElem
        while le != None:
            print(le.obj)
            le = le.nextElem

    #O: n
    def getElem(self, index):
        le = self.firstElem
        i = 0
        while le != None:
            if i == index:
                return le.obj
            le = le.nextElem
            i += 1
        print("Index out of Bound")
    
    #O: n
    def length(self):
        le = self.firstElem
        if le == None:
            return 0
        amount = 1
        while le.nextElem != None:
            amount += 1
            le = le.nextElem
        return amount
    
    #O: 1
    def clear(self):
        self.firstElem = None
    
    #O: 1
    def delFirst(self):
        self.firstElem = self.firstElem.nextElem
    
    #O: n
    def pop(self, index):
        if index == 0:
            self.delFirst()
            return 
        le = self.firstElem
        i = 0
        while le != None:
            if i == index:
                le.prevElem.nextElem = le.nextElem
                return 
            le = le.nextElem
            i += 1
        print("Index Out of Bound")

    #O: n
    def remove(self, value):
        le = self.firstElem
        while le != None:
            if value == le.obj and le.prevElem != None:
               le.prevElem.nextElem = le.nextElem
               return
            elif value == le.obj and le.prevElem == None:
                self.delFirst() 
                return
            le = le.nextElem
        print("Value not in list")
    
    #O: n
    def index(self, value):
        le = self.firstElem
        i = 0
        while le != None:
            if value == le.obj:
               return i
            le = le.nextElem
            i += 1
        print("Value not in list")

    #O: n
    def reverse(self):
        oldList = copy.deepcopy(self)
        revList = DoppeltVerketteteListe()
        while oldList.length() > 0:
            revList.append(oldList.getLastElem().obj)
            oldList.pop(oldList.length()-1)
        return revList
    
    #O: 1
    def copy(self):
        return copy.deepcopy(self)

    #O: n
    def count(self, value):
        le = self.firstElem
        i = 0
        while le != None:
            if value == le.obj:
               i += 1
            le = le.nextElem
        return i    

    #O: length(iterable)
    def extend(self, iterable):
        for i in iterable:
            self.append(i)  

    def insert(self, value, index):
        le = self.firstElem
        i = 0
        prevElem = None
        newElem = ListElement(value)
        while le != None:
            if i == index and prevElem != None and i != self.length()-1:
                prevElem.nextElem = newElem
                newElem.nextElem = le.nextElem
                return
            elif i == index and prevElem == None:
                newElem.nextElem = le
                self.firstElem = newElem
                return
            elif i == index and prevElem != None and i == self.length()-1:
                lastElement = self.getLastElem().obj
                self.pop(self.length()-1)
                self.append(value)
                self.append(lastElement)
            prevElem = le
            le = le.nextElem
            i+=1
        print("Index out of Bound")
        

def main():
    liste = DoppeltVerketteteListe()
    for i in range(10):
        liste.append(i)
    print(liste.length())
    print()
    liste.printAll()
    print()
    revList = liste.reverse()
    print()
    revList.printAll()
    print()
    print(liste.count(2))
    print()
    liste.extend([10,11,12,13])
    liste.printAll()
    print()
    liste.insert(5, 12)
    liste.printAll()


if __name__ == "__main__":
    main()

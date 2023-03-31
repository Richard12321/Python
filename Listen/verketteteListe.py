import copy

class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None

class EinfachVerketteteListe:
    def __init__(self):
        self.firstElem = None

    #O: n
    def getLastElem(self):
        le = self.firstElem
        while le.nextElem != None:
            le = le.nextElem
        return le

    #O: n
    def append(self, o):
        if self.firstElem == None:
            self.firstElem = ListElement(o)
        else:
            lastElem = self.getLastElem()
            lastElem.nextElem = ListElement(o)
    
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
        prevElem = None
        while le != None:
            if i == index:
                prevElem.nextElem = le.nextElem
                return 
            prevElem = le
            le = le.nextElem
            i += 1
        print("Index Out of Bound")

    #O: n
    def remove(self, value):
        le = self.firstElem
        prevElem = None
        while le != None:
            if value == le.obj and prevElem != None:
               prevElem.nextElem = le.nextElem
               return
            elif value == le.obj and prevElem == None:
                self.delFirst() 
                return
            prevElem = le
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
        revList = EinfachVerketteteListe()
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

    #O: n
    def insert(self, value, index):
        le = self.firstElem
        i = 0
        prevElem = None
        newElem = ListElement(value)
        while le != None:
            if i == index and prevElem != None and i != self.length()-1:
                newElem.nextElem = le
                prevElem.nextElem = newElem
                return
            elif i == index and prevElem == None:
                newElem.nextElem = le
                self.firstElem = newElem
                return
            elif i == index and prevElem != None and i == self.length()-1:
                self.append(value)
                return
            prevElem = le
            le = le.nextElem
            i+=1
        print("Index out of Bound")

    #O: n^2 Insertion Sort
    def sort(self):
        for i in range(self.length()):
            if i == 0:
                continue
            le = self.getElem(i)
            j = i
            while (le < self.getElem(j-1) and j > 0):
                j = j-1
            self.insert(le, j)
            self.pop(i+1)
        

def main():
    liste = EinfachVerketteteListe()
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
    liste.insert(5, 10)
    liste.printAll()
    print()
    liste.sort()
    liste.printAll()

    print("---------------------------------------------")
    l = EinfachVerketteteListe()
    l.extend([5,23,8,56,12])
    l.printAll()
    print()
    l.sort()
    l.printAll()


if __name__ == "__main__":
    main()

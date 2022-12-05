class company():
    def __init__(self):
        pass

class person():
    def __init__(self, gender, firstName, lastName, department):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.department = department

class employee(person):
    def __init__(self, gender):
        super().__init__(gender)

class manager(person):
    def __init__(self, gender, firstName, lastName, department):
        super().__init__(gender, firstName, lastName, department)

class department():
    def __init__(self, boss):
        self.boss = boss

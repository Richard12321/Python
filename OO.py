from enum import Enum

class gender(Enum):
    Undefined = 0
    Male = 1
    Female = 2

class company():
    def __init__(self, employees, departments):
        self.employees = employees
        self.departments = departments
    
    def genderRatio(self):
        cnt = {
            gender.Female: 0,
            gender.Male: 0,
            gender.Undefined: 0
        }
        for i in self.employees:
            cnt[i.gender] += 1
        return (list(cnt.keys()), list(map(lambda x: x / len(self.employees), cnt.values())))
    
    def cntEmployees(self):
        return len(self.employees)
    
    def cntManager(self):
        return len(list(filter(lambda x: isinstance(x, manager), self.employees)))

    def cntDepartments(self):
        return len(self.departments)

    def biggestDepartment(self):
        cnt = {}
        for i in self.departments:
            cnt[i.name] = 0
        for i in self.employees:
            cnt[i.department.name] += 1
        return cnt

class person():
    def __init__(self, gender, firstName, lastName):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName

class employee(person):
    def __init__(self, gender, firstName, lastName, department):
        self.department = department
        super().__init__(gender, firstName, lastName)

class manager(employee):
    def __init__(self, gender, firstName, lastName, department):
        super().__init__(gender, firstName, lastName, department)

class department():
    def __init__(self, name):
        self.name = name

def main():
    marketing = department("Marketing")
    distribution = department("Distribution")

    e1 = employee(gender.Male, "Richard", "Zallinger", marketing)
    e2 = employee(gender.Female, "Werner", "Mair", distribution)
    e3 = employee(gender.Male, "Dominik", "Vötter", marketing)
    e4 = employee(gender.Undefined, "Fabian", "Strasser", marketing)
    m1 = manager(gender.Male, "Miguel", "Mayrhofer", distribution)
    m2 = manager(gender.Female, "Lucas", "Schebor", marketing)

    com = company([e1, e2, e3, e4, m1, m2], [marketing, distribution])
    print(com.genderRatio())

if __name__ == "__main__":
    main()
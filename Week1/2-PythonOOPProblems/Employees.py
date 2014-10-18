class Employees:

     def __init__(self, name, hours):
        self.name = name
        self.hours = hours


class HourlyEmployee(Employees):
    SALARY = 2
    def __init__(self, name, hours):
        super().__init__(self, name, hours)

    def salary(self):
        return SALARY 


class SalariedEmployee(Employees):
     SALARY = 5
    def __init__(self, name, hours):
        super().__init__(self, name, hours)


class Manager(Employees):
     SALARY = 10
    def __init__(self, name, hours):
        super().__init__(self, name, hours)

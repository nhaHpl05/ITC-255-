

class Employee():
    def __init__(self, EmployeeName, EmployeeEmail, Datehire):
        self.EmployeeName = EmployeeName
        self.EmployeeEmail = EmployeeEmail
        self.Datehire = Datehire
    
    def getEmployeeName(self):
        return self.EmployeeName

    def getEmployeeEmail(self):
        return self.EmployeeEmail

    def getDatehire(self):
        return self.Datehire

    def __str__(self):
        return self.EmployeeName
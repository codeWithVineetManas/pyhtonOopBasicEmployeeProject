# Parent Class Employee
class Employee:
    def __init__(self,name,age,perDayPay,absentDays):
        self.name = name
        self.age = age
        self.perDayPay = perDayPay
        self.absentDays = absentDays

    def show_details(self):
        print(f"Name: {self.name}")    
        print(f"Age: {self.age}")    
        print(f"Salary: {30 * self.perDayPay}")    
        print(f"Absent Days: {self.absentDays}")  

    def getSalary(self):
        salary      = 30 * self.perDayPay
        absentDays  = self.absentDays * self.perDayPay
        totalSalary = salary - absentDays

        return totalSalary

        
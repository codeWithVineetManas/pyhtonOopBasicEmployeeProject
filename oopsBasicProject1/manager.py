# child class from parent class Employee

from employee import Employee

class Manager(Employee):
    def __init__(self, name, age, perDayPay, absentDays,projectCompted,teamSize):
        super().__init__(name, age, perDayPay, absentDays)
        self.projectCompted =   projectCompted
        self.teamSize       =   teamSize

    def show_details(self):
        super().show_details()   
        salary = super().getSalary()
        bonus = self.projectCompted * 1000
        total_salary = salary + bonus

        print(f"Total Bonus {bonus}")
        print(f"Total Salary {total_salary}")
        print(f"Team Size {self.teamSize}")
        print("--------------------")


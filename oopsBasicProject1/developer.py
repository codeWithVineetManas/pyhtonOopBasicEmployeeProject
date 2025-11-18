# child class from parent class Employee

from employee import Employee

class Developer(Employee):
    def __init__(self, name, age, perDayPay, absentDays,projectCompted,programmingLanguage):
        super().__init__(name, age, perDayPay, absentDays)
        self.projectCompted =   projectCompted
        self.programmingLanguage       =   programmingLanguage

    def show_details(self):
        super().show_details()   
        salary = super().getSalary()
        bonus = self.projectCompted * 1500
        total_salary = salary + bonus

        print(f"Total Bonus {bonus}")
        print(f"Total Salary {total_salary}")
        print(f"Programming Language  {self.programmingLanguage}")


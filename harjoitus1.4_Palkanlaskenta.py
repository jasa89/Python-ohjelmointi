class PayrollSystem:
    def calculate_payroll(self, employees):
        for index, employee in enumerate(employees, start=1):
            print(f"Palkkalaskelma\n{'='*14}")
            print(f"Henkilölle: {index} - {employee.name}")
            print(f"- Maksetaan: {employee.calculate_salary()}\n")

class Employee:
    def __init__(self, name):
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

def main():
    employees = []
    
    while True:
        name = input("Anna työntekijän nimi: (0 lopetus): ")
        if name == '0':
            break
        monthly_salary = float(input("Anna kuukausipalkka: "))
        employee = SalaryEmployee(name, monthly_salary)
        employees.append(employee)
    
    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll(employees)

if __name__ == "__main__":
    main()
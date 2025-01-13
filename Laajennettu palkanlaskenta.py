# Exercise  

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Palkkalaskelma') 
            print('==============')
            print(f'Henkilölle: {employee.id} - {employee.name}') 
            print(f'- Maksetaan: {employee.calculate_salary()}') 
            print('')
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def ask_name(self):
        try:
          self.name = str(input("Anna työntekijän nimi:"))
        except:
          self.name = ''
class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        
        self.monthly_salary = int(monthly_salary)
    def ask_salary(self):
        try: 
          self.monthly_salary = int(input("Anna kuukausipalkka:"))
        except:
          self.monthly_salary = 0    

    def calculate_salary(self):
        return self.monthly_salary
class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
       
        self.hour_rate = float(hour_rate)
        self.hours_worked = float(hours_worked)

    def ask_salary(self):
        try:
            self.hours_worked = float(input("Anna tehdyt tunnit:"))
            self.hour_rate = float(input("Anna tuntipalkka:"))
        except:
            self.hours_worked = 0
            self.hour_rate = 0    

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        
        self.commission = float(commission)

    def ask_salary(self):
        super().ask_salary()  # Kysyy kuukausipalkan
        try:
            self.commission = float(input("Anna komissio: "))
        except:
            self.commission = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission

employees = []
id = 1
while True:
  salarytype = int(input("Anna palkkatyyppi:\n(1) Kuukausi\n(2) Tunti\n(3) Komissio\n(0) Lopeta\n"))
  if salarytype == 1:
      employee = SalaryEmployee(id,'',0)
      SalaryEmployee.ask_name(employee)
      SalaryEmployee.ask_salary(employee)
      employees.append(employee)
      id += 1
  elif salarytype == 2:
      employee = HourlyEmployee(id,'',0,0)
      HourlyEmployee.ask_name(employee)
      HourlyEmployee.ask_salary(employee)
      employees.append(employee)
      id += 1
  elif salarytype == 3:
      employee = CommissionEmployee(id,'',0,0)
      CommissionEmployee.ask_name(employee)
      CommissionEmployee.ask_salary(employee)
      employees.append(employee)
      id += 1
  
   
 
  elif salarytype == 0:
      break
  else:
      print("Virheellinen valinta.")

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
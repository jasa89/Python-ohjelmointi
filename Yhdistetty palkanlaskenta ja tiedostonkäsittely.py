import csv

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def ask_name(self):
        try:
            self.name = str(input("Anna työntekijän nimi:"))
        except:
            self.name = ''

    def calculate_salary(self):
        pass


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

    def to_csv_row(self):
        return [self.id, self.name, 'M', self.monthly_salary]


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

    def to_csv_row(self):
        return [self.id, self.name, 'H', self.hour_rate, self.hours_worked]


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.commission = float(commission)

    def ask_salary(self):
        super().ask_salary()
        try:
            self.commission = float(input("Anna komissio:"))
        except:
            self.commission = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission

    def to_csv_row(self):
        return [self.id, self.name, 'C', self.monthly_salary, self.commission]


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        # Avoid adding duplicate employees by ID
        if any(emp.id == employee.id for emp in self.employees):
            print(f"Työntekijä ID: {employee.id} on jo olemassa.")
        else:
            self.employees.append(employee)

    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for emp in self.employees:
                writer.writerow(emp.to_csv_row())
        print(f"{len(self.employees)} työntekijä(ä) lisätty tiedostoon {filename}")

    def read_from_file(self, filename):
        self.employees = []  # Clear existing employees
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    id = int(row[0])
                    name = row[1]
                    if row[2] == 'M':
                        employee = SalaryEmployee(id, name, row[3])
                    elif row[2] == 'H':
                        employee = HourlyEmployee(id, name, row[3], row[4])
                    elif row[2] == 'C':
                        employee = CommissionEmployee(id, name, row[3], row[4])
                    else:
                        continue
                    self.add_employee(employee)
            print(f"{len(self.employees)} työntekijä(ä) luettu tiedostosta {filename}")
        except FileNotFoundError:
            print(f"Tiedostoa {filename} ei löydy.")

    def print_payroll(self):
        for employee in self.employees:
            print('Palkkalaskelma')
            print('==============')
            print(f'Henkilölle: {employee.id} - {employee.name}') 
            print(f'- Maksetaan: {employee.calculate_salary()}')
            print('')


def main():
    payroll_system = PayrollSystem()

    while True:
        print("\n(1) Lisää työntekijöitä")
        print("(2) Kirjoita työntekijät tiedostoon")
        print("(3) Lue työntekijät tiedostosta")
        print("(4) Tulosta palkkalaskelma")
        print("(0) Lopeta")
        action = int(input("\nValitse toiminto: "))

        if action == 1:
            while True:
                print("\nAnna palkkatyyppi:")
                print("(1) Kuukausi")
                print("(2) Tunti")
                print("(3) Komissio")
                print("(0) Lopeta")
                salarytype = int(input())

                if salarytype == 1:
                    employee = SalaryEmployee(len(payroll_system.employees) + 1, '', 0)
                    employee.ask_name()
                    employee.ask_salary()
                    payroll_system.add_employee(employee)
                elif salarytype == 2:
                    employee = HourlyEmployee(len(payroll_system.employees) + 1, '', 0, 0)
                    employee.ask_name()
                    employee.ask_salary()
                    payroll_system.add_employee(employee)
                elif salarytype == 3:
                    employee = CommissionEmployee(len(payroll_system.employees) + 1, '', 0, 0)
                    employee.ask_name()
                    employee.ask_salary()
                    payroll_system.add_employee(employee)
                elif salarytype == 0:
                    break
                else:
                    print("Virheellinen valinta.")
        
        elif action == 2:
            payroll_system.write_to_file('employee.csv')
        
        elif action == 3:
            payroll_system.read_from_file('employee.csv')
        
        elif action == 4:
            payroll_system.print_payroll()
        
        elif action == 0:
            print("Palvelu suljetaan, kiitos.")
            break
        
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()
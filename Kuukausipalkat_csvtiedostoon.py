# Exercise

def my_split(sentence, sep):
  lst = []
  tmp = ''
  for c in sentence:
    if c == sep:
        lst.append(tmp)
        tmp = ''
    else:
        tmp += c
  if tmp:
    lst.append(tmp)

  return(lst)


def my_join(lst,sep):
  mystr = ''
  for elem in lst[0:-1]:
      mystr += str(elem) + str(sep)
  mystr += str(lst[-1])

  return(mystr)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
    

while True:
    print("(1) Lisää työntekijöitä listaan\n(2) Kirjoita työntekijät tiedostoon\n(3) Lue työntekijät tiedostosta\n(4) Tulosta työntekijät\n(0) Lopeta\n")
    selection = int(input("Valitse toiminto: "))
    if selection == 1:
        salary_employees = []
        name = " "
        id = 1
        while name != '0':
          name = str(input("Anna työntekijän nimi (0 lopetus):"))
          if name != '0': 
            try: 
              salary = int(input("Anna kuukausipalkka:"))
            except:
              salary = 0    
            salary_employees.append(SalaryEmployee(id,name,salary))
            id += 1

    elif selection == 2:
        with open("salary_employee.csv", "w") as file:
            for employee in salary_employees:
                line = my_join([employee.id, employee.name, employee.monthly_salary], ",")
                file.write(line + "\n")
        print(len(salary_employees) ," työntekijä(ä) lisätty tiedostoon salary_employee.csv")
        
    elif selection == 3:
        salary_employees = []
        try:
            file = open("salary_employee.csv", "r")
            lines = file.readlines()  
            file.close()  
            for line in lines:
                id, name, monthly_salary = my_split(line.strip(), ",")
                salary_employees.append(SalaryEmployee(int(id), name, int(monthly_salary)))
                print(len(salary_employees) ," työntekijä(ä) luettu tiedostosta salary_employee.csv")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")

    elif selection == 4:
        for employee in salary_employees:
          print("Id:",employee.id, "Nimi:", employee.name, "Kuukausipalkka:", employee.monthly_salary)

    elif selection == 0:
        print("Palvelu suljetaan, kiitos.")
        break
    else:
        print("Virheellinen valinta.")


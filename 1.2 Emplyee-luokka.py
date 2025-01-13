class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def main():
    employees = []
    id_counter = 1
    
    while True:
        name = input("Anna työntekijän nimi: (0 lopetus):")
        if name == '0':
            break
        employees.append(Employee(id_counter, name))
        id_counter += 1

    for employee in employees:
        print(f"Id: {employee.id} Nimi: {employee.name}")

if __name__ == "__main__":
    main()
def bubble_sort(nums):
    n = len(nums)
    # Outer loop for number of passes
    for i in range(n - 1):
        # Inner loop for each pass
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Pääohjelma
if __name__ == "__main__":
    num_count = int(input("Anna lajiteltavien numeroiden lukumäärä: "))
    nums = []
    
    # Pyydä käyttäjältä numerot ja tallenna ne listalle
    for i in range(num_count):
        num = int(input(f"Anna taulukon {i} numero: "))
        nums.append(num)
    
    # Käytä bubble_sort -funktiota järjestämään numerot
    bubble_sort(nums)
    
    # Tulosta järjestetty lista
    print("Lajiteltu lista nousevassa järjestyksessä:", nums)
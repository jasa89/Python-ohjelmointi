# Exercise


def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


a = []
number = int(input("Anna lajiteltavien numeroiden lukumäärä : "))
for i in range(number):
    value = int(input("Anna taulukon %d numero : " %i))
    a.append(value)
print("Lajiteltu lista nousevassa järjestyksessä: ", bubble_sort(a))

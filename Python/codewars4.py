size_nums = int(input("Add size of numbers: "))
massive = []
counter = 0
list1 = []


for i in range(size_nums):
    nums = int(input("Add your number: "))
    massive.append(nums)

target = int(input("Add your target number: "))
massive.sort()

for i in massive:
    if i != target:
        target = i


print(massive)

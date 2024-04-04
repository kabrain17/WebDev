nums = {
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1
}

num = str(input('Add a Roman Number: '))
res = 0

for i in range(len(num)):
    if i > 0 and nums[num[i]] > nums[num[i - 1]]:
        res += nums[num[i]] - 2 * nums[num[i - 1]]
    else:
        res += nums[num[i]]

print(f"The decimal equivalent of {num} is {res}")
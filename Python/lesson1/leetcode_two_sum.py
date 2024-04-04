nums = list(input())
target = int(input())

values = {}
for idx, value in enumerate(nums):
    if target - value in values:
        print([values[target - value], idx])
    else:
        values[value] = idx



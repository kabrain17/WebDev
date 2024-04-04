def calculate_sum(nums, sum_of_nums):
    if not nums:
        return sum_of_nums
    else:
        sum_of_nums += nums[0]
        del nums[0]
    
        return calculate_sum(nums, sum_of_nums)

res = calculate_sum([1, 2, 3, 4], 10)
print(res)


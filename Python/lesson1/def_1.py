def sum_of_range(start, end):
    if start > end:
        start, end = end, start 
    sum = 0
    
    for i in range(start, end):
        sum += i
    return sum

a = sum_of_range(5, 20)
print(a)

def sum_range(start, end):
    if start > end:
        start, end = end, start 
    s = 0

    for i in range(start, end+1):
        s += i
    return s

a, b = map(int, input().split())
res = sum_range(a, b)
print(res)

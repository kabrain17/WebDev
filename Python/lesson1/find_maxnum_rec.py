def find_max(arr, max_num = None):
    if max_num is None:
        max_num = arr.pop()
    current = arr.pop()
    if current > max_num:
        max_num = current
    if arr:
        return find_max(arr, max_num)
    return max_num


list1=[1,2,3,4,2]
result = find_max(list1)
print(result)
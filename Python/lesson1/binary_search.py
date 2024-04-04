a = list(map(int, input().split()))
a.sort()
print(a)
 
value = int(input())
 
left = 0 # вводим переменную для поиска слева
right = len(a) - 1 # len функция возвращающая кол-во переменных в списке
value_index = -1 
iterations = 0

while left <= right: #poka u nas est otrezok [left,...,right] 
    iterations += 1
    mid = (left + right) // 2
    if a[mid] < value:
        left = mid + 1
    elif a[mid] > value:
        right = mid - 1
    elif a[mid] == value:
        value_index = mid
        break

print("iteratinos: " + str(iterations))
if value_index == -1:
    print("no such number") 
else:
    print("exists")
    print("index: " + str(value_index))

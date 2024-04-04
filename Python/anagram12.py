test1 = input()
original = input()

test1.lower()
original.lower()
list1 = []
list2 = []

for i in test1:
    list1.append(i)
for j in original:
    list2.append(j)

if len(list1) != len(list2):
    print(False)
else:
    list1_sort = list1.sort()
    list2_sort = list2.sort()
    if list1 == list2:
        print(True)
    else:
        print(False)


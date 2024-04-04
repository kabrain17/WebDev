n = int(input())
sum = []
for i in range(n):
    if i%2 == 0:
        sum.append(i)

tet = open('text.txt', 'r+')
tet.write(str(sum))

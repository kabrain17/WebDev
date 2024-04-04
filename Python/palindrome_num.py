n = int(input())
d = {}

for i in range(n):
    age = int(input())
    gender = input()

    if gender == 1:
        d.fromkeys(age)

print(d)





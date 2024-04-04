n = 6
mas = [4, 5, 7, 8, 9, 10]
count = 0

for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]

print(mas)
print(f"Количество перестановок: {count} ")
    
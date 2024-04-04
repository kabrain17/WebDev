while True: 
    what = input("Choose your operation (+,-,*,/): ")
    if what == "stop":
        break

    a = float(input ("Add first number: "))
    b = float(input("Add second number: "))

    if what == "+": 
        c = a + b
        print("Result: " + str(c))

    elif what == "-":
        c = a - b
        print("Result: " + str(c))

    elif what == "*":
        c = a * b
        print("Result: " + str(c))

    elif what == "/":
        c = a / b
        print("Result: " + str(c))

    else: 
        print("Wrong operaton!")


my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

result = sorted(my_dict, key=my_dict.get,  reverse=True)[:3]

print(result)


while True:
    what = input("Choose your operation: ")
    if what == "stop":
        break

    first_number = float(input("Add your first number: "))
    second_number = float(input("Add your second number: "))

    if what == "+":
        result = first_number + second_number
        print("Result: " + str(result))

    elif what == "-":
        result = first_number - second_number
        print("Result: " + str(result))

    elif what == "*":
        result = first_number * second_number
        print("Result: " + str(result))

    elif what == "/":
        result = first_number / second_number
        print("Result: " + str(result))

    else:
        print("Wrong operation!")


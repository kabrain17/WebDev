def transfer(size):
    if size[-1].upper() == "L":
        return 3
    elif size[-1].upper() == "M":
        return 2
    elif size[-1].upper() == "S":
        return 1


def sizeX(size):

    output = size
    for i in range(len(str(size))-1):
        output *= 10
    return output


def compare(sizeA, sizeB):

    if sizeA > sizeB:
        print(f"{size1} > {size2}")

    elif sizeA < sizeB:
        print(f"{size1} < {size2}")

    else:
        print(f"{size1} = {size2}")


size1 = input("Add first size: ")
size2 = input("Add second size: ")

sizeA, sizeB = sizeX(transfer(size1)), sizeX(transfer(size2))
compare(sizeA, sizeB)
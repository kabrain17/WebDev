#генераторы позволяют упростить работу по конструированию 

def infinite(lst, limit):
    counter = 0
    my_iter = iter(lst)
    try:
        yield next(my_iter)
    except StopIteration:
        my_iter


    while counter < limit:
        counter += 1
        yield next(my_iter)
        
my_gen = infinite([1, 2, 3], 5)
print(my_gen)





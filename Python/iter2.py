#@transaction.atomic декоратор
#основное место использования итераторов - это цикл for

class MyIter:
    limit = None
    counter = 0 

    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit 


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        
        else:
            raise StopIteration


my_iter = MyIter(5)
print(next(iter(my_iter)))





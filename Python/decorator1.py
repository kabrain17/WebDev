def decorator(func):
    def inner():
        print('Давай начнем)')
        func()
        print('Ну вот и все.')
    return inner 

def say():
    print('В процессе...')


say = decorator(say)
say()


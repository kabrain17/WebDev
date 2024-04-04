def decorator(func):

    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('end decorator')

    return inner

def say(name, surname):
    print('Hello,', name, surname + '!')

say = decorator(say)
say('Timur', 'Kali')



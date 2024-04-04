from datetime import datetime
from time import sleep
 
 
def time_now(msg, *, dt=None):
    dt = dt or datetime.now()
    print(msg, dt)

time_now('Сейчас такое время: ')
sleep(1)
time_now('Прошла секунда: ')
sleep(1)
time_now('Задам-ка другую дату: ', dt='2020-01-11 11:00:10')
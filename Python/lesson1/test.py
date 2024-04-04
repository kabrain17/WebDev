#Длина пароля должна быть больше 8 символов
#В пароле должны быть цифры
#В пароле должен быть восклицательный знак
#Пароль не должен быть “qwerty123!”

password = input()
num = int()

while len(password) < 8:
    print("Простой!")
    password = input()   
while "qwerty123" in password:
    print("Простой!")
    password = input()  
else:
    for i in password:
        if any([
        i == "!",
        i == num
            ]):
            print("Надежный")



    


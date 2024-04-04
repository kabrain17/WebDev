class User:
    login = None
    __password = None
    
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def send_message(self, message):
        print("Hello!")


class session_auth:
    def __init__(self, login, password):
        self.user = User(login, password)

    def __enter__(self):
        print(f"Пользователь {self.user.login} online")
        return self.user

    def __exit__(self, ex, tc, pp):
        print(f"Пользователь {self.user.login} offline")



with session_auth('timurkali', '<1223484>') as session:
    session.send_message("Kalaysyn?")



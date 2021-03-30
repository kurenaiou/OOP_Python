import hashlib
import AuthenticException

class User:
    def __init__(self, uname, password):
        self.username = self._encrypt_password(uname)
        self.password = self._encrypt_password(password)
        self.is_logged = 0

    def _encrypt_password(self, my_string):
        return hashlib.sha256(my_string.encode('utf-8')).hexdigest()

    def check_password(self, password):
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == self.password:
            return 1
        return 0

class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self, uname, password):
        user_to_add = User(uname, password)
        #User z hash name, passwd, is_logged -> self.users
        self.users[user_to_add.username] = [user_to_add.password,user_to_add.is_logged]
        #{'username-szyfr': ['haslo-szyfr', czy_zalogowany], ...}
        #{'9f...32f16':     ['03ac6...6f4',         0     ], ...}

    def login(self, uname, password):

        user_to_login = User(uname, password)

        if self.users.get(user_to_login.username):
            user_match = self.users.get(user_to_login.username)
            # print(user_match[0]) - zaszyfrowane hasło z osób które są w bazie
            # print(user_to_login.password) - zaszyfrowane hasło usera podanego jako arg
            if user_match[0] == user_to_login.password:
                print("To ta sama osoba")
                user_match[1] = 1
                #to płytka kopia, więc możemy tak działać
                #print(self.users.get(user_to_login.username))
            else:
                print("IncorrectPassword")
        else:
            print("IncorrectUsername")

    def is_logged_in(self, uname):
        user = User(uname, '')
        if self.users.get(user.username):
            user_match = self.users.get(user.username)
            print(user_match[1])


if __name__ == '__main__':
    pass
#TESTY dla klasy User i Authenticator
    # AuthSystem = Authenticator()
    # AuthSystem.add_user("Maria", "1234")
    # AuthSystem.add_user("Karol", "asd23")
    #
    # print(AuthSystem.users)
    # print("\n")
    # AuthSystem.login("Maria", "1234")
    # #AuthSystem.login("Karol", "asd23")
    # AuthSystem.is_logged_in("Maria")

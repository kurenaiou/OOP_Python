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
        # {'username-szyfr': ['haslo-szyfr', czy_zalogowany], ...}

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

class Authorizor:

    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        # { "permission": ["user1", "user2", ...], ... }
        if self.permissions.get(permission) == None:
            self.permissions[permission] = set()
        else:
            raise PermissionError

    def permit_user(self, uname, permission):
        user = User(uname, '')
        if self.authenticator.users.get(user.username):
            if self.permissions.get(permission) != None:
                self.permissions[permission].add(user.username)
            else:
                print("PermissionError")
        else:
            print("IncorrectUsername")

    def ckeck_permision(self, uname, permission):
        user = User(uname, '')
        if self.authenticator.users.get(user.username):
            if self.permissions.get(permission) != None:
                 S_users_with_permision = self.permissions[permission]
                    #zbiór ludzi z uprawnieniami
                 S_user_we_want_to_check = {user.username}
                    #jednoelementowy zbiór naszej osoby którą sprawdzamy
                 if S_user_we_want_to_check.issubset(S_users_with_permision):
                     return 1
                 else:
                     print("NotPermittedError")
            else:
                print("PermissionError")
        else:
            print("IncorrectUsername")
        return 0


if __name__ == '__main__':
#TESTY dla klasy User, Authenticator i Authorizer
    AuthSystem = Authenticator()
    AuthSystem.add_user("Maria", "1234")
    AuthSystem.add_user("Karol", "asd23")

    PermissionSystem = Authorizor(AuthSystem)
    PermissionSystem.add_permission("write")
    PermissionSystem.permit_user("Karol", "write")
    PermissionSystem.permit_user("Maria", "write")
    print(PermissionSystem.permissions)

    print(PermissionSystem.ckeck_permision("Maria", "write"))

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

import hashlib

class User:
    ''' Klasa z konstruktorem usera, wywouje sha256 za pomocą metody klasy
        _encrypt_password, check_password sprawdza czy hasło podane jako argument
        jest równy zapisanemu w obiekcie'''

    def __init__(self, uname, password):
        self.username = self._encrypt_password(uname)
        self.password = self._encrypt_password(password)
        self.is_logged = 0

    def _encrypt_password(self, my_string):
        return hashlib.sha256(my_string)

    def check_password(self, password):
        if hashlib.sha256(password) == self.password:
            return 1
        return 0
        #tutaj wyjątki

class AuthenticException(Exception):
    '''W tym projekcie to klasa bazowa dla innych wyhątków'''
    def __init__(self):
        self.username = None
        self.user = None
    pass
class PermissionError(Exception):
    pass
class IncorrectPassword(AuthenticException):
    pass
class IncorrectUsername(AuthenticException):
    pass
class NotLoggedError(AuthenticException):
    pass
class PasswordTooShort(AuthenticException):
    pass
class UsernameAlreadyExists(AuthenticException):
    pass
class NotPermittedError(AuthenticException):
    pass

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, uname, password):
        try:
            if self.users.get(uname) != None:
                if len(password) > 7:
                    self.users[uname]=password
                else:
                    raise PasswordTooShort
            else:
                raise UsernameAlreadyExists

        except UsernameAlreadyExists as error:
            pass
        except PasswordTooShort as error:
            pass

    def login(self, uname, password):
        try:
            if self.users.get(uname) != None:
                if self.users.get(uname) == password:
                    self.is_logged = 1
                    return 1
                else:
                    raise IncorrectPassword
            else:
                raise IncorrectUsername
        except IncorrectUsername as error:
            return 0
        except IncorrectPassword as error:
            return 0

    def is_logged_in(self):
        if bool(self.is_logged):
            return 1
        return 0

class Authorizor:

    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self,permission):
        if self.permissions.get(permission) != None:
            self.permissions[permission] = set()
        else:
            raise PermissionError

    def permit_user(self, uname, permission):
        if self.permissions:
            pass #dokończ, czy istnieje uprawnienie
                    #czy istnieje taki użytkownik w uprawnieniu

    def check_permision(self):
        pass

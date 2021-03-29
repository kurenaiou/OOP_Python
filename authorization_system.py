import hashlib

class User:
    ''' Klasa z konstruktorem usera, wywouje sha256 za pomocą metody klasy
        _encrypt_password, check_password sprawdza czy hasło podane jako argument
        jest równy zapisanemu w obiekcie'''

    def __init__(self, name, password):
        self.username = self._encrypt_password(name)
        self.password = self._encrypt_password(password)
        self.is_logged = 0

    def _encrypt_password(self, my_string):
        return hashlib.sha256(my_string)

    def ckeck_password(self, password):
        if hashlib.sha256(password) == self.password:
            return 1
        return 0
        #tutaj wyjątki


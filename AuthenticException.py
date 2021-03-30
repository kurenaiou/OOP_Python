
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
class Advisor:
    def __init__(self, name=None, lastname=None, email=None):
        self.__name = name
        self.__lastname = lastname
        self.__email = email

    def __str__(self):
        return f'Name: {self.name}, Lastname: {self.lastname}, Email: {self.email}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

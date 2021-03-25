class Student:
    def __init__(self, degree_plan, course, advisor, database):
        self.__name = None
        self.__lastname = None
        self.__major = None

        self.__dp = degree_plan
        self.__course = course
        self.__advisor = advisor
        self.__db = database

    def __str__(self):
        return f'Name: {self.name}, Lastname: {self.lastname}' \
               f'Major: {self.major}, Advisor: {self.__advisor.name}'

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
    def major(self):
        return self.__major

    @major.setter
    def major(self, major):
        self.__major = major

    @property
    def advisor(self):
        return self.__advisor

    @property
    def degree_plan(self):
        return self.__dp

    @property
    def course(self):
        return self.__course

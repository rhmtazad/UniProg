from repository import Entity


class Major:
    def __init__(self, database, course, prop):
        self.__major = Entity(database, course, prop)

    def add(self, *majors):
        self.__major.add(*majors)

    def remove(self, *major):
        self.__major.remove(*major)

    def rename(self, old_name, new_name):
        self.__major.rename(old_name, new_name)

    def form(self, major, **prop):
        self.__major.form(major, **prop)

    def copy(self, major, new_major, **prop):
        self.__major.copy(major, new_major, **prop)

    def get(self, major):
        return self.__major.get(major)

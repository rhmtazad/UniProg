from repository import Attribute


class Property:
    def __init__(self, database):
        self.__prop = Attribute(database)

    def add(self, major, **prop):
        self.__prop.add(major, **prop)

    def add_fk(self, major, prop, ref_major, ref_property):
        self.__prop.add_fk(major, prop, ref_major, ref_property)

    def rename(self, major, current_name, new_name):
        self.__prop.rename(major, current_name, new_name)

    def get(self, major, *prop):
        return self.__prop.get(major, *prop)

    def get_names(self, major):
        return self.__prop.get_names(major)

    def filter(self, major, **property_value):
        return self.__prop.filter(major, **property_value)

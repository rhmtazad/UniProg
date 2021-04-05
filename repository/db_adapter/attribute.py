from hydra.column import Column


class Attribute:
    def __init__(self, database):
        self.__attr = Column(database)

    def add(self, entity, **attributes):
        self.__attr.add(entity, **attributes)

    def add_fk(self, entity, attribute, ref_entity, ref_attribute):
        self.__attr.add_fk(entity, attribute, ref_entity, ref_attribute)

    def rename(self, entity, current_name, new_name):
        self.__attr.rename(entity, current_name, new_name)

    def get(self, entity, *attributes):
        return self.__attr.fetch(entity, *attributes)

    def get_names(self, entity):
        return self.__attr.fetch_names(entity)

    def filter(self, entity, **attr_value):
        return self.__attr.filter(entity, **attr_value)

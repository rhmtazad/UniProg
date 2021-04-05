from hydra.table import Table


class Entity:
    def __init__(self, database, record, attribute):
        self.__entity = Table(database, record, attribute)

    def add(self, *entities):
        self.__entity.add(*entities)

    def remove(self, *entities):
        self.__entity.drop(*entities)

    def rename(self, old_name, new_name):
        self.__entity.rename(old_name, new_name)

    def form(self, entity, **attributes):
        self.__entity.form(entity, **attributes)

    def copy(self, entity, new_entity, **attributes):
        self.__entity.copy(entity, new_entity, **attributes)

    def get(self, entity):
        return self.__entity.fetch(entity)

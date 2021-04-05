from hydra.database import Database


class EntityCollection:
    def __init__(self, database, entity):
        self.__collection = Database(database, entity)

    def remove_attribute(self, entity, **attributes):
        self.__collection.drop_col(entity, **attributes)

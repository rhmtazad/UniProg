from hydra.connection import Connection


class DB:
    def __init__(self, name=None, location=None):
        self.__db = Connection(name, location)

    def save(self, query):
        self.__db.execute(query)

    def get(self, query):
        return self.__db.fetch(query)

from hydra.row import Row


class Record:
    def __init__(self, database):
        self.__record = Row(database)

    def add(self, entity, **data):
        self.__record.insert(entity, **data)

    def remove(self, entity, record_id):
        self.__record.delete(entity, record_id)

    def update(self, entity, record_id, **data):
        self.__record.update(entity, record_id, **data)

    def attribute(self, entity, record_id, attribute):
        return self.__record.cell(entity, record_id, attribute)

    def get(self, entity, record_id):
        return self.__record.fetch(entity, record_id)

    def filter(self, entity, record_id, *attributes):
        return self.__record.filter(entity, record_id, *attributes)

    def count(self, entity, **attr_value):
        return self.__record.count(entity, **attr_value)

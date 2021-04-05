from abc import ABCMeta, abstractmethod


class AbstractRow(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, table, data):
        pass

    @abstractmethod
    def delete(self, table, row_id):
        pass

    @abstractmethod
    def update(self, table, row_id, data):
        pass

    @abstractmethod
    def fetch(self, table, row_id):
        pass

    @abstractmethod
    def filter(self, table, row_id, columns):
        pass

    @abstractmethod
    def cell(self, table, row_id, column):
        pass

    @abstractmethod
    def count(self, table, col_val):
        pass

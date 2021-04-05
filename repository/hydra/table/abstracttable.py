from abc import ABCMeta, abstractmethod


class AbstractTable(metaclass=ABCMeta):
    @abstractmethod
    def add(self, tables):
        pass

    @abstractmethod
    def drop(self, tables):
        pass

    @abstractmethod
    def rename(self, old_name, new_name):
        pass

    @abstractmethod
    def form(self, table, columns):
        pass

    @abstractmethod
    def copy(self, origin_tbl, new_tbl, columns):
        pass

    @abstractmethod
    def fetch(self, table):
        pass

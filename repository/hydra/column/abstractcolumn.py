from abc import ABCMeta, abstractmethod


class AbstractColumn(metaclass=ABCMeta):
    @abstractmethod
    def add(self, table, columns):
        pass

    @abstractmethod
    def add_fk(self, table, column, reference_tbl, reference_col):
        pass

    @abstractmethod
    def rename(self, table, current_name, new_name):
        pass

    @abstractmethod
    def fetch(self, table, columns):
        pass

    @abstractmethod
    def fetch_names(self, table):
        pass

    @abstractmethod
    def filter(self, table, col_val):
        pass

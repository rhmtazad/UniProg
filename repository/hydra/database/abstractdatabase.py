from abc import ABCMeta, abstractmethod


class AbstractDatabase(metaclass=ABCMeta):
    @abstractmethod
    def drop_col(self, tbl, columns):
        pass

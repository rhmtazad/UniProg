from abc import ABCMeta, abstractmethod


class AbstractConnection(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, query, fetch):
        pass

    @abstractmethod
    def fetch(self, query):
        pass

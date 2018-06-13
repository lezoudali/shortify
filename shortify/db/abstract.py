from abc import ABC, abstractmethod


class AbstractDBStorage(ABC):

    @abstractmethod
    def insert(self, key, value, overwrite=False):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def size(self):
        pass

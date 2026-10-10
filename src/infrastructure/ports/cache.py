from abc import ABC, abstractmethod

class CacheABC(ABC):
    @abstractmethod
    def set_cache(self, key:str, value: str):
        ...

    @abstractmethod
    def get_cache(self, key: str) -> str:
        ...
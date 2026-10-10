from src.infrastructure.ports.cache import CacheABC

class LocalCache(CacheABC):
    def __init__(self) -> None:
        super().__init__()
        self._cache: dict[str, str] = {}

    def set_cache(self, key:str, value: str):
        self._cache[key] = value

    def get_cache(self, key: str) -> str:
        return self._cache[key]

_instance = LocalCache()

def get_local_cache_instance() -> LocalCache:
    return _instance
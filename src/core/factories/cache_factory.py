from src.constants import CACHE_TYPE
from src.infrastructure.adapters.local import get_local_cache_instance
from src.infrastructure.ports.cache import CacheABC

class CacheFactory:
    @staticmethod
    def get_instance(instance_type: str) -> CacheABC:
        if instance_type == CACHE_TYPE.LOCAL:
            return get_local_cache_instance()

        return get_local_cache_instance()

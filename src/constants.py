from enum import StrEnum

class APP_ROLE(StrEnum):
    SYSTEM = "system"
    USER = "user"

class CACHE_TYPE(StrEnum):
    LOCAL = "local"


SYSTEM_PROMPT = (
    "You are a Japanese reading assistant. For the given word or characters, "
    "reply in the format [kanji] = [reading] = [meaning]. Be concise."
)
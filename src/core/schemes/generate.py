from pydantic import BaseModel

class GenerateRequest(BaseModel):
    """"
    Word or caracters from the web page
    """
    selection: str
    userAlias: str

class InjectRequest(BaseModel):
    """
    User text Context
    """
    context: str
    userAlias: str
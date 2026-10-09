from pydantic import BaseModel

class GenerateRequest(BaseModel):
    """"
    Word or caracters from the web page
    """
    selection: str
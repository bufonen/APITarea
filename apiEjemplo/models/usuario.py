from pydantic import BaseModel

class Usuario(BaseModel):
    Nombre: str
    Email: str

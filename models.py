
from pydantic import BaseModel

# Modelo de dados do usuário (entrada e saída)
class Usuario(BaseModel):
    id: int
    nome: str
    email: str


from pydantic import BaseModel

# Modelo de dados do usuário (entrada e saída)
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

##########################################################################

from sqlalchemy import Column, Integer, String
from database import Base

# Verão com SQLAlchemy
class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
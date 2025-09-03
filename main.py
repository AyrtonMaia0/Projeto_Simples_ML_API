# Teste Simples para ver o funcionamento
'''
from fastapi import FastAPI

# Inicializa Aplicacao FastAPI
app = FastAPI()

# Rota de teste
@app.get("/")
def read_root():
    return {"mensagem": "API Machine Learning funcionando!"}

# Outra rota exemplo
@app.get("/hello/{nome}")
def read_item(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo à API."}
'''
#############################################################################################
# https://youtu.be/nPUA8BLWzeY?si=O_c-PHdww0Z3B8yf

#Endpoints para:
    #Criar usuário
    #Listar todos os usuários
    #Consultar usuário por ID

# Primeiro Salvar Usuários na Memória 
# (um "banco de dados fake"). 
# Depois evoluímos para usar SQLite/MySQL/PostgreSQL.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializa Aplicação
app = FastAPI()

# Modelo de dados do usuário (entrada e saída)
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# "Banco de dados" em memória (lista de usuários)
usuarios_db = []

# ------------------ Rotas ------------------

# CREATE - Criar Novo Usuário
@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    # Verifica se o ID já existe
    for u in usuarios_db:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já cadastrado")
    usuarios_db.append(usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}

# READ - Listar Todos Usuários
@app.get("/usuarios/")
def listar_usuarios():
    return {"usuarios": usuarios_db}

# READ - Consultar Usuário por ID
@app.get("/usuarios/{usuario_id}")
def consultar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

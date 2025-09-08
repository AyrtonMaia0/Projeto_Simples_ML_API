
#Endpoints para:
    #Criar usuário
    #Listar todos os usuários
    #Consultar usuário por ID

# Primeiro Salvar Usuários na Memória 
# (um "banco de dados fake"). 
# Depois evoluímos para usar SQLite/MySQL/PostgreSQL.


#############################################################################################
# https://youtu.be/nPUA8BLWzeY?si=O_c-PHdww0Z3B8yf

# 1   | python -m pip install uvicorn fastapi
# 2   | python -m uvicorn main:app --reload
# 3.1 | /docs como Postman
# 3.2 | curl -X POST "http://127.0.0.1:8000/usuarios/" -H "Content-Type: application/json" -d "{\"id\":1,\"nome\":\"User\",\"email\":\"user@example.com\"}"

# 4   | pip install sqlalchemy psycopg2
# 

#############################################################################################


from fastapi import FastAPI, HTTPException
from models import Usuario  # importa a classe do outro arquivo

# Inicializa Aplicação
app = FastAPI()


# "Banco de dados" em memória (lista de usuários)
usuarios_db = []

# ------------------ Rotas ------------------

# CREATE - Criar Novo Usuário
@app.post("/user_create/")
def criar_usuario(usuario: Usuario):
    # Verifica se o ID já existe
    for u in usuarios_db:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já cadastrado")
    usuarios_db.append(usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}


# READ - Listar Todos Usuários
@app.get("/user_read/")
def listar_usuarios():
    return {"usuarios": usuarios_db}

# READ - Consultar Usuário por ID
@app.get("/user_id/{usuario_id}")
def consultar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# UPDATE - Atualizar Usuário por ID | PUT
@app.put("/user_update/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db[index] = usuario_atualizado
            return {"mensagem": "Usuário atualizado com sucesso!", "usuario": usuario_atualizado}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# DELETE - Remover Usuário por ID
@app.delete("/user_delete/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db.pop(index)
            return {"mensagem": f"Usuário com ID {usuario_id} deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
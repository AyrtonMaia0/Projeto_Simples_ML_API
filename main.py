
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


from fastapi import FastAPI, Depends, HTTPException
from models import Base, Usuario, UsuarioDB # importa a classe do outro arquivo
from database import SessionLocal, engine
from sqlalchemy.orm import Session

# Cria tabelas no banco se não existirem
Base.metadata.create_all(bind=engine)

# Inicializa Aplicação
app = FastAPI()

# "Banco de dados" em memória (lista de usuários)
#usuarios_db = []

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------ Rotas ------------------

# CREATE
@app.post("/user_create/")
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    db_usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario.id).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="ID já cadastrado")
    novo_usuario = UsuarioDB(**usuario.dict())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}



# READ ALL
@app.get("/user_read/")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioDB).all()
    return {"usuarios": usuarios}

# READ ID
@app.get("/user_id/{usuario_id}")
def consultar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# UPDATE
@app.put("/user_update/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
    if usuario:
        usuario.nome = usuario_atualizado.nome
        usuario.email = usuario_atualizado.email
        db.commit()
        return {"mensagem": "Usuário atualizado com sucesso!", "usuario": usuario_atualizado}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# DELETE
@app.delete("/user_delete/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return {"mensagem": f"Usuário com ID {usuario_id} deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
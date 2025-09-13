#  Descrição do Projeto

Este repositório contém uma **API simples construída com FastAPI**, como parte de uma atividade proposta em sala de aula. A intenção foi aplicar os primeiros conceitos de criação de endpoints RESTful e integração com banco de dados utilizando SQLAlchemy.

⚠️ **IMPORTANTE:** A atividade não foi finalizada por completo, pois a continuação da aula que traria o desfecho do desenvolvimento **não ocorreu**. Assim, a API encontra-se funcional, porém básica, seguindo exatamente o que foi proposto até o ponto em que a aula foi interrompida.

---

##  O que a API faz?

A aplicação permite realizar operações básicas (CRUD) sobre uma entidade de **usuário**, contendo os seguintes endpoints:

- **[POST] `/user_create/`** – Criação de um novo usuário.
- **[GET] `/user_read/`** – Listagem de todos os usuários.
- **[GET] `/user_id/{id}`** – Consulta de usuário por ID.
- **[PUT] `/user_update/{id}`** – Atualização de dados de um usuário.
- **[DELETE] `/user_delete/{id}`** – Exclusão de usuário por ID.

Inicialmente, os dados foram pensados para serem armazenados apenas na memória. Com o avanço da aula (até onde foi possível), foi implementada a integração com banco de dados utilizando **SQLAlchemy** e variáveis de ambiente para a conexão PostgreSQL via **Railway**.

---

##  Estrutura do Projeto

O projeto está dividido em alguns arquivos principais:

- `main.py`: onde estão definidos os endpoints da API.
- `models.py`: definição dos modelos de dados com Pydantic e SQLAlchemy.
- `database.py`: configuração da conexão com o banco de dados e sessão do SQLAlchemy.
- `.gitignore` e `.gitattributes`: arquivos de configuração padrão do repositório.

---

##  Tecnologias Utilizadas

- **FastAPI**
- **Uvicorn** (para execução do servidor)
- **SQLAlchemy**
- **PostgreSQL** (Railway como host de banco)
- **Python-dotenv**

---

##  Considerações Finais

Este projeto teve como foco a **introdução ao desenvolvimento de APIs com FastAPI**. O código está funcional e pronto para testes via `/docs` (Swagger UI) ou via ferramentas como `curl` e Postman.

Por fim, reforça-se que, por falta de continuidade da aula, **não houve aprofundamento** ou refinamento da aplicação além do básico apresentado aqui.


---

##  Como Executar Localmente

###  Pré-requisitos

- Python 3.8 ou superior
- Git
- PostgreSQL (caso queira usar localmente)
- Conta no [Railway](https://railway.app/) (caso queira usar banco em nuvem)

### 🔧 Instalação

#### Clone o repositório:

```bash
git clone https://github.com/AyrtonMaia0/Projeto_Simples_ML_API.git
cd Projeto_Simples_ML_API
```

#### Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
#### Instale as dependências:
```bash
pip install -r requirements.txt
```

❗ Caso o arquivo requirements.txt não exista, você pode instalar manualmente:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv
```

#### Crie um arquivo .env com a variável de ambiente:
```bash
DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco
```

### Executando o servidor

#### Com tudo instalado, execute:
```bash
uvicorn main:app --reload
```

#### Acesse no navegador:
```bash
http://127.0.0.1:8000/docs
```

---

# Créditos

Projeto desenvolvido por **Ayrton Maia**, **Ayanne Caroline** e **Petrônio Silva** como parte de atividade didática.
Repositório: Projeto_Simples_ML_API

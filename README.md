# API de Gerenciamento de Tarefas

API RESTful para gerenciamento de tarefas desenvolvida com FastAPI e SQLAlchemy.

## Tecnologias Utilizadas

- Python 3.8+
- FastAPI (framework web)
- SQLAlchemy (ORM)
- SQLite (banco de dados)
- Pydantic (validação de dados)
- Uvicorn (servidor ASGI)

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://seu-repositorio/task-api.git
   cd task-api
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando a API

1. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Acesse a documentação interativa da API:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Endpoints Disponíveis

### Tarefas

- `GET /tasks/`: Lista todas as tarefas (com paginação)
- `POST /tasks/`: Cria uma nova tarefa
- `GET /tasks/{task_id}`: Obtém uma tarefa específica
- `PUT /tasks/{task_id}`: Atualiza uma tarefa
- `DELETE /tasks/{task_id}`: Remove uma tarefa

## Exemplos de Uso

### Criar uma nova tarefa

```bash
curl -X POST "http://localhost:8000/tasks/" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Estudar FastAPI",
           "description": "Aprender sobre FastAPI e suas funcionalidades"
         }'
```

### Listar tarefas

```bash
# Listar todas as tarefas
curl "http://localhost:8000/tasks/"

# Listar tarefas com paginação
curl "http://localhost:8000/tasks/?skip=0&limit=10"

# Listar apenas tarefas concluídas
curl "http://localhost:8000/tasks/?completed=true"
```

### Atualizar uma tarefa

```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{
           "completed": true
         }'
```

### Remover uma tarefa

```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## Estrutura do Projeto

```
task-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── requirements.txt
├── README.md
└── .gitignore
```

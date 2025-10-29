Criar projeto FastAPI completo do zero com API de gerenciamento de tarefas.

ESTRUTURA DE ARQUIVOS:
- app/__init__.py (vazio, marca como pacote)
- app/main.py (aplicação FastAPI)
- app/database.py (configuração SQLite)
- app/models.py (modelos SQLAlchemy)
- app/schemas.py (schemas Pydantic)
- .gitignore (incluir: venv/, __pycache__/, *.db, .env, .vscode/)
- requirements.txt
- README.md (com instruções completas de setup e uso)
- AGENTS.md (padrões de código do projeto)
- .coderabbit.yaml (configuração CodeRabbit em português)

DEPENDÊNCIAS A INSTALAR:
- fastapi
- uvicorn[standard]
- sqlalchemy
- pydantic

IMPLEMENTAÇÃO DETALHADA:

1. app/database.py:
   - SQLAlchemy engine com SQLite (arquivo tasks.db)
   - URL: sqlite:///./tasks.db
   - SessionLocal com sessionmaker(autocommit=False, autoflush=False)
   - Base = declarative_base()
   - Função get_db() para dependency injection com yield

2. app/models.py:
   - Importar Base de app.database
   - Classe Task(Base) com __tablename__ = "tasks"
   - Campos: id (Integer, primary_key, index), title (String, nullable=False, index), 
     description (String), completed (Boolean, default=False), 
     created_at (DateTime, default=datetime.utcnow)

3. app/schemas.py:
   - TaskCreate: title (Field min_length=3, max_length=100), 
     description (Optional, max_length=500)
   - TaskUpdate: todos campos Optional
   - TaskResponse: todos campos + from_attributes=True (Pydantic v2)

4. app/main.py:
   - FastAPI(title="Task Management API", description="...", version="1.0.0")
   - models.Base.metadata.create_all(bind=engine) no startup
   - Endpoints CRUD completos com tags=["Tasks"]:
     * POST /tasks/ (response_model=TaskResponse, status_code=201)
     * GET /tasks/ (List[TaskResponse], params: skip=0, limit=10, completed: Optional[bool])
     * GET /tasks/{task_id} (TaskResponse)
     * PUT /tasks/{task_id} (TaskResponse)
     * DELETE /tasks/{task_id} (status_code=204)
   - Tratamento HTTPException 404 para task não encontrada
   - Docstrings em todas as funções
   - Endpoint raiz GET / retorna mensagem de boas-vindas

5. README.md incluir:
   - Descrição do projeto
   - Tecnologias usadas
   - Instruções de setup (clonar, venv, instalar, rodar)
   - Como testar a API (via /docs)
   - Exemplos de requisições

6. AGENTS.md incluir:
   - Padrões Python (PEP 8, type hints, docstrings)
   - Estrutura do projeto
   - Convenções FastAPI
   - Padrões de validação

7. .coderabbit.yaml:
   - language: "pt"
   - reviews.high_level_summary: true
   - path_filters para ignorar venv/, __pycache__/, *.db
   - path_instructions específicas para app/models.py, app/schemas.py, app/main.py

APÓS CRIAR TODOS OS ARQUIVOS:
1. Executar: pip install -r requirements.txt
2. Confirmar que todas dependências foram instaladas
3. Informar que o projeto está pronto para rodar com: uvicorn app.main:app --reload
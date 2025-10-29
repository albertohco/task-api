# PR: feat_api → main

## Título sugerido
feat(api): adicionar API completa de gerenciamento de tarefas (FastAPI + SQLAlchemy)

## Resumo
Este PR implementa uma API REST completa para gerenciamento de tarefas usando FastAPI, SQLAlchemy e SQLite.
Fornece endpoints CRUD, validação com Pydantic (v2), configuração do banco e documentação interativa.

Objetivo: entregar um serviço mínimo funcional para criação, listagem, atualização e remoção de tarefas, pronto para uso em desenvolvimento e testes.

---

## Principais mudanças
Adicionados / Alterados:

- `app/__init__.py` — marca o diretório como pacote
- `app/main.py` — aplicação FastAPI e rotas CRUD (endpoints e docstrings)
- `app/database.py` — configuração do SQLite e dependency `get_db`
- `app/models.py` — modelo SQLAlchemy `Task`
- `app/schemas.py` — schemas Pydantic (`TaskCreate`, `TaskUpdate`, `TaskResponse`)
- `.coderabbit.yaml` — configuração para revisões automatizadas (em português)
- `AGENTS.md` — padrões e convenções do projeto (PEP8, type hints, docstrings)
- `requirements.txt` — dependências do projeto
- `README.md` — instruções de setup, execução e exemplos de uso
- `.gitignore` — adicionado/atualizado para ignorar `venv/`, `__pycache__/`, `*.db`, `.env`, `.vscode/`

---

## Como testar localmente
1. Troque para a branch `feat_api` (se necessário):
```bash
git checkout feat_api
```
2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Inicie a API em modo de desenvolvimento:
```bash
uvicorn app.main:app --reload
```
5. Acesse a documentação interativa:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Requisições de verificação rápidas (curl)
- Criar tarefa:
```bash
curl -X POST "http://localhost:8000/tasks/" -H "Content-Type: application/json" -d '{"title":"Testar API","description":"Descrição de teste"}'
```
- Listar tarefas:
```bash
curl "http://localhost:8000/tasks/"
```
- Atualizar tarefa:
```bash
curl -X PUT "http://localhost:8000/tasks/1" -H "Content-Type: application/json" -d '{"completed": true}'
```
- Remover tarefa:
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

---

## Notas de implementação / decisões importantes
- Banco: SQLite em arquivo (`sqlite:///./tasks.db`) — indicado para desenvolvimento; recomenda-se migrar para um SGBD mais robusto em produção.
- Pydantic v2: uso de `model_dump()` para serialização na criação/atualização e `from_attributes = True` em `TaskResponse` para compatibilidade com objetos ORM.
- Criação automática de tabelas: `models.Base.metadata.create_all(bind=engine)` é chamado no módulo principal para criar o banco no startup.
- O arquivo `.coderabbit.yaml` contém instruções em português para revisões automatizadas. Verifique se a integração com CodeRabbit espera exatamente essa semântica de `path_filters`.

---

## Checklist (revisão)
- [ ] Código segue padrões descritos em `AGENTS.md` (PEP8, type hints, docstrings).
- [ ] Endpoints implementados com docstrings e códigos de status apropriados.
- [ ] Validações Pydantic adequadas (min/max lengths, campos obrigatórios/opcionais).
- [ ] Tratamento de erro 404 para tarefas não encontradas.
- [ ] Dependências listadas em `requirements.txt`.
- [ ] `.gitignore` cobre artefatos locais.
- [ ] Testes manuais básicos (criar, listar, atualizar, deletar) validados localmente.
- [ ] Revisão do `.coderabbit.yaml` por quem gerencia a ferramenta (se aplicável).

---

## Sugestão de reviewers
- Backend lead / responsável por infra (migração DB e segurança)
- Autor(es) do projeto (padrões de código)
- QA / tester (fluxos e endpoints)

---

## Observações finais / próximos passos sugeridos
- Adicionar testes automatizados (pytest + test client do FastAPI) cobrindo os endpoints principais.
- Adicionar migração para um SGBD adequado em ambiente de staging/produção (ex.: PostgreSQL) e usar Alembic para migrações.
- Se desejar, eu posso gerar testes básicos e/ou abrir o PR no GitHub (preciso de permissões/credentials).


> PR gerado automaticamente pelo assistente — altere o conteúdo conforme necessário antes de abrir o PR.

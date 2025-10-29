# Padrões e Convenções do Projeto

Este documento descreve os padrões e convenções que devem ser seguidos no desenvolvimento deste projeto.

## Padrões Python (PEP 8)

1. **Indentação**
   - Use 4 espaços para indentação (não use tabs)
   - Limite linhas a 79 caracteres para código e 72 para comentários/documentação

2. **Imports**
   - Um import por linha
   - Organize imports em grupos: stdlib, third-party, local
   - Use imports absolutos em vez de relativos

3. **Convenções de Nomenclatura**
   - Classes: CamelCase
   - Funções e variáveis: snake_case
   - Constantes: UPPER_CASE
   - Nomes descritivos e significativos

## Type Hints

1. **Uso Obrigatório**
   - Todas as funções devem ter type hints
   - Use tipos do módulo `typing` quando necessário

2. **Exemplos**
   ```python
   from typing import List, Optional

   def get_task(task_id: int) -> dict:
       pass

   def list_tasks(limit: Optional[int] = None) -> List[dict]:
       pass
   ```

## Docstrings

1. **Formato**
   - Use docstrings estilo Google
   - Inclua descrição, args, returns e raises quando aplicável

2. **Exemplo**
   ```python
   def create_task(task: TaskCreate) -> Task:
       """
       Cria uma nova tarefa.

       Args:
           task: Dados da tarefa a ser criada

       Returns:
           Task: A tarefa criada

       Raises:
           HTTPException: Se houver erro de validação
       """
       pass
   ```

## Estrutura do Projeto

1. **Organização de Arquivos**
   ```
   app/
   ├── __init__.py      # Marca o diretório como pacote Python
   ├── main.py          # Aplicação FastAPI e rotas
   ├── database.py      # Configuração do banco de dados
   ├── models.py        # Modelos SQLAlchemy
   └── schemas.py       # Schemas Pydantic
   ```

2. **Responsabilidades**
   - `main.py`: Rotas e lógica da API
   - `database.py`: Configuração do banco de dados
   - `models.py`: Modelos de dados
   - `schemas.py`: Validação e serialização

## Convenções FastAPI

1. **Rotas**
   - Use tags para agrupar endpoints
   - Inclua descrições claras nas rotas
   - Use status codes apropriados

2. **Validação**
   - Use Pydantic para validação de entrada/saída
   - Defina limites e restrições claros
   - Trate erros adequadamente

3. **Dependências**
   - Use `Depends` para injeção de dependências
   - Crie funções de dependência reutilizáveis

## Padrões de Validação

1. **Campos Obrigatórios**
   ```python
   class TaskCreate(BaseModel):
       title: str = Field(..., min_length=3, max_length=100)
   ```

2. **Campos Opcionais**
   ```python
   class TaskUpdate(BaseModel):
       title: Optional[str] = Field(None, min_length=3, max_length=100)
   ```

3. **Validações Customizadas**
   - Use validators do Pydantic quando necessário
   - Implemente validações de negócio nas rotas

## Tratamento de Erros

1. **HTTP Exceptions**
   - Use códigos HTTP apropriados
   - Forneça mensagens de erro claras
   - Mantenha consistência nas respostas de erro

2. **Validação de Dados**
   - Valide dados de entrada usando Pydantic
   - Trate erros de validação adequadamente
   - Retorne mensagens de erro descritivas

## Boas Práticas

1. **Segurança**
   - Sanitize dados de entrada
   - Evite exposição de informações sensíveis
   - Use HTTPS em produção

2. **Performance**
   - Use paginação em listagens
   - Otimize consultas ao banco de dados
   - Cache quando apropriado

3. **Manutenibilidade**
   - Mantenha o código DRY (Don't Repeat Yourself)
   - Documente alterações significativas
   - Siga os padrões estabelecidos
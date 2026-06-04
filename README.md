# Knowledge Hub - FastAPI Backend

## Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

## Save Dependencies
```bash
pip freeze > requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

**Visit:** http://localhost:8000

**Swagger:** http://localhost:8000/docs

**ReDoc:** http://localhost:8000/redoc

## Generate Migration
```bash
alembic revision --autogenerate -m "create users table"
alembic revision --autogenerate -m "create collections table"
```

## Run Migration
```bash
alembic upgrade head
```
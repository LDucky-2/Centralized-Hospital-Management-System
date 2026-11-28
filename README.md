# Centralized Hospital Management System

A role-based academic hospital-management prototype built as a FastAPI backend and React/Vite frontend.

## Structure

```text
backend/
  app/
    auth/
    users/
    patients/
    staff/
    rbac/
    activity/
  alembic/
  main.py
frontend/
  src/
    components/
    context/
    layouts/
    pages/
    services/
    types/
docs/
```

The frontend and backend follow the same feature/service/repository separation pattern as the example project.

## Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
fastapi dev main.py
```

API documentation: `http://localhost:8000/api/docs`

Development IT account:

- ID: `9999`
- Password: `9999`

## Frontend

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## Database

Local development uses SQLite at `backend/chms.db`. Supabase PostgreSQL is selected through `DATABASE_URL` or `POSTGRES_URL` in production.

Run migrations with Alembic from the `backend/` directory.

## Demo data

After applying migrations:

```powershell
cd backend
python scripts/seed_demo.py
```

Demo staff IDs use `1001` through `1007`, password `1234`. The IT account remains `9999` / `9999`. The demo patient is `80000001` / `1234`.

## Stack

- React, TypeScript, Vite
- FastAPI, SQLModel, Alembic
- SQLite locally and PostgreSQL/Supabase in production
- PyJWT and Argon2

## Backend

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH="backend"
uvicorn app.main:app --reload
```

API documentation: `http://localhost:8000/api/docs`

The development seed IT account is `9999` with password `9999`.

## Frontend

```powershell
cd frontend
npm install
npm run dev
```

Create a `frontend/.env` file with `VITE_API_URL=http://localhost:8000` if the API does not use the default.


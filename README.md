# OMS (Order Management System)

A FastAPI-based order management system with user authentication, PostgreSQL, and Alembic migrations.

## Features

- **FastAPI** – REST API with automatic OpenAPI docs
- **PostgreSQL** – Database with SQLAlchemy ORM
- **Alembic** – Database migrations
- **Auth** – User registration with password hashing (bcrypt)
- **Docker** – Run app and database with Docker Compose

## Prerequisites

- Python 3.11+
- PostgreSQL (or use Docker for the database)
- Optional: Docker & Docker Compose for containerized setup

## Setup

### 1. Clone and install dependencies

```bash
git clone <repo-url>
cd OMS
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment variables

Create a `.env` file in the project root (see [Environment variables](#environment-variables)). Do not commit `.env`.

### 3. Database and migrations

With a running PostgreSQL instance:

```bash
# Run migrations
alembic upgrade head

# Optional: seed data
python -m app.seed
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

API: **http://localhost:8003** (or the port set in `PORT`).  
Docs: **http://localhost:8003/docs**

---

## Docker

Run the app and PostgreSQL together:

```bash
docker-compose up --build
```

App: **http://localhost:8000**  
Run migrations inside the app container:

```bash
docker-compose exec app alembic upgrade head
```

---

## Environment variables

| Variable        | Description                    | Example                    |
|----------------|--------------------------------|----------------------------|
| `PORT`         | Server port                    | `8003`                     |
| `DATABASE_URL` | PostgreSQL connection string   | `postgresql://user:pass@localhost:5432/oms` |
| `JWT_SECRET`   | Secret for JWT signing         | (use a long random string) |

---

## API overview

| Method | Path           | Description        |
|--------|----------------|--------------------|
| GET    | `/health`      | Health check       |
| POST   | `/users/register` | Register a user |

Interactive API documentation: **/docs** (Swagger UI).

---

## Project structure

```
OMS/
├── app/
│   ├── config/       # Settings (e.g. from .env)
│   ├── crud/         # Database operations
│   ├── db/           # Database connection and session
│   ├── models/       # SQLAlchemy models
│   ├── routes/       # API routes (health, auth)
│   ├── schemas/      # Pydantic request/response models
│   ├── services/     # Business logic (e.g. auth)
│   ├── main.py       # FastAPI app entry
│   └── seed.py       # Optional seed script
├── alembic/          # Migrations
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env              # Local env (not committed)
```

---

## License

MIT (or your chosen license)

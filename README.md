# 🔐 Auth API System (JWT + FastAPI)

A secure authentication & authorization REST API built with **FastAPI**, **SQLModel**, **bcrypt**, and **JWT** tokens.

## Features
- Register & login endpoints
- Secure password hashing
- JWT token issuance & verification
- Role-based access control
- SQLite database by default
- Unit tests with pytest
- Interactive docs at `/docs`

## Quickstart
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` to explore.

## Env Config
Edit `app/core/config.py` or set env vars:
- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `DATABASE_URL`
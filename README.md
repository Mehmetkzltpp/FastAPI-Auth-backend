# Secure FastAPI Authentication Backend

A production-ready User Authentication system built with FastAPI and SQLAlchemy.

## Features
- **Separation of Concerns:** Clean 5-file architecture (`main`, `models`, `schemas`, `database`, `utils`).
- **Security:** Password hashing using `bcrypt` (Passlib).
- **Session Management:** Stateless authentication using signed JSON Web Tokens (JWT).
- **Database:** SQLite integration with SQLAlchemy ORM.

## How to Run
1. Install dependencies: `pip install fastapi uvicorn sqlalchemy passlib bcrypt==3.2.2 PyJWT`
2. Start server: `uvicorn main:app --reload`
3. View API docs: `http://127.0.0.1:8000/docs`
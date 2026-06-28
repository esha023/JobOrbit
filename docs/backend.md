# JobOrbit Backend Documentation

This document explains the technical details of the backend module layout, including routing structures, authentication wrappers, database helper sessions, and environmental configurations.

## 1. Technologies Stack
*   **FastAPI**: High-performance python web framework.
*   **Uvicorn**: ASGI web server implementation.
*   **SQLAlchemy 2.0**: Object Relational Mapper for PostgreSQL.
*   **Pydantic v2**: Type validations and configurations management.

---

## 2. Server Framework Layout

### Request Flow
```
Client HTTP Request
       ↓
 CORS Middleware
       ↓
 Firebase Token Validator (Security Dependency)
       ↓
 FastAPI Controller (Route Handlers)
       ↓
 Database Session Injector (SQLAlchemy Engine Dependency)
       ↓
 DB Query execution / Third-party services integration
       ↓
 Client Response
```

---

## 3. Core Modules Detail

### 1. `main.py`
The API entry point. Mounts CORS rules allowing frontend origins, links the major route groups, and manages API lifecycle events.

### 2. `core/config.py`
Uses Pydantic's `BaseSettings` to parse environment variables from `.env` files. Ensures validation of connection endpoints (e.g. database URL string correctness, API keys) during bootstrap.

### 3. `core/database.py`
Configures the SQLAlchemy pool engine:
*   Includes `pool_pre_ping=True` to handle transient database drops.
*   Declares `SessionLocal` class generators.
*   Exposes `get_db()` helper used as a route dependency injection hook.

### 4. `core/security.py`
Exposes the token checker dependency (`get_current_user`). It parses the `Authorization` header bearer token and validates it with the Firebase Admin service helper.

---

## 4. Sub-router Integrations
*   `/api/v1/auth`: Syncs Firebase credentials and handles onboarding.
*   `/api/v1/jobs`: Tracks application entries.
*   `/api/v1/ai`: Communicates with LLM models for parsing or content generators.
*   `/api/v1/sync`: Interacts with Google services.

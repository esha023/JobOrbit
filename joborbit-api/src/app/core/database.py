from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.app.core.config import settings

# Create engine
engine = create_engine(
    settings.DATABASE_URL,
    # pool_pre_ping is important to automatically reconnect if PostgreSQL restarts
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get db session in API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

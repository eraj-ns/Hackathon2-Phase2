from sqlmodel import create_engine, Session
import os


# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create engine with connection pooling for Neon Serverless PostgreSQL
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Enable SQL logging for development
    pool_size=5,  # Connection pool size
    max_overflow=10,  # Additional connections if pool is exhausted
    pool_pre_ping=True,  # Verify connections are alive before using
)


def create_db_and_tables():
    """Create database tables."""
    from sqlmodel import SQLModel
    # Import models here to ensure they're registered
    from .models.task import Task
    from .models.user import User
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get database session."""
    with Session(engine) as session:
        yield session

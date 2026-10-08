"""Database tables. Add your models here (Task 2: Dataset; Task 3: Resource, Alert).

Tables are created when the app starts (see main.py). If you change a model after its table exists,
delete backend/cis_exercise.db to recreate it: there are no migrations in this exercise.

Example of the style used (SQLAlchemy 2.0):

    class Example(Base):
        __tablename__ = "examples"

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(200))
        created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(db_url, echo=True, future=True)
        self._session_factory = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def get_session(self) -> AsyncSession:
        return self._session_factory()

    async def create_database(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

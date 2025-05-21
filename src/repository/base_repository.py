from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Callable


class BaseRepository:
    def __init__(self, session_factory: Callable[[], AsyncSession]):
        self.session: AsyncSession = session_factory()

# If there is any changes that needed to be done here, please discuss with JJ
# Otherwise, the changes you made may be refactored/excluded
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import app_configuration

database_engine = create_async_engine(
    app_configuration.DATABASE_URL,
    connect_args={"ssl": True},
    echo=app_configuration.SQL_ECHO,
)

__async_session = async_sessionmaker(
    database_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_database_session() -> AsyncGenerator[AsyncSession, None]:
    async with __async_session() as session:
        yield session

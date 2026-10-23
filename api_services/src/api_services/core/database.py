# If there is any changes that needed to be done here, please discuss with JJ
# Otherwise, the changes you made may be refactored/excluded

from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session

from api_services.core.settings import settings

database_engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"sslmode": "require", "channel_binding": "require"},
    echo=settings.SQL_ECHO,
)


def __get_session():
    with Session(database_engine) as session:
        yield session


DatabaseSession = Annotated[Session, Depends(__get_session)]

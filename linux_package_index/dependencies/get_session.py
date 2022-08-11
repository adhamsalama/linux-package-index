from sqlmodel import Session
from linux_package_index.db import engine
from typing import Generator


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

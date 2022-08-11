from sqlmodel import Field, SQLModel


class Package(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    website: str | None
    deb: str | None
    rpm: str | None

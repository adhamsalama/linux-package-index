from decouple import config  # type: ignore
from sqlmodel import create_engine
import linux_package_index.models.package

sqlite_url: str = str(config("sqlite_url"))

engine = create_engine(sqlite_url, echo=True)

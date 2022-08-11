from fastapi import APIRouter, Depends
from linux_package_index.models.package import Package
from sqlmodel import Session, select
from linux_package_index.db import engine
from linux_package_index.dependencies.get_session import get_session
from sqlmodel import delete

router = APIRouter()


@router.get("")
def get_all_packages(session: Session = Depends(get_session)):
    packages = session.exec(select(Package)).all()
    print(packages)
    return packages


@router.post("")
def add_package(package: Package, session: Session = Depends(get_session)):
    session.add(package)
    session.commit()
    session.refresh(package)
    return package


@router.put("/{id}")
def update_package(id: int, package: Package, session: Session = Depends(get_session)):
    result = session.exec(select(Package).where(Package.id == id)).one()
    print(result)
    result.name = package.name
    result.website = package.website
    result.deb = package.deb
    result.rpm = package.rpm
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


@router.delete("/{id}")
def delete_package(id: int, session: Session = Depends(get_session)):
    result = session.exec(select(Package).where(Package.id == id)).one()
    session.delete(result)
    session.commit()
    return result

from typing import Annotated
from fastapi import Depends

from app.database import SessionDep
from app.wards.repository import WardRepository
from app.wards.service import WardService


def get_ward_service(session: SessionDep) -> WardService:
    return WardService(WardRepository(session))


WardServiceDep = Annotated[WardService, Depends(get_ward_service)]

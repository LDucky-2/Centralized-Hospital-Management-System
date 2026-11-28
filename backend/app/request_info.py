from typing import Annotated

from fastapi import Depends, Request


class ClientInfo:
    def __init__(self, user_agent: str | None, ip_address: str | None) -> None:
        self.user_agent = user_agent
        self.ip_address = ip_address


def get_client(request: Request) -> ClientInfo:
    return ClientInfo(
        user_agent=request.headers.get("user-agent"),
        ip_address=request.client.host if request.client else None,
    )


ClientDep = Annotated[ClientInfo, Depends(get_client)]

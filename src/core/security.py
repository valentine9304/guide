from fastapi import Header, HTTPException, status
from os import getenv

from src.core.config import configs


async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != configs.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key"
        )

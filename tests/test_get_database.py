import pytest
from notion_client.errors import APIResponseError

from src.get_database import get_database


@pytest.mark.asyncio
async def test_invalid_get_database() -> None:
    with pytest.raises(APIResponseError):
        await get_database("invalid_database_id")


@pytest.mark.asyncio
async def test_valid_get_database() -> None:
    database = await get_database("1b7f60eb44fe80449e7dc5aa41e0caab")
    assert database is not None

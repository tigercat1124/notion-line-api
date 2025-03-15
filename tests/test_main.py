import pytest
from notion_client.errors import APIResponseError

from src.main import create_page


@pytest.mark.asyncio
async def test_create_page_invalid_database_id() -> None:
    with pytest.raises(APIResponseError):
        await create_page("invalid_database_id", "test_title")


@pytest.mark.asyncio
async def test_create_page_valid_database_id() -> None:
    # database_id = "1b7f60eb-44fe-8044-9e7d-c5aa41e0caab"
    # pattern = re.compile(
    #     "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    # )
    # assert pattern.match(database_id)
    pass

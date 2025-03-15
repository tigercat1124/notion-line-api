import pytest

from src.main import create_page


@pytest.mark.asyncio
async def test_create_page_invalid_database_id():
    with pytest.raises(Exception):
        await create_page("invalid_database_id", "test_title")


@pytest.mark.asyncio
async def test_create_page_valid_database_id():
    # TODO: 環境変数を設定する必要がある
    # os.environ["NOTION_TOKEN"] = "YOUR_NOTION_TOKEN"
    # DATABASE_ID = "YOUR_DATABASE_ID"
    # await create_page(DATABASE_ID, "test_title")
    pass

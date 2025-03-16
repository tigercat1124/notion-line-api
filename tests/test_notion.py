import datetime
import unittest.mock

import pytest

from src.notion import AsyncNotion


@pytest.mark.asyncio
async def test_create_page() -> None:
    mock_client = unittest.mock.AsyncMock()
    mock_client.pages.create.return_value = {"id": "test_page_id"}
    mock_notion = AsyncNotion(client=mock_client)
    page = await mock_notion.create_page()
    assert page is not None
    assert page["id"] == "test_page_id"


@pytest.mark.asyncio
async def test_search_page_by_date() -> None:
    mock_client = unittest.mock.AsyncMock()
    mock_client.databases.query.return_value = {"results": [{"id": "test_page_id"}]}
    mock_notion = AsyncNotion(client=mock_client)
    today = datetime.date.today()
    pages = await mock_notion.search_page_by_date(today)
    assert isinstance(pages, list)
    assert pages[0]["id"] == "test_page_id"


@pytest.mark.asyncio
async def test_append_block_to_page() -> None:
    mock_client = unittest.mock.AsyncMock()
    mock_client.pages.create.return_value = {"id": "test_page_id"}
    mock_client.blocks.children.append.return_value = None
    mock_notion = AsyncNotion(client=mock_client)
    page = await mock_notion.create_page()
    assert page is not None
    page_id = page["id"]
    result = await mock_notion.append_block_to_page(page_id, "This is some content!")
    assert result is None

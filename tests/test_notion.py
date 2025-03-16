import datetime

import pytest

from src.notion import AsyncNotion


@pytest.mark.asyncio
async def test_create_page() -> None:
    notion = AsyncNotion()
    page = await notion.create_page()
    assert page is not None


@pytest.mark.asyncio
async def test_search_page_by_date() -> None:
    notion = AsyncNotion()
    today = datetime.date.today()
    pages = await notion.search_page_by_date(today)
    assert isinstance(pages, list)


@pytest.mark.asyncio
async def test_append_block_to_page() -> None:
    notion = AsyncNotion()
    page = await notion.create_page()
    assert page is not None
    page_id = page["id"]
    result = await notion.append_block_to_page(page_id, "This is some content!")
    assert result is True

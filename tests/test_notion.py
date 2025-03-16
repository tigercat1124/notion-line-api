import pytest

from src.notion import AsyncNotion


@pytest.mark.asyncio
async def test_create_page() -> None:
    notion = AsyncNotion()
    page = await notion.create_page()
    assert page is not None

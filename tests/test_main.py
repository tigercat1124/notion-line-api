from unittest.mock import AsyncMock

import pytest
from httpx import Response
from notion_client.errors import APIErrorCode, APIResponseError

from src.notion import AsyncNotion


@pytest.mark.asyncio
async def test_notion_create_page_success() -> None:
    mock_client = AsyncMock()
    mock_client.pages.create.return_value = {"id": "test_id"}
    notion = AsyncNotion(client=mock_client)
    result = await notion.create_page()
    assert result == {"id": "test_id"}


@pytest.mark.asyncio
async def test_notion_create_page_failure() -> None:
    mock_client = AsyncMock()
    mock_client.pages.create.side_effect = APIResponseError(
        response=Response(500),
        code=APIErrorCode.InternalServerError,
        message="Internal Server Error",
    )
    notion = AsyncNotion(client=mock_client)
    with pytest.raises(APIResponseError):
        await notion.create_page()


@pytest.mark.asyncio
async def test_notion_create_page_retry() -> None:
    mock_client = AsyncMock()
    mock_client.pages.create.side_effect = APIResponseError(
        response=Response(429),
        code=APIErrorCode.RateLimited,
        message="Rate limited",
    )
    notion = AsyncNotion(client=mock_client)
    with pytest.raises(APIResponseError):
        await notion.create_page()

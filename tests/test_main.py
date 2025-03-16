from unittest.mock import AsyncMock, patch

import pytest
from httpx import Response
from notion_client.errors import APIErrorCode, APIResponseError

from src.notion import AsyncNotion


@pytest.mark.asyncio
async def test_notion_create_page_success() -> None:
    notion = AsyncNotion(notion_token="valid_token")
    with patch.object(
        notion._AsyncNotion__client.pages, "create", new_callable=AsyncMock
    ) as mock_create:
        mock_create.return_value = {"id": "test_id"}
        result = await notion.create_page(title="test_title")
        assert result == {"id": "test_id"}


@pytest.mark.asyncio
async def test_notion_create_page_retry() -> None:
    notion = AsyncNotion(notion_token="valid_token")
    with patch.object(
        notion._AsyncNotion__client.pages, "create", new_callable=AsyncMock
    ) as mock_create:
        mock_create.side_effect = [
            APIResponseError(
                response=Response(429),
                code=APIErrorCode.RateLimited,
                message="Rate limited",
            ),
            {"id": "test_id"},
        ]
        result = await notion.create_page(title="test_title")
        assert result == {"id": "test_id"}
        assert mock_create.call_count == 2


@pytest.mark.asyncio
async def test_notion_create_page_failure() -> None:
    notion = AsyncNotion(notion_token="valid_token")
    with patch.object(
        notion._AsyncNotion__client.pages, "create", new_callable=AsyncMock
    ) as mock_create:
        mock_create.side_effect = APIResponseError(
            response=Response(500),
            code=APIErrorCode.InternalServerError,
            message="Internal Server Error",
        )
        with pytest.raises(APIResponseError):
            await notion.create_page(title="test_title")

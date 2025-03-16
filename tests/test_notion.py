# tests/test_notion.py
import datetime
from unittest import mock

import pytest

from src.config import DATABASE_ID
from src.notion import AsyncNotion


@pytest.fixture
def mock_notion_client() -> mock.AsyncMock:
    """Notionクライアントのモックを作成するフィクスチャ"""
    mock_client = mock.AsyncMock()
    mock_client.pages.create.return_value = {"id": "test_page_id"}
    mock_client.databases.query.return_value = {"results": [{"id": "test_page_id"}]}
    mock_client.blocks.children.append.return_value = None
    return mock_client


@pytest.fixture
def notion_instance(mock_notion_client: mock.AsyncMock) -> AsyncNotion:
    """モック化されたクライアントを使用したAsyncNotionインスタンスを返すフィクスチャ"""
    return AsyncNotion(client=mock_notion_client)


@pytest.mark.asyncio
async def test_create_page(
    notion_instance: AsyncNotion, mock_notion_client: mock.AsyncMock
) -> None:
    """create_pageメソッドが正しく動作することを確認するテスト"""
    # メソッド実行
    page = await notion_instance.create_page()

    # 結果の検証
    assert page is not None
    assert page["id"] == "test_page_id"

    # クライアントが正しく呼び出されたことを検証
    mock_notion_client.pages.create.assert_called_once()
    call_args = mock_notion_client.pages.create.call_args[1]
    assert call_args["parent"]["database_id"] == DATABASE_ID
    assert "properties" in call_args
    assert "children" in call_args


@pytest.mark.asyncio
async def test_search_page_by_date(
    notion_instance: AsyncNotion, mock_notion_client: mock.AsyncMock
) -> None:
    """search_page_by_dateメソッドが正しく動作することを確認するテスト"""
    # テストデータ準備
    today = datetime.date.today()

    # メソッド実行
    pages = await notion_instance.search_page_by_date(today)

    # 結果の検証
    assert isinstance(pages, list)
    assert pages[0]["id"] == "test_page_id"

    # クライアントが正しく呼び出されたことを検証
    mock_notion_client.databases.query.assert_called_once()
    call_args = mock_notion_client.databases.query.call_args[1]
    assert call_args["database_id"] == DATABASE_ID
    assert call_args["filter"]["timestamp"] == "created_time"
    assert call_args["filter"]["created_time"]["equals"] == today.isoformat()


@pytest.mark.asyncio
async def test_append_block_to_page(
    notion_instance: AsyncNotion, mock_notion_client: mock.AsyncMock
) -> None:
    """append_block_to_pageメソッドが正しく動作することを確認するテスト"""
    # テストデータ準備
    page_id = "test_page_id"
    content = "This is some content!"

    # メソッド実行
    await notion_instance.append_block_to_page(page_id, content)

    # クライアントが正しく呼び出されたことを検証
    mock_notion_client.blocks.children.append.assert_called_once()
    call_args = mock_notion_client.blocks.children.append.call_args[1]
    assert call_args["block_id"] == page_id
    assert call_args["children"][0]["type"] == "paragraph"
    assert (
        call_args["children"][0]["paragraph"]["rich_text"][0]["text"]["content"]
        == content
    )


@pytest.mark.asyncio
async def test_exception_handling(mock_notion_client: mock.AsyncMock) -> None:
    """例外処理が正しく動作することを確認するテスト"""

    # モックに例外を発生させるよう設定
    class NotionAPIError(Exception):
        """Notion API特有のエラー"""

        pass

    mock_notion_client.pages.create.side_effect = NotionAPIError("API error")
    notion = AsyncNotion(client=mock_notion_client)

    # 例外が再度発生することを確認
    with pytest.raises(NotionAPIError):
        await notion.create_page()

    assert "API error" in str(mock_notion_client.pages.create.side_effect)

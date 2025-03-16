import datetime
import logging
from typing import Any

from notion_client import AsyncClient

from src.config import DATABASE_ID, NOTION_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AsyncNotion:
    def __init__(self, client: AsyncClient | None = None) -> None:
        if client:
            self._client = client
        else:
            self._client = AsyncClient(auth=NOTION_TOKEN)

    async def create_page(self) -> Any:
        logger.info("新しいページを作成します...")
        now = datetime.datetime.now()
        formatted_title = now.strftime("%Y%m%d %H:%M:%S")
        try:
            page = await self._client.pages.create(
                **{
                    "parent": {"database_id": DATABASE_ID},
                    "properties": {
                        "名前": {
                            "title": [
                                {
                                    "text": {"content": formatted_title},
                                }
                            ]
                        }
                    },
                    "children": [
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {
                                            "content": "This is some content!",
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                }
            )
            logger.info(f"ページが正常に作成されました。ページID: {page['id']}")
            return page
        except Exception as e:
            logger.exception(f"ページ作成中にエラーが発生しました: {e}")
            raise e

    async def search_page_by_date(self, date: datetime.date) -> Any:
        """指定された日付のページを検索する."""
        logger.info(f"Searching for pages by date: {date}")
        try:
            response = await self._client.databases.query(
                **{
                    "database_id": DATABASE_ID,
                    "filter": {
                        "timestamp": "created_time",
                        "created_time": {
                            "equals": date.isoformat(),
                        },
                    },
                }
            )
            logger.info(
                f"検索が正常に完了しました。{len(response['results'])} ページが見つかりました"
            )
            return response["results"]
        except Exception as e:
            logger.exception(f"ページ検索中にエラーが発生しました: {e}")
            raise e

    async def append_block_to_page(self, page_id: str, content: str) -> None:
        """指定されたページにブロックを追加する."""
        logger.info(
            f"ページにブロックを追加します。ページID: {page_id}, 内容: {content}"
        )
        try:
            await self._client.blocks.children.append(
                **{
                    "block_id": page_id,
                    "children": [
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {"content": content},
                                    },
                                ],
                            },
                        },
                    ],
                }
            )
            logger.info("ブロックが正常に追加されました。")
        except Exception as e:
            logger.exception(f"ブロック追加中にエラーが発生しました: {e}")
            raise e

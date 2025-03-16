import datetime
from typing import Any

from notion_client import AsyncClient

from src.config import DATABASE_ID, NOTION_TOKEN


class AsyncNotion:
    def __init__(self) -> None:
        self.client = AsyncClient(auth=NOTION_TOKEN)

    async def create_page(self) -> Any:
        now = datetime.datetime.now()
        formatted_title = now.strftime("%Y%m%d %H:%M:%S")
        try:
            page = await self.client.pages.create(
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
            return page
        except Exception as e:
            print(e)
            raise e

    async def search_page_by_date(self, date: datetime.date) -> Any:
        """指定された日付のページを検索する."""
        formatted_date = date.strftime("%Y%m%d")
        try:
            response = await self.client.databases.query(
                **{
                    "database_id": DATABASE_ID,
                    "filter": {
                        "property": "名前",
                        "title": {"contains": formatted_date},
                    },
                }
            )
            return response["results"]
        except Exception as e:
            print(e)
            raise e

    async def append_block_to_page(self, page_id: str, content: str) -> Any:
        """指定されたページにブロックを追加する."""
        try:
            await self.client.blocks.children.append(
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
            return True
        except Exception as e:
            print(e)
            raise e

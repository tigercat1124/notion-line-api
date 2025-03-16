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
            await self.client.pages.create(
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
            return True
        except Exception as e:
            print(e)
            raise e

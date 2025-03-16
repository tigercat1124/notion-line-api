from typing import Any

from notion_client import AsyncClient

from src.config import DATABASE_ID, NOTION_TOKEN


class AsyncNotion:
    def __init__(self) -> None:
        self.client = AsyncClient(auth=NOTION_TOKEN)

    async def create_page(self, title: str) -> Any:
        try:
            await self.client.pages.create(
                **{
                    "parent": {"database_id": DATABASE_ID},
                    "properties": {
                        "名前": {
                            "title": [
                                {
                                    "text": {"content": title},
                                }
                            ]
                        }
                    },
                }
            )
        except Exception as e:
            print(e)
            raise e

import asyncio
import os
from typing import Any

from dotenv import load_dotenv
from notion_client import AsyncClient

load_dotenv()

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = "1b7f60eb44fe80449e7dc5aa41e0caab"

notion = AsyncClient(auth=NOTION_TOKEN)


async def create_page(database_id: str, title: str) -> None:
    try:
        new_page: Any = await notion.pages.create(
            **{
                "parent": {"database_id": database_id},
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
        print(f"ページが作成されました: {new_page.get('url')}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        raise e


async def main() -> None:
    title = "新しいページ"
    await create_page(DATABASE_ID, title)


if __name__ == "__main__":
    asyncio.run(main())

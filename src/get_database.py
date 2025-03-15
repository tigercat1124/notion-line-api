import os
from typing import Any

from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = "1b7f60eb44fe80449e7dc5aa41e0caab"

notion = Client(auth=NOTION_TOKEN)


async def get_database(database_id: str) -> Any:
    try:
        database: Any = notion.databases.retrieve(database_id)
        return database
    except Exception as e:
        raise e


async def main() -> None:
    await get_database(DATABASE_ID)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

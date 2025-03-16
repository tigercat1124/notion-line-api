import asyncio
import datetime

from src.notion import AsyncNotion


async def main() -> None:
    notion = AsyncNotion()
    today = datetime.date.today()
    pages = await notion.search_page_by_date(today)

    if pages:
        page_id = pages[0]["id"]
        await notion.append_block_to_page(page_id, "This is some content!")
    else:
        await notion.create_page()


if __name__ == "__main__":
    asyncio.run(main())

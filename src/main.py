import asyncio
import datetime
import logging

from src.notion import AsyncNotion

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("メイン関数を開始します...")
    notion = AsyncNotion()
    today = datetime.date.today()
    try:
        pages = await notion.search_page_by_date(today)

        if pages:
            page_id = pages[0]["id"]
            await notion.append_block_to_page(page_id, "This is some content!")
        else:
            await notion.create_page()
        logger.info("メイン関数が正常に完了しました。")
    except Exception as e:
        logger.exception(f"メイン関数でエラーが発生しました: {e}")


if __name__ == "__main__":
    asyncio.run(main())

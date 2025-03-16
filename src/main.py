import asyncio

from src.notion import AsyncNotion


async def main() -> None:
    title = "新しいページ"
    await AsyncNotion().create_page(title)


if __name__ == "__main__":
    asyncio.run(main())

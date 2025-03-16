import asyncio

from src.notion import AsyncNotion


async def main() -> None:
    await AsyncNotion().create_page()


if __name__ == "__main__":
    asyncio.run(main())

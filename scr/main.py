import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from bot import main

if __name__ == "__main__":
    print("Бот запущен")
    asyncio.run(main())

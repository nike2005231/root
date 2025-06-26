from config.read_cfg import data_config
import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.handlers import init_heanlers
from keyboards.keyboards import menu_keyboard
from database.db import DataBase
from aiogram.fsm.context import FSMContext
from handlers.handler_dice import init_dice

bot = Bot(token=data_config())
dp = Dispatcher()
router = Router()
dp.include_router(router)
db = DataBase(db_path=r'database\root.sqlite')

@dp.message(Command('start'))
async def start(message: types.Message):
    db.insert_data(message.chat.id, message.chat.first_name, request='insert or ignore into users(id, name_user) values(?, ?)')
    await message.answer("🏠 Вы в меню", reply_markup=menu_keyboard())

async def main():
    
    await init_dice(router=router, F=F, db=db)
    await init_heanlers(router=router, F=F, db=db)
    await dp.start_polling(bot)

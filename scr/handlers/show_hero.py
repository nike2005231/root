from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import profile_keyboard

async def show_hero(router, F, db, message):
    info_data = db.get_data(message.chat.id, request='SELECT archetype, name, species FROM info WHERE chat_id == ?')[0]
    money = db.get_data(message.chat.id, request='SELECT money FROM inventory WHERE chat_id == ?')[0][0]
    status_data = db.get_data(message.chat.id, request='SELECT injury, depletion, costs, max_injury, max_depletion, max_costs FROM character_status WHERE chat_id == ?')[0]
    stats_data = db.get_data(message.chat.id, request='SELECT power, agility, luck, cunning, charm FROM stats WHERE chat_id == ?')[0]
    key_photo = db.get_data(message.chat.id, request='SELECT character_photo FROM info WHERE chat_id == ?')[0][0]
    
    caption = (
        f'🧙 *Персонаж*: {info_data[1]}\n'
        f'🏆 *Архетип*: {info_data[0]}\n'
        f'🌍 *Раса*: {info_data[2]}\n\n'
        f'💰 *Шмекели*: {money}\n\n'
        f'⚡ *Состояние*:\n'
        f'🤕 Травмы: {status_data[0]}|{status_data[3]}\n'
        f'🥵 Истощение: {status_data[1]}|{status_data[4]}\n'
        f'💸 Затраты: {status_data[2]}|{status_data[5]}\n\n'
        f'📊 *Характеристики*:\n'
        f'💪 Сила: {stats_data[0]}\n'
        f'🏃‍♂️ Сноровка: {stats_data[1]}\n'
        f'🍀 Удача: {stats_data[2]}\n'
        f'🧠 Хитрость: {stats_data[3]}\n'
        f'💫 Обаяние: {stats_data[4]}\n'
    )
    await message.answer_photo(key_photo, caption=caption, parse_mode="Markdown", reply_markup=profile_keyboard())
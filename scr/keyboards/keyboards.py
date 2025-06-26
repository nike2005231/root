from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text='🎭 Мой персонаж'), KeyboardButton(text='🎲 Мастер')],
            [KeyboardButton(text='🎮 Игра')]
        ],
        resize_keyboard=True
    )

def check_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text='✅ Да'), KeyboardButton(text='❌ Нет')]
        ],
        resize_keyboard=True
    )

def profile_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='💉 Ячейки ТИЗ')],
            [KeyboardButton(text='📚 Навыки')],
            [KeyboardButton(text='📜 История')],
            [KeyboardButton(text='✨ Скиллы')],
            [KeyboardButton(text='🏛 Отношения фракций')],
            [KeyboardButton(text='🎒 Инвентарь')],
            [KeyboardButton(text='💔 Удалить персонажа')],
            [KeyboardButton(text='🏠 Меню')]
        ],
        resize_keyboard=True
    )

def tiz_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🔝 Изменить вместимость ячейки')],
            [KeyboardButton(text='💢 Изменить Травмы')],
            [KeyboardButton(text='🥵 Изменить Истощение')],
            [KeyboardButton(text='💸 Изменить Затраты')],
            [KeyboardButton(text='🏠 Назад')]
        ],
        resize_keyboard=True
    )

def skills_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='💪 Изменить Мощь')],
            [KeyboardButton(text='🏹 Изменить Ловкость')],
            [KeyboardButton(text='🍀 Изменить Удача')],
            [KeyboardButton(text='🦊 Изменить Хитрость')],
            [KeyboardButton(text='🌟 Изменить Харизму')],
            [KeyboardButton(text='🏠 Назад')]
        ],
        resize_keyboard=True
    )

def fractions_keyboard():
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='🐾 Изменить престиж Котов')],
            [KeyboardButton(text='🦅 Изменить престиж Птиц')],
            [KeyboardButton(text='🌲 Изменить престиж Лесного альянса')],
            [KeyboardButton(text='🌿 Изменить престиж Лесного народа')],
            [KeyboardButton(text='🏠 Меню')]
        ],
        resize_keyboard=True
    )

def fractions_keyboard_choice():
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='✨ Положительный')],
            [KeyboardButton(text='💢 Отрицательный')],
            [KeyboardButton(text='🏠 Меню')]
        ],
        resize_keyboard=True
    )



def inventory_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='💰 Изменить шмекели')],  
            [KeyboardButton(text='➕ Добавить предмет')],  
            [KeyboardButton(text='➖ Удалить предмет')], 
            [KeyboardButton(text='🏠 Меню')]
        ],
        resize_keyboard=True
    )

def master_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text='📍 Сменить локацию')],
            [KeyboardButton(text='🧾 Просмотреть всех персонажей игроков')],
            [KeyboardButton(text='СМС ДЛЯ ВСЕХ')],
            [KeyboardButton(text='🎲 Бросить кубики')],
            [KeyboardButton(text='🧾 Правила')],
            [KeyboardButton(text='🏠 Меню')]
        ],
        resize_keyboard=True
    )

def game_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text='🎲 Бросить кубики')],
            [KeyboardButton(text='📍 Локация')],  
            [KeyboardButton(text='🤝 Союзники')], 
            [KeyboardButton(text='👤 Персонажи')], 
            [KeyboardButton(text='⚔️ Махыч')],    
            [KeyboardButton(text='🧾 Правила')],
            [KeyboardButton(text='🏠 Меню')]      
        ],
        resize_keyboard=True
    )

def check_hero():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text='❤️ Мне нравится мой выбор')],
            [KeyboardButton(text='🔄 Пересоздать')],
            [KeyboardButton(text='🏠 Меню')]  
        ],
        resize_keyboard=True
    )

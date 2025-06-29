from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.keyboards import tiz_keyboard
from aiogram.fsm.context import FSMContext
from states.state_change_hero import TizStats
from handlers.handlers_changes_stats.send_mes_all import send_message_all_users
from keyboards.keyboards import profile_keyboard

async def init_tiz(router, F, db, message):
    @router.message(F.text == "🔝 Изменить вместимость ячейки")
    async def capacity(message: Message, state: FSMContext):
        await message.answer(
            "📦 *Изменение вместимости ячеек*\n\n"
            "Напиши два числа через пробел:\n"
            "`1` — травмы, `2` — истощение, `3` — затраты\n"
            "_Пример: 1 5 — установить максимум травм 5_",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(TizStats.change_capacity)

    @router.message(TizStats.change_capacity)
    async def capacity_get(message: Message, state: FSMContext):
        parts = message.text.strip().split()

        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            await message.reply("❗ Введите два числа, например: 2 5")
            return

        key, value = map(int, parts)

        if key not in (1, 2, 3):
            await message.reply("❗ Первое число должно быть 1 (травмы), 2 (истощение) или 3 (затраты).")
            return
        if value > 6:
            await message.answer(f"❗️ Максимальная вместимость ячейки не может быть больше *6*", parse_mode="Markdown")
            return
        if value < 4:
            await message.answer(f"❗️ Максимальная вместимость ячейки не может быть меньше *4*", parse_mode="Markdown")
            return
        column_map = {
            1: "max_injury",
            2: "max_depletion",
            3: "max_costs"
        }
        column = column_map[key]
        db.insert_data(
            value,
            message.chat.id,
            request=f'UPDATE character_status SET {column} = ? WHERE chat_id = ?'
        )

        name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]

        text = (
            f"🛠 <b>Изменение максимального значения</b>\n\n"
            f"👤 Пользователь: <code>{name_user}</code>\n"
            f"📈 Установлено новое значение: <code>{value}</code>"
        )

        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(F.text == "💢 Изменить Травмы")
    async def change_injuries(message: Message, state: FSMContext):
        current_value = db.get_data(message.chat.id, request='select injury from character_status where chat_id == ?')[0][0]
        await message.answer(
            "🩹 *Изменение уровня травм*\n\n"
            f"Текущее значение: *{current_value}*\n"
            "Введите новое число (0-Y):\n\n",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(TizStats.change_injuries)
    
    @router.message(TizStats.change_injuries)
    async def change_injuries_get(message: Message, state: FSMContext):
        try:
            new_injuries_value = int(message.text)
        except ValueError:
            await message.reply("❗️ Введите, пожалуйста, только число!")
            return

        current_value, max_value = db.get_data(message.chat.id, request='select injury, max_injury from character_status where chat_id == ?')[0]

        if new_injuries_value > max_value + 1:
            await message.answer(f"❗️ Ячейка травмы не может быть больше *{max_value + 1}*", parse_mode="Markdown")
            return

        db.insert_data(
            new_injuries_value,
            message.chat.id,
            request='UPDATE character_status SET injury = ? WHERE chat_id = ?'
        )
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"🩹 <b>Изменение показателя травм</b>\n\n"
            f"👤 Пользователь: <code>{name_user}</code>\n"
            f"📊 Изменил значение травм:\n"
            f"• Было: <code>{current_value}</code>\n"
            f"• Стало: <code>{new_injuries_value}</code>"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(F.text == "🥵 Изменить Истощение")
    async def change_depletion(message: Message, state: FSMContext):
        current_value = db.get_data(message.chat.id, request='select depletion from character_status where chat_id == ?')[0][0]
        await message.answer(
            "💤 *Коррекция уровня истощения*\n\n"
            f"Текущий показатель: *{current_value}*\n\n"
            "✏️ Введите новое значение:\n",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(TizStats.change_depletion)

    @router.message(TizStats.change_depletion)
    async def change_depletion_get(message: Message, state: FSMContext):
        try:
            new_depletion_value = int(message.text)
        except ValueError:
            await message.reply("❗️ Введите, пожалуйста, только число!")
            return

        current_value, max_value = db.get_data(message.chat.id, request='select depletion, max_depletion from character_status where chat_id == ?')[0]
        
        if new_depletion_value > max_value + 1:
            await message.answer(f"❗️ Ячейка травмы не может быть больше *{max_value + 1}*", parse_mode="Markdown")
            return

        db.insert_data(
            new_depletion_value,
            message.chat.id,
            request='UPDATE character_status SET depletion = ? WHERE chat_id = ?'
        )
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"🥵 <b>Изменение показателя истощения</b>\n\n"
            f"👤 Пользователь: <code>{name_user}</code>\n"
            f"📊 Изменил значение истощения:\n"
            f"• Было: <code>{current_value}</code>\n"
            f"• Стало: <code>{new_depletion_value}</code>"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(F.text == "💸 Изменить Затраты")
    async def change_costs(message: Message, state: FSMContext):
        current_value = db.get_data(message.chat.id, request='select costs from character_status where chat_id == ?')[0][0]
        await message.answer(
            "💎 *Управление ресурсами*\n\n"
            f"✏️ Текущий значение: *{current_value}*\n\n"
            "📥 Введите новое количество:\n",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(TizStats.change_costs)

    @router.message(TizStats.change_costs)
    async def change_costs_get(message: Message, state: FSMContext):
        try:
            new_costs_value = int(message.text)
        except ValueError:
            await message.reply("❗️ Введите, пожалуйста, только число!")
            return

        current_value, max_value = db.get_data(message.chat.id, request='select costs, max_costs from character_status where chat_id == ?')[0]

        if new_costs_value > max_value + 1:
            await message.answer(f"❗️ Ячейка травмы не может быть больше *{max_value + 1}*", parse_mode="Markdown")
            return

        db.insert_data(
            new_costs_value,
            message.chat.id,
            request='UPDATE character_status SET costs = ? WHERE chat_id = ?'
        )
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"💸 <b>Изменение показателя затрат</b>\n\n"
            f"👤 Пользователь: <code>{name_user}</code>\n"
            f"📊 Изменил значение затрат:\n"
            f"• Было: <code>{current_value}</code>\n"
            f"• Стало: <code>{new_costs_value}</code>"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()
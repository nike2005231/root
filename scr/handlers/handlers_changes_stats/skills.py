from aiogram.types import ReplyKeyboardRemove
from states.state_change_hero import SkillsState
from handlers.handlers_changes_stats.send_mes_all import send_message_all_users
from keyboards.keyboards import profile_keyboard

async def init_skills(router, F, db, message):
    @router.message(F.text == "💪 Изменить Мощь")
    async def change_strength(message, state):
        await message.answer(
            '💥 *Введите новое значение Мощи:*\n',
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(SkillsState.strength)

    @router.message(F.text == "🏹 Изменить Ловкость")
    async def change_agility(message, state):
        await message.answer(
            '🎯 *Введите новое значение Ловкости:*\n',
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(SkillsState.agility)

    @router.message(F.text == "🍀 Изменить Удача")
    async def change_luck(message, state):
        await message.answer(
            '✨ *Введите новое значение Удачи:*\n',
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(SkillsState.luck)

    @router.message(F.text == "🦊 Изменить Хитрость")
    async def change_cunning(message, state):
        await message.answer(
            '🧠 *Введите новое значение Хитрости:*\n',
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(SkillsState.cunning)

    @router.message(F.text == "🌟 Изменить Харизму")
    async def change_charisma(message, state):
        await message.answer(
            '🌠 *Введите новое значение Харизмы:*\n',
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(SkillsState.charisma)



    @router.message(SkillsState.strength)
    async def change_strength(message, state):
        new_stat = message.text
        try:
            value = int(new_stat)
            if value not in (-2, -1, 0, 1, 2, 3):
                await message.answer("Вы можете указать значение только в пределах от -2 до 3.")
                return
            else:
                past_value = db.get_data(message.chat.id, request='SELECT power FROM stats WHERE chat_id == ?')[0][0]
                db.insert_data(value, message.chat.id, request='update stats set power = ? WHERE chat_id = ?')
                name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
                text = (
                    f"🛠 <b>Изменение характеристики: Сила</b>\n\n"
                    f"👤 Пользователь: <code>{name_user}</code>\n"
                    f"📈 Старое значение: <code>{past_value}</code>\n"
                    f"📊 Новое значение: <code>{value}</code>\n\n"
                    f"✨ Ваша сила успешно обновлена!"
                )

                await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
                await state.clear()

        except ValueError as ex:
            await message.answer("Вы можете указать только числовой параметр.")


    @router.message(SkillsState.agility)
    async def change_agility(message, state):
        new_stat = message.text
        try:
            value = int(new_stat)
            if value not in (-2, -1, 0, 1, 2, 3):
                await message.answer("Вы можете указать значение только в пределах от -2 до 3.")
                return
            else:
                past_value = db.get_data(message.chat.id, request='SELECT agility FROM stats WHERE chat_id == ?')[0][0]
                db.insert_data(value, message.chat.id, request='update stats set agility = ? WHERE chat_id = ?')
                name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
                text = (
                    f"🛠 <b>Изменение характеристики: Ловкость</b>\n\n"
                    f"👤 Пользователь: <code>{name_user}</code>\n"
                    f"📈 Старое значение: <code>{past_value}</code>\n"
                    f"📊 Новое значение: <code>{value}</code>\n\n"
                    f"✨ Ваша ловкость успешно обновлена!"
                )
                await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
                await state.clear()
        except ValueError as ex:
            await message.answer("Вы можете указать только числовой параметр.")


    @router.message(SkillsState.luck)
    async def change_luck(message, state):
        new_stat = message.text
        try:
            value = int(new_stat)
            if value not in (-2, -1, 0, 1, 2, 3):
                await message.answer("Вы можете указать значение только в пределах от -2 до 3.")
                return
            else:
                past_value = db.get_data(message.chat.id, request='SELECT luck FROM stats WHERE chat_id == ?')[0][0]
                db.insert_data(value, message.chat.id, request='update stats set luck = ? WHERE chat_id = ?')
                name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]

                text = (
                    f"🛠 <b>Изменение характеристики: Удача</b>\n\n"
                    f"👤 Пользователь: <code>{name_user}</code>\n"
                    f"📈 Старое значение: <code>{past_value}</code>\n"
                    f"📊 Новое значение: <code>{value}</code>\n\n"
                    f"✨ Ваша удача успешно обновлена!"
                )
                await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
                await state.clear()
        except ValueError as ex:
            await message.answer("Вы можете указать только числовой параметр.")


    @router.message(SkillsState.cunning)
    async def change_cunning(message, state):
        new_stat = message.text
        try:
            value = int(new_stat)
            if value not in (-2, -1, 0, 1, 2, 3):
                await message.answer("Вы можете указать значение только в пределах от -2 до 3.")
                return
            else:
                past_value = db.get_data(message.chat.id, request='SELECT cunning FROM stats WHERE chat_id == ?')[0][0]
                db.insert_data(value, message.chat.id, request='update stats set cunning = ? WHERE chat_id = ?')
                name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
                
                text = (
                    f"🛠 <b>Изменение характеристики: Хитрость</b>\n\n"
                    f"👤 Пользователь: <code>{name_user}</code>\n"
                    f"📈 Старое значение: <code>{past_value}</code>\n"
                    f"📊 Новое значение: <code>{value}</code>\n\n"
                    f"✨ Ваша хитрость успешно обновлена!"
                )
                await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
                await state.clear()
        except ValueError as ex:
            await message.answer("Вы можете указать только числовой параметр.")


    @router.message(SkillsState.charisma)
    async def change_charisma(message, state):
        new_stat = message.text
        try:
            value = int(new_stat)
            if value not in (-2, -1, 0, 1, 2, 3):
                await message.answer("Вы можете указать значение только в пределах от -2 до 3.")
                return
            else:
                past_value = db.get_data(message.chat.id, request='SELECT charisma FROM stats WHERE chat_id == ?')[0][0]
                db.insert_data(value, message.chat.id, request='update stats set charisma = ? WHERE chat_id = ?')
                name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
                
                text = (
                    f"🛠 <b>Изменение характеристики: Харизма</b>\n\n"
                    f"👤 Пользователь: <code>{name_user}</code>\n"
                    f"📈 Старое значение: <code>{past_value}</code>\n"
                    f"📊 Новое значение: <code>{value}</code>\n\n"
                    f"✨ Ваша харизма успешно обновлена!"
                )
                await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
                await state.clear()
        except ValueError as ex:
            await message.answer("Вы можете указать только числовой параметр.")
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from states.state_change_hero import FractionStats
from keyboards.keyboards import profile_keyboard, fractions_keyboard_choice, fractions_keyboard
from handlers.handlers_changes_stats.send_mes_all import send_message_all_users

async def init_fractions(router, F, db, message):

    @router.message(F.text == "✨ Положительный")
    async def change_positive_prestige(message: Message, state: FSMContext):
        current_state = await state.get_state()
        
        if current_state == FractionStats.cats_choice.state: 
            rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == 3:
                await message.answer("🎉 Поздравляем! У вас максимальная репутация, увеличивать некуда!")

            else:
                await message.answer(
                    '🐾 <b>Изменение положительного престижа Маркизата</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '✨ Чем выше число - тем лучше отношение фракции'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации -3, -2, -1, 0: от 0 до 5\n'
                    '• При репутации 1: от 0 до 10\n'
                    '• При репутации 2: от 0 до 15',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.cats_p)

        elif current_state == FractionStats.birds_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == 3:
                await message.answer("🎉 Поздравляем! У вас максимальная репутация, увеличивать некуда!")

            else:
                await message.answer(
                    '🦅 <b>Изменение положительного престижа Крылатых Династий</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '✨ Чем выше число - тем лучше отношение фракции'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации -3, -2, -1, 0: от 0 до 5\n'
                    '• При репутации 1: от 0 до 10\n'
                    '• При репутации 2: от 0 до 15',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.birds_p)

        elif current_state == FractionStats.alliance_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == 3:
                await message.answer("🎉 Поздравляем! У вас максимальная репутация, увеличивать некуда!")

            else:
                await message.answer(
                    '🌳 <b>Изменение положительного престижа Лесного Альянса</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '✨ Чем выше число - тем лучше отношение фракции'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации -3, -2, -1, 0: от 0 до 5\n'
                    '• При репутации 1: от 0 до 10\n'
                    '• При репутации 2: от 0 до 15',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.alliance_p)

        elif current_state == FractionStats.nation_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == 3:
                await message.answer("🎉 Поздравляем! У вас максимальная репутация, увеличивать некуда!")

            else:
                await message.answer(
                    '🍃 <b>Изменение положительного престижа Лесного Народа</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '✨ Чем выше число - тем лучше отношение фракции'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации -3, -2, -1, 0: от 0 до 5\n'
                    '• При репутации 1: от 0 до 10\n'
                    '• При репутации 2: от 0 до 15',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.nation_p)

    @router.message(F.text == "💢 Отрицательный")
    async def change_negative_prestige(message: Message, state: FSMContext):
        current_state = await state.get_state()
        if current_state == FractionStats.cats_choice.state: 
            rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == -3:
                await message.answer("🎉 Поздравляем! Коты считают что вы хуесос, хуже некуда!")
            else:
                await message.answer(
                    '🐾 <b>Изменение отрицательного престижа Маркизата</b>\n\n'
                    '▫️ Введите <b>целое отрицательное число</b>\n'
                    '💢 Чем ниже число - тем хуже отношение фракции\n\n'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации 3, 2, 1, 0: от -3 до 0\n'
                    '• При репутации -1: от -6 до 0\n'
                    '• При репутации -2: от -9 до 0',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.cats_m)

        elif current_state == FractionStats.birds_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == -3:
                await message.answer("🎉 Поздравляем! Птицы считают что вы хуесос, хуже некуда!")
            else:
                await message.answer(
                    '🦅 <b>Изменение отрицательного престижа Крылатых Династий</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '💢 Чем ниже число - тем хуже отношение фракции\n\n'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации 3, 2, 1, 0: от -3 до 0\n'
                    '• При репутации -1: от -6 до 0\n'
                    '• При репутации -2: от -9 до 0',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.birds_m)

        elif current_state == FractionStats.alliance_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == -3:
                await message.answer("🎉 Поздравляем! Альянс считает что вы хуесос, хуже некуда!")
            else:
                await message.answer(
                    '🌳 <b>Изменение отрицательного престижа Лесного Альянса</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '💢 Чем ниже число - тем хуже отношение фракции\n\n'
                    '<i>Ограничения ввода:</i>\n'
                    f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации 3, 2, 1, 0: от -3 до 0\n'
                    '• При репутации -1: от -6 до 0\n'
                    '• При репутации -2: от -9 до 0',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.alliance_m)

        elif current_state == FractionStats.nation_choice.state:
            rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]
            if rep == -3:
                await message.answer("🎉 Поздравляем! Народ считает что вы хуесос, хуже некуда!")
            else:
                await message.answer(
                    '🍃 <b>Изменение отрицательного престижа Лесного Народа</b>\n\n'
                    '▫️ Введите <b>целое положительное число</b>\n'
                    '▫️ Например: <i>1, 4, 9, 16</i>\n\n'
                    '💢 Чем ниже число - тем хуже отношение фракции\n\n'
                    '<i>Ограничения ввода:</i>\n'
                   f'<b>Ваша текущая репутация:</b> <code>{rep}</code>\n\n'
                    '• При репутации 3, 2, 1, 0: от -3 до 0\n'
                    '• При репутации -1: от -6 до 0\n'
                    '• При репутации -2: от -9 до 0',
                    parse_mode="HTML",
                    reply_markup=ReplyKeyboardRemove()
                )
                await state.set_state(FractionStats.nation_m)

    @router.message(F.text == "🐾 Изменить престиж Котов")
    async def change_cats(message, state):
        await message.answer(
            'Выбери режим:',
            parse_mode="Markdown",
            reply_markup=fractions_keyboard_choice()
        )
        await state.set_state(FractionStats.cats_choice)

    @router.message(F.text == "🦅 Изменить престиж Птиц")
    async def change_birds(message, state):
        await message.answer(
            'Выбери режим:',
            parse_mode="Markdown",
            reply_markup=fractions_keyboard_choice()
        )
        await state.set_state(FractionStats.birds_choice)

    @router.message(F.text == "🌲 Изменить престиж Лесного альянса")
    async def change_trees(message, state):
        await message.answer(
            'Выбери режим:',
            parse_mode="Markdown",
            reply_markup=fractions_keyboard_choice()
        )
        await state.set_state(FractionStats.alliance_choice)

    @router.message(F.text == "🌿 Изменить престиж Лесного народа")
    async def change_mama(message, state):
        await message.answer(
            'Выбери режим:',
            parse_mode="Markdown",
            reply_markup=fractions_keyboard_choice()
        )
        await state.set_state(FractionStats.nation_choice)

    async def recalculation_positive(colum_rep, colum_p, colum_m, message, db): #marquisate_rep marquisate_prestige_p marquisate_prestige_m

        while True:
            rep = db.get_data(message.chat.id, request=f'SELECT {colum_rep} FROM fractions WHERE chat_id == ?')[0][0]
            prestige_p = db.get_data(message.chat.id, request=f'SELECT {colum_p} FROM fractions WHERE chat_id == ?')[0][0]
            prestige_m = db.get_data(message.chat.id, request=f'SELECT {colum_m} FROM fractions WHERE chat_id == ?')[0][0]

            if rep == 0 and prestige_m <= -3: #БЛЯТЬ ЭТО ПИЗДЕЦ НО ТУТ 0 а ниже -1 я долго голову ебал
                value_rep = rep - 1
                value_m = prestige_m + 3
                db.insert_data(value_rep, message.chat.id, request=f'UPDATE fractions SET {colum_rep} = ? WHERE chat_id = ?')
                db.insert_data(value_m, message.chat.id, request=f'UPDATE fractions SET {colum_m} = ? WHERE chat_id = ?')

            elif rep == -1 and prestige_m <= -6:
                value_rep = rep - 1
                value_m = prestige_m + 6
                db.insert_data(value_rep, message.chat.id, request=f'UPDATE fractions SET {colum_rep} = ? WHERE chat_id = ?')
                db.insert_data(value_m, message.chat.id, request=f'UPDATE fractions SET {colum_m} = ? WHERE chat_id = ?')
            else:
                break

    async def recalculation_negative(colum_rep, colum_p, colum_m, message, db): #marquisate_rep marquisate_prestige_p marquisate_prestige_m
        while True:
            rep = db.get_data(message.chat.id, request=f'SELECT {colum_rep} FROM fractions WHERE chat_id == ?')[0][0]
            prestige_p = db.get_data(message.chat.id, request=f'SELECT {colum_p} FROM fractions WHERE chat_id == ?')[0][0]
            prestige_m = db.get_data(message.chat.id, request=f'SELECT {colum_m} FROM fractions WHERE chat_id == ?')[0][0]
            if rep == 0 and prestige_p >= 5: #БЛЯТЬ ЭТО ПИЗДЕЦ НО ТУТ 0 а ниже -1 я долго голову ебал
                value_rep = rep + 1
                value_p = prestige_p - 5
                db.insert_data(value_rep, message.chat.id, request=f'UPDATE fractions SET {colum_rep} = ? WHERE chat_id = ?')
                db.insert_data(value_p, message.chat.id, request=f'UPDATE fractions SET {colum_p} = ? WHERE chat_id = ?')

            elif rep == 1 and prestige_p >= 10:
                value_rep = rep + 1
                value_p = prestige_p - 10
                db.insert_data(value_rep, message.chat.id, request=f'UPDATE fractions SET {colum_rep} = ? WHERE chat_id = ?')
                db.insert_data(value_p, message.chat.id, request=f'UPDATE fractions SET {colum_p} = ? WHERE chat_id = ?')
            else:
                break

    @router.message(FractionStats.cats_p)
    async def marquisate_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep <= 0 and not 0 <= data_user <= 5:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 5!")
                return

            elif last_rep == 1 and not 0 <= data_user <= 10:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 10!")
                return

            elif last_rep == 2 and not 0 <= data_user <= 15:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 15!")
                return

            if last_rep <= 0 and data_user == 5:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            elif last_rep == 1 and data_user == 10:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            elif last_rep == 2 and data_user == 15:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET marquisate_prestige_p = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_positive('marquisate_rep', 'marquisate_prestige_p', 'marquisate_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Престижа Маркисата</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.birds_p)
    async def winged_dynasties_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep <= 0 and not 0 <= data_user <= 5:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 5!")
                return

            elif last_rep == 1 and not 0 <= data_user <= 10:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 10!")
                return

            elif last_rep == 2 and not 0 <= data_user <= 15:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 15!")
                return

            if last_rep <= 0 and data_user == 5:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            elif last_rep == 1 and data_user == 10:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            elif last_rep == 2 and data_user == 15:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET winged_dynasties_prestige_p = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_positive('winged_dynasties_rep', 'winged_dynasties_prestige_p', 'winged_dynasties_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Престижа Крылатых Династий</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.alliance_p)
    async def forest_alliance_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep <= 0 and not 0 <= data_user <= 5:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 5!")
                return

            elif last_rep == 1 and not 0 <= data_user <= 10:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 10!")
                return

            elif last_rep == 2 and not 0 <= data_user <= 15:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 15!")
                return

            if last_rep <= 0 and data_user == 5:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            elif last_rep == 1 and data_user == 10:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            elif last_rep == 2 and data_user == 15:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET forest_alliance_prestige_p = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_positive('forest_alliance_rep', 'forest_alliance_prestige_p', 'forest_alliance_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Престижа Лесного Альянса</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.nation_p)
    async def woodland_folk_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep <= 0 and not 0 <= data_user <= 5:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 5!")
                return

            elif last_rep == 1 and not 0 <= data_user <= 10:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 10!")
                return

            elif last_rep == 2 and not 0 <= data_user <= 15:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до 15!")
                return

            if last_rep <= 0 and data_user == 5:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            elif last_rep == 1 and data_user == 10:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            elif last_rep == 2 and data_user == 15:
                value = last_rep + 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET woodland_folk_prestige_p = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_positive('woodland_folk_rep', 'woodland_folk_prestige_p', 'woodland_folk_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Престижа Лесного Народа</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.cats_m)
    async def marquisate_negative_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep >= 0 and not -3 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -3!")
                return

            elif last_rep == -1 and not -6 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -6!")
                return

            elif last_rep == -2 and not -9 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return
            
            elif last_rep == -3:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            if last_rep >= 0 and data_user == -3:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            elif last_rep == -1 and data_user == -6:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            elif last_rep == -2 and data_user == -9:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET marquisate_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET marquisate_prestige_m = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT marquisate_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_negative('marquisate_rep', 'marquisate_prestige_p', 'marquisate_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Негативного престижа Маркисата</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.birds_m)
    async def winged_dynasties_negative_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep >= 0 and not -3 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -3!")
                return

            elif last_rep == -1 and not -6 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -6!")
                return

            elif last_rep == -2 and not -9 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            elif last_rep == -3:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            if last_rep >= 0 and data_user == -3:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            elif last_rep == -1 and data_user == -6:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            elif last_rep == -2 and data_user == -9:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET winged_dynasties_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET winged_dynasties_prestige_m = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT winged_dynasties_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_negative('winged_dynasties_rep', 'winged_dynasties_prestige_p', 'winged_dynasties_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Негативного престижа Крылатых Династий</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.alliance_m)
    async def forest_alliance_negative_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep >= 0 and not -3 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -3!")
                return

            elif last_rep == -1 and not -6 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -6!")
                return

            elif last_rep == -2 and not -9 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            elif last_rep == -3:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            if last_rep >= 0 and data_user == -3:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            elif last_rep == -1 and data_user == -6:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            elif last_rep == -2 and data_user == -9:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET forest_alliance_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET forest_alliance_prestige_m = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT forest_alliance_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_negative('forest_alliance_rep', 'forest_alliance_prestige_p', 'forest_alliance_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Негативного престижа Лесного Альянса</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return


    @router.message(FractionStats.nation_m)
    async def woodland_folk_negative_prestige_get(message, state):
        data_user = message.text
        try:
            last_rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]
            data_user = int(data_user)
            input_user = int(data_user)

            if last_rep >= 0 and not -3 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -3!")
                return

            elif last_rep == -1 and not -6 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -6!")
                return

            elif last_rep == -2 and not -9 <= data_user <= 0:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            elif last_rep == -3:
                await message.answer(f"⚠️ Введено: {data_user} (репутация {last_rep}) - допустимо только от 0 до -9!")
                return

            if last_rep >= 0 and data_user == -3:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            elif last_rep == -1 and data_user == -6:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            elif last_rep == -2 and data_user == -9:
                value = last_rep - 1
                data_user = 0
                db.insert_data(value, message.chat.id, request='UPDATE fractions SET woodland_folk_rep = ? WHERE chat_id = ?')

            db.insert_data(data_user, message.chat.id, request='UPDATE fractions SET woodland_folk_prestige_m = ? WHERE chat_id = ?')
            name_user = db.get_data(message.chat.id, request='SELECT name FROM info WHERE chat_id == ?')[0][0]
            rep = db.get_data(message.chat.id, request='SELECT woodland_folk_rep FROM fractions WHERE chat_id == ?')[0][0]

            await recalculation_negative('woodland_folk_rep', 'woodland_folk_prestige_p', 'woodland_folk_prestige_m', message, db)

            text = (
                f"🛠 <b>Изменение Негативного престижа Лесного Народа</b>\n\n"
                f"👤 Пользователь: <code>{name_user}</code>\n"
                f"▫️ Установил новое значение: <code>{input_user}</code>\n"
                f"▫️ Текущая репутация: <code>{rep}</code>"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
            await state.clear()

        except ValueError:
            await message.answer(
                "⚠️ Ошибка ввода\n\n"
                "▪️ Необходимо ввести целое число\n"
                f"▪️ Вы ввели: *{data_user}*\n\n"
                "Пожалуйста, попробуйте еще раз"
            )
            return
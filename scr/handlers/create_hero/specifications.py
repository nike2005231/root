from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.specifications import specifications_choice
import textwrap

async def specifications_hero(router):
    @router.message(CreateHero.choosing_specifications)
    async def specifications_chosen(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_choice_specifications = specifications_choice(archetype=data['archetype'])
            choice_user = message.text

            Power = int(data_choice_specifications[1])
            Agility = int(data_choice_specifications[2])
            Luck = int(data_choice_specifications[3])
            Cunning = int(data_choice_specifications[4])
            Charm = int(data_choice_specifications[5])

            choice_user = int(choice_user)

            match choice_user:
                case 1:
                    if Power != 2:
                        Power += 1
                    else:
                        await message.answer("⚠️ <b>Мощь</b> уже имеет максимальное значение (2)", parse_mode="HTML")
                        return
                case 2:
                    if Agility != 2:
                        Agility += 1
                    else:
                        await message.answer("⚠️ <b>Сноровка</b> уже имеет максимальное значение (2)", parse_mode="HTML")
                        return
                case 3:
                    if Luck != 2:
                        Luck += 1
                    else:
                        await message.answer("⚠️ <b>Удача</b> уже имеет максимальное значение (2)", parse_mode="HTML")
                        return
                case 4:
                    if Cunning != 2:
                        Cunning += 1
                    else:
                        await message.answer("⚠️ <b>Хитрость</b> уже имеет максимальное значение (2)", parse_mode="HTML")
                        return
                case 5:
                    if Charm != 2:
                        Charm += 1
                    else:
                        await message.answer("⚠️ <b>Шарм</b> уже имеет максимальное значение (2)", parse_mode="HTML")
                        return
                case _:
                    await message.answer("❌ Введите цифру от 1 до 5", parse_mode="HTML")
                    return

            await state.update_data({
                'power': Power,
                'agility': Agility,
                'luck': Luck,
                'cunning': Cunning,
                'charm': Charm
            })
            await state.set_state(CreateHero.getting_reputation)

            await message.answer(
                textwrap.dedent(f"""
                🌟 *Какой фракции помогли?* 🌟
                +2 очка престижа
                
                📌 Отправь мне *одну цифру* от 1 до 4:
                
                1️⃣ Маркисат
                2️⃣ Крылатые династии
                3️⃣ Лесной союз
                4️⃣ Обитатели Леса
                """),
                parse_mode="Markdown"
            )

        except ValueError:
            await message.answer("❌ Введите цифру от 1 до 4", parse_mode="HTML")
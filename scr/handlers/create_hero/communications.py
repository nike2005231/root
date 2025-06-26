from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.communications import communications_choice
import textwrap

async def communications_hero(router):      
    @router.message(CreateHero.choosing_communications)
    async def choosing_communications(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            archetype = data.get("archetype", "").lower()

            data_communications = communications_choice(archetype)
            roles, description_1, description_2 = data_communications
            role_1, role_2 = roles

            names = message.text.strip().split()

            if len(names) != 2:
                await message.answer(
                    "⚠️ Пожалуйста, введите *ровно два имени* через пробел.\nПример: `Саша Влад`",
                    parse_mode="Markdown"
                )
                return

            name_1, name_2 = names

            communications_full = textwrap.dedent(f"""
                {name_1} — {role_1}
                {name_2} — {role_2}

                {description_1}

                {description_2}
            """).strip()

            await state.update_data({'communications': communications_full})

            await state.set_state(CreateHero.getting_photo)

            await message.answer(
                textwrap.dedent(f"""
                    🌟 *ФИНАЛЬНЫЙ ШАГ: ФОТО ПЕРСОНАЖА* 🌟
                    
                    Пожалуйста, отправьте фото вашего персонажа:
                    
                    📸 Это будет его визуальным представлением
                    🖼️ Можно прислать готовое изображение

                    ⚠️ Убедитесь, что фото хорошо передает характер вашего героя!
                """),
                parse_mode="Markdown"
            )

        except KeyError:
            await message.answer("⚠️ Ошибка: неизвестный архетип. Пожалуйста, вернитесь и выберите архетип заново.")
        except Exception as e:
            await message.answer(f"⚠️ Произошла ошибка: {str(e)}")
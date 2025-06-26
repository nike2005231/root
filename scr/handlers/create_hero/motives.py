from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.motives import motives_choice
from archetype.personality import personality_choice
from archetype.specifications import specifications_choice
import textwrap

async def motive_hero(router):
    @router.message(CreateHero.choosing_motives)
    async def motives_chosen(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_choice_motive = motives_choice(archetype=data['archetype'])
            data_choice_personality = personality_choice(archetype=data['archetype'])
            choice_user = message.text
            parts = choice_user.split()
            if len(parts) != 2:
                await message.answer("❌ Нужно ввести ровно две цифры через пробел!\nПример: <b>1 3</b>", parse_mode="HTML")
                return    

            num1, num2 = int(parts[0]), int(parts[1])

            if not (1 <= num1 <= 4) or not (1 <= num2 <= 4):
                await message.answer("❌ Цифры должны быть от 1 до 4!\nПопробуй еще раз:")
                return
            
            if num1 == num2:
                await message.answer("❌ Нужно выбрать два разных мотива!\nУкажи разные цифры:")
                return

            finished_text = f"{data_choice_motive[num1]}\n\n{data_choice_motive[num2]}"
            await state.update_data(motives=finished_text)
            await state.set_state(CreateHero.choosing_personality)

            await message.answer(
                textwrap.dedent(f"""
                ✨ *Выбери характеристику* ✨
                
                🔹Отправь мне *ОДНУ цифру* от 1 до 2:
                🔹Очистите шкалу истощения:

                1️⃣ {data_choice_personality[1]}
                2️⃣ {data_choice_personality[2]}
                """),
                parse_mode="Markdown"
            )

        except ValueError:
            await message.answer("❌ Нужно вводить только цифры!\nПример правильного ввода: <b>2 4</b>", parse_mode="HTML")

    @router.message(CreateHero.choosing_personality)
    async def personality_chosen(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_choice_personality = personality_choice(archetype=data['archetype'])
            data_choice_specifications = specifications_choice(archetype=data['archetype'])
            choice_user = message.text
            if int(choice_user) not in (1, 2):
                await message.answer("❌ Нужно ввести ровно одну цифру в ренже от 1 до 2!\nПример: <b>1</b>", parse_mode="HTML")
                return    

            num = int(choice_user)

            finished_text = f"{data_choice_personality[num]}"
            await state.update_data(personality=finished_text)
            await state.set_state(CreateHero.choosing_specifications)

            await message.answer(
                "💪 *УЛУЧШЕНИЕ ХАРАКТЕРИСТИКИ*\n\n"
                "Выбери цифру от 1️⃣ до 5️⃣ для улучшения:\n"
                "➕ Можно добавить +1 к характеристике\n"
                "⚠️ Максимальное значение - 2 (если в правилах не указано иное)\n\n"
                "🔢 *Введи цифру характеристики для улучшения:*\n\n"
                f"🎯 *ВАШИ ХАРАКТЕРИСТИКИ* 🎯\n"
                f"{textwrap.dedent(data_choice_specifications[0])}",
                parse_mode="Markdown"
            )

        except ValueError:
            await message.answer("❌ Нужно вводить только цифры!\nПример правильного ввода: <b>2</b>", parse_mode="HTML")
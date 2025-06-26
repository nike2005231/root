from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.rogue_skills import rouge_skill_choice
from archetype.weapon_skills import weapon_skill_choice
from archetype.moves import moves_choice
import textwrap

async def weapon_rogue_skills(router):    
    @router.message(CreateHero.recording_receptions)
    async def recording_receptions(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_rouge_skill = rouge_skill_choice(data['archetype'].lower())
            data_weapon_skill = weapon_skill_choice(data['archetype'].lower())
            choice_user = list(map(int, message.text.split()))
            
            if len(choice_user) != len(set(choice_user)):
                await message.answer("❌ Все числа должны быть разными!")
                return
                
            if data['archetype'].lower() == 'судья':
                if len(choice_user) != 1:
                    await message.answer("❌ Судья введите одно число!\nПример: <b>1</b>", parse_mode="HTML")
                    return
            elif data['archetype'].lower() == 'вор':
                if len(choice_user) != 4:
                    await message.answer("❌ Вор введите четыре числа!\nПример: <b>1 2 3 4</b>", parse_mode="HTML")
                    return
            
            max_skill_index = len(data_rouge_skill) - 1
            if any(x < 0 or x > max_skill_index for x in choice_user):
                await message.answer(f"❌ Введите числа от 0 до {max_skill_index}!")
                return
                
            selected_skills = [data_rouge_skill[x] for x in choice_user]
            text_finish = '\n'.join(selected_skills)

            await state.update_data({'rogue_skills': text_finish})
            await state.set_state(CreateHero.choosing_weapon_skill)

            await message.answer(
                textwrap.dedent(f"""
                    ⚔️ *Оружейное мастерство {data['archetype'].upper()}* ⚔️
                    
                    Выберите один навык владения оружием:
                    
                    1️⃣ {data_weapon_skill[1]}
                    2️⃣ {data_weapon_skill[2]}
                    3️⃣ {data_weapon_skill[3]}
                    4️⃣ {data_weapon_skill[4]}
                    
                    ✨ Выберите номер от *1* до *4*
                    📝 Отправьте цифру (например: "2")
                    """),
                    parse_mode="Markdown"
                )

        except ValueError:
            await message.answer("❌ Пожалуйста, введите только числа, разделенные пробелами!")


    @router.message(CreateHero.choosing_weapon_skill)
    async def choosing_weapon_skill(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_weapon_skill = weapon_skill_choice(data['archetype'].lower())
            data_moves = moves_choice(data['archetype'].lower())
            choice_user = message.text.strip()

            if not choice_user.isdigit() or int(choice_user) not in {1, 2, 3, 4}:
                await message.answer("❌ Неверный ввод! Пожалуйста, введите ОДНО число от 1 до 4.")
                return
                
            choice = int(choice_user)
            text_finish = data_weapon_skill[choice]
            await state.update_data({'weapon_skill': text_finish})

            if data['archetype'].lower() != 'ремесленник':
                await message.answer(
                    textwrap.dedent(f"""
                    🎭 *{data['archetype'].capitalize()} - выберите три хода* 🎭
                    
                    Вам доступны особые умения вашего архетипа:
                    
                    1️⃣ {data_moves[1]}
                    2️⃣ {data_moves[2]}
                    3️⃣ {data_moves[3]}
                    4️⃣ {data_moves[4]}
                    5️⃣ {data_moves[5]}
                    6️⃣ {data_moves[6]}
                    
                    ✨ Выберите *три* хода из предложенных
                    📝 Отправьте номера через пробел (например: "1 3 5")
                    🚨 Внимание! Выбор будет окончательным
                    """),
                    parse_mode="Markdown"
                )
            else:
                await message.answer(
                    textwrap.dedent(f"""
                    🛠️ *Ремесленник - ваши умения* 🛠️

                    📦 *Автоматически получаете:*
                    👉 *Набор инструментов*: {data_moves[5]}
                    👉 *Починить*: {data_moves[6]}

                    ➕ *Дополнительно выберите 1 ход:*
                    1️⃣ {data_moves[1]}
                    2️⃣ {data_moves[2]}
                    3️⃣ {data_moves[3]}
                    4️⃣ {data_moves[4]}

                    ✏️ Введите цифру от 1 до 4
                    Пример: "3"
                    """),
                    parse_mode="Markdown"
                )
            await state.set_state(CreateHero.choosing_moves)
        except Exception as ex:
            print(f"Ошибка при выборе навыка оружия: {ex}")
            await message.answer("⚠️ Произошла ошибка при обработке вашего выбора. Попробуйте еще раз.")
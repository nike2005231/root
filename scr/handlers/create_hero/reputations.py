from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.rogue_skills import rouge_skill_choice
from archetype.weapon_skills import weapon_skill_choice
import textwrap

async def reputations_hero(router):    
    @router.message(CreateHero.getting_reputation)
    async def reputation_handler(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            choice_user = int(message.text)
            
            if choice_user not in (1, 2, 3, 4):
                await message.answer("❌ Нужно ввести цифру от 1 до 4!\nПример: <b>1</b>", parse_mode="HTML")
                return

            # Получаем ТЕКУЩИЕ значения из состояния
            marquisate = data.get('marquisate_prestige_p', 0)
            winged = data.get('winged_dynasties_prestige_p', 0)
            forest = data.get('forest_alliance_prestige_p', 0)
            woodland = data.get('woodland_folk_prestige_p', 0)

            # Меняем только выбранную фракцию
            match choice_user:
                case 1:
                    marquisate += 2
                case 2:
                    winged += 2
                case 3:
                    forest += 2
                case 4:
                    woodland += 2

            # Сохраняем ВСЕ значения
            await state.update_data({
                'marquisate_prestige_p': marquisate,
                'winged_dynasties_prestige_p': winged,
                'forest_alliance_prestige_p': forest,
                'woodland_folk_prestige_p': woodland
            })

            await message.answer(
                textwrap.dedent(f"""
                💢 *Какой фракции навредили?* 💢
                -1 очка престижа
                
                📌 Отправь мне *одну цифру* от 1 до 4:
                
                1️⃣ Маркизат
                2️⃣ Крылатые династии
                3️⃣ Лесной союз
                4️⃣ Обитатели Леса
                """),
                parse_mode="Markdown"
            )
            
            await state.set_state(CreateHero.take_reputation)

        except ValueError:
            await message.answer("❌ Вводите только цифры!\nПример: <b>2</b>", parse_mode="HTML")


    @router.message(CreateHero.take_reputation)
    async def faction_not_helped(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            choice_user = int(message.text) 
            data_weapon_skill = weapon_skill_choice(data['archetype'].lower())
            data_rouge_skill = rouge_skill_choice(data['archetype'].lower())
            
            if choice_user not in (1, 2, 3, 4):
                await message.answer("❌ Нужно ввести ровно одну цифру от 1 до 4!\nПример: <b>1</b>", parse_mode="HTML")
                return    

            # Инициализируем переменные с текущими значениями (если они есть)
            marquisate_prestige_m = data.get('marquisate_prestige_m', 0)
            winged_dynasties_prestige_m = data.get('winged_dynasties_prestige_m', 0)
            forest_alliance_prestige_m = data.get('forest_alliance_prestige_m', 0)
            woodland_folk_prestige_m = data.get('woodland_folk_prestige_m', 0)

            marquisate = data.get('marquisate_prestige_p')
            winged = data.get('winged_dynasties_prestige_p')
            forest = data.get('forest_alliance_prestige_p')
            woodland = data.get('woodland_folk_prestige_p')

            match choice_user:
                case 1:
                    marquisate_prestige_m -= 1
                case 2:
                    winged_dynasties_prestige_m -= 1
                case 3:
                    forest_alliance_prestige_m -= 1
                case 4:
                    woodland_folk_prestige_m -= 1

            await state.update_data({
                'marquisate_prestige_m': marquisate_prestige_m,
                'winged_dynasties_prestige_m': winged_dynasties_prestige_m,
                'forest_alliance_prestige_m': forest_alliance_prestige_m,
                'woodland_folk_prestige_m': woodland_folk_prestige_m
            })
            
            roles = {'авантюрист':9, 'судья':10, 'налетчик':9, 'следопыт':9, 'ронин':11, 'поджигатель':8, 'вор':6, 'ремесленник':8, 'скиталец':9}
            await state.update_data({'money': roles[data['archetype'].lower()]})

            await message.answer(
                textwrap.dedent(f"""
                ✅ *Репутация обновлена!* ✅

                Текущий статус:
                1️⃣ Маркисат: {marquisate} | {marquisate_prestige_m}
                2️⃣ Крылатые династии: {winged} | {winged_dynasties_prestige_m}
                3️⃣ Лесной союз: {forest} | {forest_alliance_prestige_m}
                4️⃣ Обитатели Леса: {woodland} | {woodland_folk_prestige_m}
                """),
                parse_mode="Markdown"
            )
            
            if data['archetype'].lower() in ('судья', 'вор'):
                await state.set_state(CreateHero.recording_receptions)
                await message.answer(
                    textwrap.dedent(f"""
                    🃏 *Мастерство {data['archetype'].lower()}* 🃏
                    
                    Вам доступны особые плутовские приемы:
                    
                    1️⃣ {data_rouge_skill[1]}
                    2️⃣ {data_rouge_skill[2]}
                    3️⃣ {data_rouge_skill[3]}
                    4️⃣ {data_rouge_skill[4]}
                    5️⃣ {data_rouge_skill[5]}
                    6️⃣ {data_rouge_skill[6]}
                    7️⃣ {data_rouge_skill[7]}
                    8️⃣ {data_rouge_skill[8]}
                    9️⃣ {data_rouge_skill[9]}
                    
                    ✨ Выберите *{data_rouge_skill[0]}* из предложенных
                    📝 Отправьте номера через пробел (например: "1 3 4 7")
                    """),
                    parse_mode="Markdown"
                )
            else:
                await message.answer(
                f"🧩 *Навыки {textwrap.dedent(data['archetype'].lower())}* 🧩\n"
                f"Ваш персонаж начинает с такими умениями:\n"
                f"{textwrap.dedent('\n'.join(f'• *{skill}*' for skill in data_rouge_skill))}\n"
                f"Эти способности помогут вам в первых испытаниях!\n",
                parse_mode="Markdown"
                )

                finish_text = '\n'.join(data_rouge_skill)
                await state.update_data({'rogue_skills': finish_text})
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
            await message.answer("❌ Нужно вводить только цифры!\nПример: <b>3</b>", parse_mode="HTML")
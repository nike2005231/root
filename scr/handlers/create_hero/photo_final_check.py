from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from aiogram import F
from keyboards.keyboards import check_hero
from keyboards.keyboards import menu_keyboard

async def final_build(router, F, db):
    @router.message(CreateHero.getting_photo, F.photo)
    async def handle_character_photo(message: Message, state: FSMContext):
        try:
            photo_id = message.photo[-1].file_id
            await state.update_data({'character_photo': photo_id})

            data = await state.get_data()
            cm1_k, cm1_v = next(iter(data['communications_1'].items())) #Вроде и без генератора норм будет
            cm2_k, cm2_v = next(iter(data['communications_2'].items()))
            await message.answer_photo(
                photo=photo_id,
                caption="📸 *Портрет вашего персонажа*",
                parse_mode='Markdown'
            )
            character_info = (
                "🌟 *ВАШ ПЕРСОНАЖ СОЗДАН!* 🌟\n\n"
                f"🔮 *ОСНОВНАЯ ИНФОРМАЦИЯ*\n"
                f"🏷 Имя: {data['name']}\n"
                f"🎭 Архетип: {data['archetype']}\n"
                f"🧬 Вид: {data['species']}\n"
                f"🏠 Родной край: {data['home']}\n"
                f"💭 Причина странствий: {data['reason']}\n"
                f"📜 Оставленное позади: {data['left_behind']}\n\n"
                
                f"📊 *ХАРАКТЕРИСТИКИ*\n"
                f"💪 Мощь: {data['power']}\n"
                f"🏹 Ловкость: {data['agility']}\n"
                f"🍀 Удача: {data['luck']}\n"
                f"🦊 Хитрость: {data['cunning']}\n"
                f"✨ Харизма: {data['charm']}\n\n"
                
                f"🏛 *ФРАКЦИИ И ОТНОШЕНИЯ*\n"
                f"👑 Маркизат: *п* {data['marquisate_prestige_p']} | {data['marquisate_prestige_m']}\n"
                f"🦅 Крылатые Династии: *п* {data['winged_dynasties_prestige_p']} | {data['winged_dynasties_prestige_m']}\n"
                f"🌲 Лесной Альянс: *п* {data['forest_alliance_prestige_p']} | {data['forest_alliance_prestige_m']}\n"
                f"🍄 Лесной Народ: *п* {data['woodland_folk_prestige_p']} | {data['woodland_folk_prestige_m']}\n\n"
                
                f"💰 *РЕСУРСЫ И НАВЫКИ*\n"
                f"🪙 Деньги: {data['money']} серебра\n"
                f"🎯 Воровской навык: {data['rogue_skills']}\n"
                f"⚔ Боевое мастерство: {data['weapon_skill']}\n\n"
                
                f"💎 *ОСОБЕННОСТИ ВНЕШНОСТИ*\n"
                f"{data['features']}\n\n"
                
                f"🎭 *МАНЕРЫ ПОВЕДЕНИЯ*\n"
                f"{data['behavior']}\n\n"
                
                f"💡 *МОТИВАЦИЯ*\n"
                f"{data['motives']}\n\n"
                
                f"🧠 *ОСОБЕННОСТИ ЛИЧНОСТИ*\n"
                f"{data['personality']}\n\n"
                
                f"🎥 *ХОДЫ*\n"
                f"{data['moves']}"
                
                f"🤝 *СВЯЗИ С ПЕРСОНАЖАМИ*\n"
                f"*{cm1_k}*{cm1_v}\n"
                f"*{cm2_k}*{cm2_v}"
            )
            await message.answer(character_info, parse_mode="Markdown", reply_markup=check_hero())
            # await state.set_state(CreateHero.finall_check)
            
        except Exception as e:
            await message.answer(f"⚠️ Произошла ошибка при обработке фото: {str(e)}")

    @router.message(F.text == "❤️ Мне нравится мой выбор")
    async def save_character(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            chat_id = message.chat.id
            
            # Сохраняем основную информацию в таблицу info
            cm1_k, cm1_v = next(iter(data['communications_1'].items())) #Вроде и без генератора норм будет
            cm2_k, cm2_v = next(iter(data['communications_2'].items()))


            import json
            communications = [cm1_k, cm1_v, '\n', cm2_k, cm2_v]

            serialized = json.dumps(communications) #lite не воспринимает листы переводим лист тип в строку json и потом как будем получать читаем его loads выглядит так '[cm1_k, cm1_v, cm2_k, cm2_v]'

            db.insert_data(
                chat_id,
                data.get('archetype'),
                data.get('name'),
                data.get('species'),
                data.get('features'),
                data.get('behavior'),
                data.get('home'),
                data.get('reason'),
                data.get('left_behind'),
                serialized,
                data.get('character_photo'),
                data.get('motives'),
                False,  # is_active
                request='''
                INSERT INTO info (
                    chat_id, archetype, name, species, features, behavior,
                    home, reason, left_behind, communications, character_photo,
                    motives, is_active
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
            )

            db.insert_data(
                chat_id, 0, 0, 0, 
                request='''
                INSERT INTO character_status (chat_id, injury, depletion, costs)
                VALUES (?, ?, ?, ?)
                '''
            )

            db.insert_data(
                chat_id,
                data.get('money', 0),
                "", 
                request='''
                INSERT INTO inventory (chat_id, money, items)
                VALUES (?, ?, ?)
                '''
            )

            db.insert_data(
                chat_id,
                data.get('marquisate_prestige_p', 0),
                data.get('winged_dynasties_prestige_p', 0),
                data.get('forest_alliance_prestige_p', 0),
                data.get('woodland_folk_prestige_p', 0),
                data.get('marquisate_prestige_m', 0),
                data.get('winged_dynasties_prestige_m', 0),
                data.get('forest_alliance_prestige_m', 0),
                data.get('woodland_folk_prestige_m', 0),
                request='''
                INSERT INTO fractions (
                    chat_id, marquisate_prestige_p, winged_dynasties_prestige_p,
                    forest_alliance_prestige_p, woodland_folk_prestige_p, 
                    marquisate_prestige_m, winged_dynasties_prestige_m,
                    forest_alliance_prestige_m, woodland_folk_prestige_m
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
            )

            db.insert_data(
                chat_id,
                data.get('power', 0),
                data.get('agility', 0),
                data.get('luck', 0),
                data.get('cunning', 0),
                data.get('charm', 0),
                request='''
                INSERT INTO stats (
                    chat_id, power, agility, luck, cunning, charm
                ) VALUES (?, ?, ?, ?, ?, ?)
                '''
            )

            db.insert_data(
                chat_id,
                data.get('rogue_skills', ''),
                data.get('weapon_skill', ''),
                data.get('moves', ''),
                request='''
                INSERT INTO skills (chat_id, rogue_skills, weapon_skill, moves)
                VALUES (?, ?, ?, ?)
                '''
            )

            await message.answer("✅ Персонаж успешно сохранён!", reply_markup=menu_keyboard())
            await state.clear()

        except Exception as e:
            await message.answer(f"❌ Ошибка при сохранении персонажа: {str(e)}")
            print(f"Error saving character: {e}")
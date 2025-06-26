from aiogram.types import Message
import random
from keyboards.keyboards import tiz_keyboard, check_keyboard, menu_keyboard, inventory_keyboard, fractions_keyboard, skills_keyboard
from handlers.handlers_changes_stats.tiz_handlers import init_tiz
from handlers.handlers_changes_stats.fractions_handlers import init_fractions
from handlers.handlers_changes_stats.inventory import init_inventory
from handlers.handlers_changes_stats.skills import init_skills

async def init_hero_changes_stats(router, F, db, message):
    @router.message(F.text == "💉 Ячейки ТИЗ")
    async def show_injuries(message: Message):
        data = db.get_data(message.chat.id, request='SELECT injury, depletion, costs, max_injury, max_depletion, max_costs FROM character_status WHERE chat_id = ?')
        if data:
            injury, depletion, costs, max_i, max_d, max_c = data[0]

            if injury >= max_i:
                injury_roast = random.choice(["Ты на последнем издыхании!", "Тебе нужен лекарь... СРОЧНО!", "Кажется, ты разваливаешься."])
            elif injury > max_i / 2:
                injury_roast = random.choice(["Потрепанный, но ещё стоишь.", "Немного побитый жизнью.", "Боевые шрамы или просто неуклюжий?"])
            else:
                injury_roast = random.choice(["Ещё цел!", "Неплохо, не развалился пока.", "Ты ещё даже не поцарапан!"])

            if depletion >= max_d:
                depletion_roast = random.choice(["Ты выглядишь как булыга после недельного запоя.", "Валишься с ног?", "Тебя бы сейчас только поспать."])
            elif depletion > max_d / 2:
                depletion_roast = random.choice(["Устал как собака?", "Батарейка садится.", "Немного вымотан."])
            else:
                depletion_roast = random.choice(["Бодр как огурчик!", "Полон сил!", "Энергии хоть отбавляй."])

            if costs >= max_c:
                costs_roast = random.choice(["Бля, ты банкрот.", "Деньги? Что это?", "Ветер свистит в карманах."])
            elif costs > max_c / 2:
                costs_roast = random.choice(["Почти на мели.", "Тяжеловато с финансами.", "Живёшь на дошираке?"])
            else:
                costs_roast = random.choice(["Денег куры не клюют!", "На коне!", "Можно и потратиться."])

            response = (
                "🔴 *Состояние персонажа:*\n\n"
                f"💢 *Травмы:* {injury}/{max_i} – _{injury_roast}_\n"
                f"🥵 *Истощение:* {depletion}/{max_d} – _{depletion_roast}_\n"
                f"💸 *Затраты:* {costs}/{max_c} – _{costs_roast}_"
            )
            await init_tiz(router=router, F=F, db=db, message=message)
            await message.answer(response, parse_mode="Markdown", reply_markup=tiz_keyboard())
            

    @router.message(F.text == "📚 Навыки")
    async def show_skills(message: Message):
        data = db.get_data(message.chat.id, request='SELECT rogue_skills, weapon_skill, moves FROM skills WHERE chat_id = ?')
        if data:
            rogue, weapon, moves = data[0]

            response = (
                "📚 *Навыки персонажа:*\n\n"
                f"🦹 *Воровские навыки:*\n{rogue or 'Не указано'}\n\n"
                f"⚔️ *Боевое мастерство:*\n{weapon or 'Не указано'}\n\n"
                f"🏃 *Ходы персонажа:*\n{moves or 'Не указано'}"
            )
            await message.answer(response, parse_mode="Markdown")

    @router.message(F.text == "📜 История")
    async def show_history(message: Message):
        data = db.get_data(message.chat.id, request='SELECT name, species, features, behavior, home, reason, left_behind, communications, motives FROM info WHERE chat_id = ?')
        if data:
            (name, species, features, behavior, home, reason, left, comm, motives) = data[0]

            response = (
                "📖 *История персонажа:*\n\n"
                f"📛 *Имя:* {name or 'Не указано'}\n"
                f"🧬 *Вид:* {species or 'Не указано'}\n"
                f"🎭 *Особенности:* {features or 'Не указано'}\n"
                f"💃 *Манеры:* {behavior or 'Не указано'}\n\n"
                f"🏠 *Родной край:*\n{home or 'Не указано'}\n\n"
                f"❓ *Причина странствий:*\n{reason or 'Не указано'}\n\n"
                f"👣 *Оставленное позади:*\n{left or 'Не указано'}\n\n"
                f"📞 *Связи:*\n{comm or 'Не указано'}\n\n"
                f"💫 *Мотивация:*\n*Развитие происходит*\n{motives or 'Не указано'}"
            )
            await message.answer(response, parse_mode="Markdown")

    @router.message(F.text == "✨ Скиллы")
    async def show_stats(message: Message):
        data = db.get_data(message.chat.id, request='SELECT power, agility, luck, cunning, charm FROM stats WHERE chat_id = ?')
        if data:
            (power, agi, luck, cunning, charm) = data[0]

            power_roast = random.choice(["Ты хотя бы банку открыть можешь?", "Дрыщ."]) if power <= 0 else (random.choice(["Ну ладно, качок.", "Силач!"]) if power >= 2 else random.choice(["Среднячок.", "Не дрыщ и не качок."]))
            agi_roast = random.choice(["Не пизданись", "Тормоз."]) if agi <= 0 else (random.choice(["Саске вернись в Коноху.", "Шустрый!"]) if agi >= 2 else random.choice(["Двигаешься.", "Неуклюжий, но не совсем."]))
            luck_roast = random.choice(["Тебе бы в казино не ходить.", "Неудачник."]) if luck <= 0 else (random.choice(["Везучий уёбок.", "Сорвал куш!"]) if luck >= 2 else random.choice(["Так себе удача.", "Невезение преследует."]))
            cunning_roast = random.choice(["Пфф* сам себя не наеби ", "Тупень."]) if cunning <= 0 else (random.choice(["А ты умеешь пиздеть.", "Хитрюга!"]) if cunning >= 2 else random.choice(["Что-то мутишь.", "Не семи пядей во лбу."]))
            charm_roast = random.choice(["Тебя люди терпят только из вежливости.", "Страшила."]) if charm <= 0 else (random.choice(["Харизматичный мудак.", "Душа компании!"]) if charm >= 2 else random.choice(["Не отталкиваешь, и то хорошо.", "Приятный в общении... иногда."]))

            response = (
                "✨ *Характеристики персонажа:*\n\n"
                f"💪 *Мощь:* {power} – _{power_roast}_\n"
                f"🏹 *Ловкость:* {agi} – _{agi_roast}_\n"
                f"🍀 *Удача:* {luck} – _{luck_roast}_\n"
                f"🦊 *Хитрость:* {cunning} – _{cunning_roast}_\n"
                f"🌟 *Харизма:* {charm} – _{charm_roast}_"
            )
            await init_skills(router=router, F=F, db=db, message=message)
            await message.answer(response, parse_mode="Markdown", reply_markup=skills_keyboard())

    @router.message(F.text == "🏛 Отношения фракций")
    async def show_fractions(message: Message):
        data = db.get_data(message.chat.id, request='''
            SELECT
                marquisate_rep, winged_dynasties_rep,
                forest_alliance_rep, woodland_folk_rep,
                marquisate_prestige_p, winged_dynasties_prestige_p,
                forest_alliance_prestige_p, woodland_folk_prestige_p,
                marquisate_prestige_m, winged_dynasties_prestige_m,
                forest_alliance_prestige_m, woodland_folk_prestige_m
            FROM fractions WHERE chat_id = ?
        ''')
        if data:
            (m_rep, wd_rep, fa_rep, wf_rep, m_pr, wd_pr, fa_pr, wf_pr, m_pr_m, wd_pr_m, fa_pr_m, wf_pr_m) = data[0]

            response = (
                "🏰 *Фракции и ваши отношения* 🏰\n\n"
                
                f"👑 *Маркизат*\n"
                f"├ Репутация: {'+' if m_rep > 0 else ''}{m_rep}\n"
                f"├ Положительный престиж: {m_pr}\n"
                f"└ Отрицательный престиж: {m_pr_m}\n\n"
                
                f"🦅 *Крылатые Династии*\n"
                f"├ Репутация: {'+' if wd_rep > 0 else ''}{wd_rep}\n"
                f"├ Положительный престиж: {wd_pr}\n"
                f"└ Отрицательный престиж: {wd_pr_m}\n\n"
                
                f"🌳 *Лесной Альянс*\n"
                f"├ Репутация: {'+' if fa_rep > 0 else ''}{fa_rep}\n"
                f"├ Положительный престиж: {fa_pr}\n"
                f"└ Отрицательный престиж: {fa_pr_m}\n\n"
                
                f"🍄 *Лесной Народ*\n"
                f"├ Репутация: {'+' if wf_rep > 0 else ''}{wf_rep}\n"
                f"├ Положительный престиж: {wf_pr}\n"
                f"└ Отрицательный престиж: {wf_pr_m}\n\n"
                
                "\nℹ️ *п/м* - положительный/отрицательный престиж"
            )

            await init_fractions(router=router, F=F, db=db, message=message)
            await message.answer(response, parse_mode="Markdown", reply_markup=fractions_keyboard())

    @router.message(F.text == "🎒 Инвентарь")
    async def show_inventory(message: Message):
        data = db.get_data(message.chat.id, request='SELECT money, items FROM inventory WHERE chat_id = ?')
        if data:
            money, items = data[0]

            response = (
                "🎒 *Инвентарь:*\n\n"
                f"💰 *Деньги:* {money or 0} шмекелей\n\n"
                f"📦 *Предметы:*\n{items or 'Инвентарь пуст'}"
            )
            await init_inventory(router=router, F=F, db=db, message=message)
            await message.answer(response, parse_mode="Markdown", reply_markup=inventory_keyboard())
            

    #Будет тут я хуй знает куда его еще пихнуть
    @router.message(F.text == "💔 Удалить персонажа")
    async def clear_bd(message: Message):

        await message.answer("Вы уверены что хотите удалить персонажа?", reply_markup=check_keyboard())

        @router.message(F.text == "✅ Да")
        async def back_menu(message: Message): 
            try:
                chat_id = message.chat.id
                
                tables = [
                    'info',
                    'character_status',
                    'inventory',
                    'fractions',
                    'stats',
                    'skills'
                ]
                
                for table in tables:
                    db.insert_data(chat_id, request=f"DELETE FROM {table} WHERE chat_id = ?")

                await message.answer("💀 Персонаж полностью удален. Все данные очищены.", reply_markup=menu_keyboard())
            
            except Exception as e:
                await message.answer(f"⚠️ Произошла ошибка при удалении персонажа: {str(e)}")
        
        @router.message(F.text == "❌ Нет")
        async def back_menu(message: Message):
            await message.answer("🏠 Вы в меню", reply_markup=menu_keyboard())
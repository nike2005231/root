from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.keyboards import menu_keyboard, profile_keyboard, master_keyboard, game_keyboard
import asyncio
import textwrap

async def init_dice(router, F, db):
    @router.message(F.text == "🎲 Бросить кубики")
    async def dice_roll(message: Message):
        try:
            users = db.get_data(request="SELECT id, name_user FROM users")
            if not users:
                await message.answer("❌ В базе данных нет пользователей")
                return

            temp_msg = await message.answer("🎲 Подбрасываем кубики...")
            
            dice1 = await message.answer_dice(emoji="🎲")
            dice2 = await message.answer_dice(emoji="🎲")
            await asyncio.sleep(3)
            
            # Получаем результаты
            roll1 = dice1.dice.value
            roll2 = dice2.dice.value
            total = roll1 + roll2

            if total <= 6:
                result = "💀 Критический провал (1-6)"
                details = "Полный провал - возможны негативные последствия (не забудьте просуммировать с характеристиками)"
            elif total <= 9:
                result = "🌿 Малый успех (7-9)"
                details = "Частичное достижение цели с осложнениями (не забудьте просуммировать с характеристиками)"
            else:
                result = "✨ Блестящий успех (10-12)"
                details = "Полное достижение цели с возможным бонусом (не забудьте просуммировать с характеристиками)"

            result_message = textwrap.dedent(f"""
            🎲 *Результаты броска от {message.from_user.first_name}* 🎲
            
            🔥 Общая сумма: *{total}*
            
            🎯 *Результат:* {result}
            📝 *Эффект:* {details}
            
            {'⚠️ *Особый эффект:* Критическая неудача!' if total <= 3 else 
             '🌟 *Особый эффект:* Идеальный бросок!' if total == 12 else ''}
            """)
            
            success_count = 0
            failed_users = []
            
            for user_id, name_user in users:
                try:
                    await message.bot.send_message(
                        chat_id=user_id,
                        text=result_message,
                        parse_mode="Markdown"
                    )
                    success_count += 1
                except Exception as e:
                    failed_users.append(str(user_id))
                    continue

        except Exception as e:
            await message.answer(f"⚠️ Произошла ошибка: {str(e)}")
            raise e

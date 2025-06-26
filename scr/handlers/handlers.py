from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.keyboards import menu_keyboard, profile_keyboard, master_keyboard, game_keyboard
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from handlers.create_hero.handlers_create_hero import init_handlers_create_hero
from handlers.show_hero import show_hero
from handlers.handlers_changes import init_hero_changes_stats

async def init_heanlers(router, F, db):
    @router.message(F.text.in_(["🎭 Мой персонаж", "🔄 Пересоздать"]))
    async def show_profile(message: Message, state: FSMContext):
        await state.clear()
        try:
            result = db.get_data(message.chat.id, request='SELECT 1 FROM info WHERE chat_id = ? LIMIT 1')
            has_character = bool(result)  # True, если есть записи
            
            if has_character:
                await show_hero(router=router, F=F, db=db, message=message)
                await init_hero_changes_stats(router=router, F=F, db=db, message=message)
            else:
                await state.set_state(CreateHero.choosing_archetype)
                await init_handlers_create_hero(router=router, F=F, db=db)
                await message.answer(
                    "🛡️ *Создание нового персонажа* 🎭\n\n"
                    "У вас еще нет своего героя в этом мире. Давайте создадим его!\n"
                    "Первым шагом выберите *архетип* — основу вашего персонажа:\n\n"
                    "• 🎒 *Авантюрист* — стремится к приключениям и новым связям\n"
                    "• ⚖️ *Судья* — стоит за справедливость или карает\n"
                    "• 🪓 *Налётчик* — действует быстро и решительно (через е)\n"
                    "• 🐾 *Следопыт* — действует один, задаёт неудобные вопросы\n"
                    "• 🗡️ *Ронин* — хладнокровный мститель или стойкий воин\n"
                    "• 🔥 *Поджигатель* — разрушает порядок и манипулирует\n"
                    "• 🎭 *Вор* — хитёр, изворотлив и полагается на удачу\n"
                    "• 🔧 *Ремесленник* — творит и созидает\n"
                    "• 🌍 *Скиталец* — ищет новое и исследует неизведанное\n"
                    "• 🤵 *Сутинер* — тоже ищет новое и исследует неизведанное\n\n"
                    "Введите название архетипа (ПРИМЕР - Авантюрист):",
                    reply_markup=ReplyKeyboardRemove(),
                    parse_mode="markdown"
                )
                
        except Exception as e:
            print(f"Ошибка при проверке персонажа: {e}")
            await message.answer("⚠️ Произошла ошибка при проверке персонажа. Попробуйте позже.")


    @router.message(F.text == "🎲 Мастер")
    async def show_master(message: Message):
        if message.chat.id in (633986877, 6491217944, 5594910070):
            await message.answer('🔮 Привествую мастер-создатель\n\n🧞‍♂️ Что прикажите? Георгий.', reply_markup=master_keyboard())
        else:
            await message.answer('🧙‍♂️ Вы не Гоша-сэнсей', reply_markup=None)

    @router.message(F.text == "🎮 Игра")
    async def show_master(message: Message):
        await message.answer('Мастер', reply_markup=game_keyboard())

    @router.message(F.text == "🏠 Меню")
    async def back_menu(message: Message):
        await message.answer("🏠 Вы в меню", reply_markup=menu_keyboard())
    
    
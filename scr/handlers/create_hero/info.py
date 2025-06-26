from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.motives import motives_choice
import textwrap

async def global_informations_hero(router):
    @router.message(CreateHero.choosing_archetype)
    async def archetype_chosen(message: Message, state: FSMContext):
        if message.text.lower() in ("авантюрист", "судья", "налетчик", "следопыт", "ронин", "поджигатель", "вор", "ремесленник", "скиталец"):
            await state.update_data(archetype=message.text)
            await state.set_state(CreateHero.filling_name)
            await message.answer(
                "🎉 *Отличный выбор архетипа!* 🎉\n\n"
                f"Вы выбрали путь *{message.text}*! 🌟 Теперь ваш герой готов получить имя.\n\n"
                "✍️ Введите запоминающееся имя для своего персонажа: 🦸‍♂️",
                reply_markup=ReplyKeyboardRemove(),
                parse_mode="markdown"
            )
        elif message.text.lower() == 'сутинер':
            await message.answer(
                "🎭 <b>Сутинер?</b> 🎭\n\n"
                "Нихуя ты шалунишка! 😈\n"
                f"А теперь-ка выбери нормальный архетип, {message.chat.first_name}. 💅\n\n", parse_mode='html'
            )
            return
        else:
            await message.answer('✍️ Введите архетип из перечисленных\n\n'                
            "• 🎒 *Авантюрист* — стремится к приключениям и новым связям\n"
            "• ⚖️ *Судья* — стоит за справедливость или карает\n"
            "• 🪓 *Налётчик* — действует быстро и решительно (через е)\n"
            "• 🐾 *Следопыт* — действует один, задаёт неудобные вопросы\n"
            "• 🗡️ *Ронин* — хладнокровный мститель или стойкий воин\n"
            "• 🔥 *Поджигатель* — разрушает порядок и манипулирует\n"
            "• 🎭 *Вор* — хитёр, изворотлив и полагается на удачу\n"
            "• 🔧 *Ремесленник* — творит и созидает\n"
            "• 🌍 *Скиталец* — ищет новое и исследует неизведанное\n"
            "• 🤵 *Сутинер* — тоже ищет новое и исследует неизведанное\n\n",
            parse_mode='Markdown'
            )

    @router.message(CreateHero.filling_name)
    async def name_filled(message: Message, state: FSMContext):
        await state.update_data(name=message.text.lower())
        await state.set_state(CreateHero.choosing_species)
        await message.answer(
            "🌿 *Прекрасное имя!* 🌿\n\n"
            f"Теперь <b>{message.text}</b> обретает форму...\n\n"
            "🦉 <i>Выберите вид своего персонажа</i>:\n"
            "• Можно выбрать из классических: лиса, кролик, мышь\n"
            "• Или придумать что-то уникальное!\n\n"
            "✨ <b>Просто напишите ваш вариант:</b>",
            parse_mode="HTML"
        )

    @router.message(CreateHero.choosing_species)
    async def species_chosen(message: Message, state: FSMContext):
        await state.update_data(species=message.text)
        await state.set_state(CreateHero.choosing_distinctive_features)
        await message.answer(
            "🎭 *Внешность персонажа* 🎭\n\n"
            "Опишите <b>3 отличительные черты</b> через запятую:\n"
            "Пример: <i>«мужской, яркий, с медальоном»</i>\n\n"
            "Пусть это будет что-то запоминающееся!",
            parse_mode="HTML"
        )

    @router.message(CreateHero.choosing_distinctive_features)
    async def features_chosen(message: Message, state: FSMContext):
        await state.update_data(features=message.text)
        await state.set_state(CreateHero.choosing_behavior)
        await message.answer(
            "🌀 *Манера поведения* 🌀\n\n"
            "Какое у вашего персонажа <b>основное качество</b>?\n"
            "Например: <i>«дипломатичный, но с железной волей»</i>\n\n"
            "Опишите в свободной форме:",
            parse_mode="HTML"
        )

    @router.message(CreateHero.choosing_behavior)
    async def behavior_chosen(message: Message, state: FSMContext):
        await state.update_data(behavior=message.text)
        await state.set_state(CreateHero.choosing_home)
        await message.answer(
            "🏡 *Где ваш дом?* 🏡\n\n"
            "Это может быть:\n"
            "• Затерянная поляна в Лесу\n"
            "• Далёкие земли за горизонтом\n"
            "• Или что-то совсем необычное...\n\n"
            "📜 Напишите вашу историю:",
            parse_mode="HTML"
        )

    @router.message(CreateHero.choosing_home)
    async def home_chosen(message: Message, state: FSMContext):
        await state.update_data(home=message.text)
        await state.set_state(CreateHero.choosing_reason)
        await message.answer(
            "🌪️ *Почему вы стали бродягой?* 🌪️\n\n"
            "Опишите <b>поворотный момент</b>:\n"
            "• Быть может, вы бежите от прошлого?\n"
            "• Или ищете что-то важное?\n\n"
            "💬 Расскажите в одном-двух предложениях:",
            parse_mode="HTML"
        )

    @router.message(CreateHero.choosing_reason)
    async def reason_chosen(message: Message, state: FSMContext):
        await state.update_data(reason=message.text)
        await state.set_state(CreateHero.choosing_left_behind)
        await message.answer(
            "💔 *Кого вы оставили?* 💔\n\n"
            "Опишите <b>самую болезненную потерю</b>:\n"
            "• Любовь всей жизни\n"
            "• Ученика, который предал\n"
            "• Или может, целую семью...\n\n"
            "🖋️ Напишите что-то личное:",
            parse_mode="HTML"
        )
    
    @router.message(CreateHero.choosing_left_behind)
    async def left_behind_chosen(message: Message, state: FSMContext):
        await state.update_data(left_behind=message.text)
        await state.set_state(CreateHero.choosing_motives)
        data = await state.get_data()
        data_choice_motive = motives_choice(archetype=data['archetype'])
        
        await message.answer(
            textwrap.dedent(f"""
            🔥 *Выбери два мотива* 🔥
            
            Введи две цифры через пробел (например: 1 3)
            
            💡 *Развите происходит*:

            1️⃣ {data_choice_motive[1]}
            2️⃣ {data_choice_motive[2]}
            3️⃣ {data_choice_motive[3]}
            4️⃣ {data_choice_motive[4]}
            """),
            parse_mode="Markdown"
        )
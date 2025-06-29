from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.communications import communications_choice
from keyboards.keyboards import communications_keyboard
from aiogram import F
import textwrap

async def communications_hero(router):
    async def final(message: Message, state: FSMContext):
        await state.set_state(CreateHero.getting_photo)

        await message.answer(
            textwrap.dedent(f"""
                🌟 *ФИНАЛЬНЫЙ ШАГ: ФОТО ПЕРСОНАЖА* 🌟
                
                Пожалуйста, отправьте фото вашего персонажа:
                
                📸 Это будет его визуальным представлением
                🖼️ Можно прислать готовое изображение

                ⚠️ Убедитесь, что фото хорошо передает характер вашего героя!
            """),
            reply_markup=ReplyKeyboardRemove(),
            parse_mode="Markdown"
        )


    @router.message(F.text == "👥 Друг")
    async def chosing_friend(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя друга",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_friend_2)
        else:
            await state.set_state(CreateHero.choosing_communications_friend_1)

    @router.message(CreateHero.choosing_communications_friend_1)
    async def add_friend(message: Message, state: FSMContext):
        await state.update_data({'communications_1':{'друг':f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_friend_2)
    async def add_friend(message: Message, state: FSMContext):
        await state.update_data({'communications_2':{'друг':f' - {message.text.lower()}'}})
        await final(message=message, state=state)
    
    
    @router.message(F.text == "🛡️ Защитник")
    async def choosing_guardian(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя защитника",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_guardian_2)
        else:
            await state.set_state(CreateHero.choosing_communications_guardian_1)

    @router.message(CreateHero.choosing_communications_guardian_1)
    async def add_guardian(message: Message, state: FSMContext):
        await state.update_data({'communications_1': {'защитник': f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_guardian_2)
    async def add_guardian_2(message: Message, state: FSMContext):
        await state.update_data({'communications_2': {'защитник': f' - {message.text.lower()}'}})
        await final(message=message, state=state)


    @router.message(F.text == "❤️ Партнёр")
    async def choosing_partner(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя партнёра",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_partner_2)
        else:
            await state.set_state(CreateHero.choosing_communications_partner_1)

    @router.message(CreateHero.choosing_communications_partner_1)
    async def add_partner(message: Message, state: FSMContext):
        await state.update_data({'communications_1': {'партнёр': f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_partner_2)
    async def add_partner_2(message: Message, state: FSMContext):
        await state.update_data({'communications_2': {'партнёр': f' - {message.text.lower()}'}})
        await final(message=message, state=state)


    @router.message(F.text == "💼 Профессионал")
    async def choosing_professional(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя профессионала",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_pro_2)
        else:
            await state.set_state(CreateHero.choosing_communications_pro_1)

    @router.message(CreateHero.choosing_communications_pro_1)
    async def add_professional(message: Message, state: FSMContext):
        await state.update_data({'communications_1': {'профессионал': f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_pro_2)
    async def add_professional_2(message: Message, state: FSMContext):
        await state.update_data({'communications_2': {'профессионал': f' - {message.text.lower()}'}})
        await final(message=message, state=state)


    @router.message(F.text == "🏠 Семья")
    async def choosing_family(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя члена семьи",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_family_2)
        else:
            await state.set_state(CreateHero.choosing_communications_family_1)

    @router.message(CreateHero.choosing_communications_family_1)
    async def add_family(message: Message, state: FSMContext):
        await state.update_data({'communications_1': {'семья': f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_family_2)
    async def add_family_2(message: Message, state: FSMContext):
        await state.update_data({'communications_2': {'семья': f' - {message.text.lower()}'}})
        await final(message=message, state=state)


    @router.message(F.text == "👀 Наблюдатель")
    async def choosing_watcher(message: Message, state: FSMContext):
        await message.answer(
            "Теперь введи имя наблюдателя",
            reply_markup=communications_keyboard()
        )
        data = await state.get_data()
        if data.get('communications_1'):
            await state.set_state(CreateHero.choosing_communications_watcher_2)
        else:
            await state.set_state(CreateHero.choosing_communications_watcher_1)

    @router.message(CreateHero.choosing_communications_watcher_1)
    async def add_watcher(message: Message, state: FSMContext):
        await state.update_data({'communications_1': {'наблюдатель': f' - {message.text.lower()}'}})
        await message.answer(
            "Первое имя получено, теперь выбери вторую связь на клавиатуре",
            reply_markup=communications_keyboard()
        )
        await state.set_state(CreateHero.choosing_communications)

    @router.message(CreateHero.choosing_communications_watcher_2)
    async def add_watcher_2(message: Message, state: FSMContext):
        await state.update_data({'communications_2': {'наблюдатель': f' - {message.text.lower()}'}})
        await final(message=message, state=state)
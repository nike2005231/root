from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from states.state_change_hero import CommunicateState, DeleteCommunicate
from keyboards.keyboards import profile_keyboard, change_communications_keyboard, history_keyboard, choice_communications_keyboard
from handlers.handlers_changes_stats.send_mes_all import send_message_all_users
import json

async def init_history(router, F, db, message):
    @router.message(F.text == "🧾 Справка")
    async def reference(message: Message, state: FSMContext):
        connections_info = (
            "*Друг*:\n"
            "Если ПИ помогает тому, с кем связан, то управляющий им игрок может отметить 2 истощения, "
            "чтобы прибавить к броскам +2, вместо того, чтобы отметить 1 истощение и прибавить +1.\n\n"
            
            "*Профессионал*:\n"
            "Если ПИ делится с тем, с кем связан, информацией после анализа напряжённой ситуации, оба получают +1 "
            "к результатам бросков действий на основе ответов. Если ПИ помогает тому, с кем связан, выполнить "
            "плутовской приём, то управляющий игрок отмечает ему одно истощение, но получает выбор во время помощи, "
            "как если бы отметил два истощения.\n\n"
            
            "*Семья*:\n"
            "Если ПИ помогает реализовать характер тому, с кем он связан, оба могут очистить шкалы истощения.\n\n"
            
            "*Партнер*:\n"
            "Выбрав эту связь, один игрок и другой, с ПИ которого связан ПИ первого игрока, должны отметить 2 ячейки "
            "престижа у фракции, которой помог первый ПИ, и 2 ячейки дурной славы у фракции, которой он навредил. "
            "Если обоих ПИ заметят вместе, и они должны будут при этом получить престиж или дурную славу у этих "
            "фракций, то полученные числа удвоятся.\n\n"
            
            "*Наблюдатель*:\n"
            "Если ПИ пытается понять того, с кем связан, то игрок, управляющий этим ПИ, получает 1 очко запаса, "
            "даже при провале. Когда этот ПИ уговаривает того, с кем связан, то может позволить ему очистить 2 "
            "истощения вместо 1.\n\n"
            
            "*Защитник*:\n"
            "Когда защищаемый находится в пределах досягаемости защитника, игрок, управляющий защитником, может "
            "отметить истощение защитнику, чтобы тот принял на себя удар, предназначенный защищаемому. После этого "
            "до конца сцены защитник получает +1 к результатам бросков оружейных ходов."
        )
        await message.answer(connections_info, parse_mode="Markdown", reply_markup=history_keyboard())

    @router.message(F.text == "🌐 Связи")
    async def change_communicate(message: Message, state: FSMContext):
        await message.answer('Выбери действие:', parse_mode="Markdown", reply_markup=change_communications_keyboard())

    @router.message(F.text == "➕ Добавить связь")
    async def add_communicate(message: Message, state: FSMContext):
        MAXIMUM_CONNECTIONS = 6
        data = db.get_data(message.chat.id, request='SELECT role, name FROM communications WHERE chat_id = ?')      
        
        if len(data) >= MAXIMUM_CONNECTIONS:
            await message.answer(
                '⚠️ *Достигнут лимит связей*\n\n'
                'Вы уже добавили *максимальное количество* (6) – больше нельзя.\n'
                'Если хотите добавить новую связь, сначала удалите одну из старых.',  
                parse_mode="Markdown",  
                reply_markup=history_keyboard()  
            )
        else:
            await message.answer(
                '*Выберите новую связь*',
                parse_mode="Markdown",  
                reply_markup=choice_communications_keyboard()  
            )

    async def record_communicate(role: str, name: str):
        try:
            db.insert_data(message.chat.id, role, name, request='insert into communications (chat_id, role, name) values (?, ?, ?)')
        except Exception as ex:
            print(f'Ошибка - {ex}')
            
    async def add_communication_handler(message: Message, state: FSMContext, state_class):
        await message.answer(
            '*Теперь введи имя:*',
            parse_mode="Markdown",  
            reply_markup=ReplyKeyboardRemove()  
        )
        await state.set_state(state_class)
    
    generate_handlers = [
        ["👥 Друга", "💼 Профессионала", "🏠 Семью", "❤️ Партнёра", "👀 Наблюдателя", "🛡️ Защитника"], 
        [CommunicateState.add_friend, CommunicateState.add_professional, CommunicateState.add_family, CommunicateState.add_partner, CommunicateState.add_observer, CommunicateState.add_protector],
        ['друг', 'профессионал', 'семья', 'партнер', 'наблюдатель', 'защитник']
    ]

    def create_handler(name, name_state, rename_record):
        @router.message(F.text == name)
        async def add_communicate(message: Message, state: FSMContext):
            await add_communication_handler(message, state, name_state)

        @router.message(name_state)
        async def add_guardian(message: Message, state: FSMContext):
            name = message.text
            existing_names = {row[0] for row in db.get_data(message.chat.id, request='SELECT name FROM communications WHERE chat_id = ?')}
            if name in existing_names:
                await message.answer('Одно имя, не может быть в двух связях!!!')
                return
            text = (
                f"Пользователь: <code>{message.chat.first_name}</code>\n"
                f"Добавил новую связь:\n"
                f"<code>{rename_record} - {name}</code>\n"
            )
            await send_message_all_users(db=db, message=message, text=text, markup=history_keyboard())

            await record_communicate(rename_record, name)
            await state.clear()
    
    for name, name_state, rename_record in zip(*generate_handlers):
        create_handler(name, name_state, rename_record)

    @router.message(F.text == "➖ Убрать связь")
    async def delete_communicate(message: Message, state: FSMContext):
        data = db.get_data(message.chat.id, request='SELECT * FROM communications WHERE chat_id = ?')
        if not data:
            await message.answer('*Связей нет*', parse_mode="Markdown") 
        else:
            async def generated_keyboards_communications(data: list):
                if data:
                    keyboard = [[KeyboardButton(text=f'{item[2]} - {item[3]}')] for item in data]
                    await message.answer('Выберите связь которую хотите удалить', reply_markup=ReplyKeyboardMarkup(keyboard = keyboard, resize_keyboard=True))
                    await state.set_state(DeleteCommunicate.delete)
            await generated_keyboards_communications(data=data)

    @router.message(DeleteCommunicate.delete, F.text.regexp(r'^(.+?) - (.+)$'))
    async def handle_delete_in_state(message: Message, state: FSMContext):
        role, name = message.text.split(' - ') # СВЯЗЬ - ИМЯ
        
        db.insert_data(message.chat.id, role, name, request='delete from communications where chat_id = ? and role = ? and name = ?')
        text = (
            f"Пользователь: <code>{message.chat.first_name}</code>\n"
            f"Стер связь:\n"
            f"<code>{role} - {name}</code>\n"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=history_keyboard())
        await state.clear()
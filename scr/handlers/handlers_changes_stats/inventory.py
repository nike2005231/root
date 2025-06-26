from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from states.state_change_hero import InventoryStats
from handlers.handlers_changes_stats.send_mes_all import send_message_all_users
from keyboards.keyboards import profile_keyboard

async def init_inventory(router, F, db, message):
    @router.message(F.text == "💰 Изменить шмекели")
    async def capacity(message: Message, state: FSMContext):
        await message.answer(
            "💰 Введи новое количество шмекелей:",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(InventoryStats.money)

    @router.message(F.text == "➕ Добавить предмет")
    async def add_item_start(message: Message, state: FSMContext):
        await message.answer(
            "📦 Введите название предмета для добавления:",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(InventoryStats.add_item)

    @router.message(F.text == "➖ Удалить предмет")
    async def remove_item_start(message: Message, state: FSMContext):
        # Получаем текущий список предметов
        items_data = db.get_data(message.chat.id, request='select items from inventory where chat_id == ?')
        if not items_data or not items_data[0][0]:
            await message.answer("❌ Ваш инвентарь пуст!")
            return
        
        items = items_data[0][0].split('|') 
    
        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=item)] for item in items],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        
        await message.answer(
            "❌ Выберите предмет для удаления:",
            reply_markup=keyboard
        )
        await state.set_state(InventoryStats.remove_item)






    @router.message(InventoryStats.money)
    async def money_get(message: Message, state: FSMContext):
        try:
            new_money_value = int(message.text)
        except ValueError:
            await message.reply("❗️ Введите, пожалуйста, только число!")
            return

        current_value = db.get_data(message.chat.id, request='select money from inventory where chat_id == ?')[0][0]
        db.insert_data(
            new_money_value,
            message.chat.id,
            request='UPDATE inventory SET money = ? WHERE chat_id = ?'
        )
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"💰 <b>Шмекели зашевелились!</b> 💸\n\n"
            f"👤 Вкладчик: <code>{name_user}</code>\n"
            f"📊 Изменение баланса:\n"
            f"• Было: <code>{current_value}</code> шмекелей\n"
            f"• Стало: <code>{new_money_value}</code> шмекелей\n\n"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(InventoryStats.add_item)
    async def add_item_process(message: Message, state: FSMContext):
        new_item = message.text.strip()
        
        # Получаем текущие предметы
        items_data = db.get_data(message.chat.id, request='select items from inventory where chat_id == ?')
        current_items = items_data[0][0].split('|') if items_data and items_data[0][0] else []
        
        # Добавляем новый предмет
        if new_item in current_items:
            await message.reply("❌ Этот предмет уже есть в инвентаре!\nЕсли хотите добавить копию пишите название_предмета + его_номер")
            return
            
        current_items.append(new_item)
        updated_items = '|'.join(current_items)
        
        # Обновляем базу данных
        db.insert_data(
            updated_items,
            message.chat.id,
            request='UPDATE inventory SET items = ? WHERE chat_id = ?'
        )
        
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"🎉 <b>Инвентарь обновлен!</b> 🛍️\n\n"
            f"👤 Вкладчик: <code>{name_user}</code>\n"
            f"🆕 Добавлен предмет: <code>{new_item}</code>\n"
            f"📦 Теперь в инвентаре: <code>{len(current_items)}</code> предметов\n\n"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(InventoryStats.remove_item)
    async def remove_item_process(message: Message, state: FSMContext):
        item_to_remove = message.text.strip()
        
        # Получаем текущие предметы
        items_data = db.get_data(message.chat.id, request='select items from inventory where chat_id == ?')
        if not items_data or not items_data[0][0]:
            await message.reply("❌ Ваш инвентарь пуст!")
            await state.clear()
            return
            
        current_items = items_data[0][0].split('|')
        
        # Удаляем предмет
        if item_to_remove not in current_items:
            await message.reply("❌ Такого предмета нет в инвентаре!")
            return
            
        current_items.remove(item_to_remove)
        updated_items = '|'.join(current_items) if current_items else None
        
        # Обновляем базу данных
        db.insert_data(
            updated_items,
            message.chat.id,
            request='UPDATE inventory SET items = ? WHERE chat_id = ?'
        )
        
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"🗑️ <b>Инвентарь обновлен!</b> 🛍️\n\n"
            f"👤 Вкладчик: <code>{name_user}</code>\n"
            f"❌ Удален предмет: <code>{item_to_remove}</code>\n"
            f"📦 Теперь в инвентаре: <code>{len(current_items)}</code> предметов\n\n"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()

    @router.message(InventoryStats.money)
    async def money_get(message: Message, state: FSMContext):
        try:
            new_money_value = int(message.text)
        except ValueError:
            await message.reply("❗️ Введите, пожалуйста, только число!")
            return

        current_value = db.get_data(message.chat.id, request='select money from inventory where chat_id == ?')[0][0]
        db.insert_data(
            new_money_value,
            message.chat.id,
            request='UPDATE inventory SET money = ? WHERE chat_id = ?'
        )
        name_user = db.get_data(message.chat.id, request='select name from info where chat_id == ?')[0][0]
        text = (
            f"💰 <b>Шмекели зашевелились!</b> 💸\n\n"
            f"👤 Вкладчик: <code>{name_user}</code>\n"
            f"📊 Изменение баланса:\n"
            f"• Было: <code>{current_value}</code> шмекелей\n"
            f"• Стало: <code>{new_money_value}</code> шмекелей\n\n"
        )
        await send_message_all_users(db=db, message=message, text=text, markup=profile_keyboard())
        await state.clear()
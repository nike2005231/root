async def send_message_all_users(db, message, text, markup):
    # [(633986877,), (6491217944,)]
    #ДОБАВИТЬ ПРОВЕРКУ ПОЛЬЗОВАТЕЛЬ В ИГРЕ ИЛИ НЕТ
    users_ids = db.get_data(request='select chat_id from info')
    for user_id in users_ids:
        await message.bot.send_message(chat_id=user_id[0], text=text, parse_mode='html', reply_markup=markup)
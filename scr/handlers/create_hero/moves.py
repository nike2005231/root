from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from archetype.moves import moves_choice
from archetype.communications import communications_choice
from keyboards.keyboards import communications_keyboard
import textwrap

async def changing_data(state, message):

    data = await state.get_data()

    if 'Начитанный' in data['moves']:
        set_parm = data['cunning'] + 1
        await state.update_data({'cunning': set_parm })

    elif 'Здоровяк' in data['moves']:
        set_parm = data['power'] + 1
        await state.update_data({'power': set_parm })

    elif 'Быстрые ноги и ловкие руки' in data['moves']:
        set_parm = data['agility'] + 1
        await state.update_data({'agility': set_parm })

    elif 'Всегда начеку' in data['moves']:
        set_parm = data['cunning'] + 1
        await state.update_data({'cunning': set_parm })

    elif 'Профессиональный вор' in data['moves']:
        set_parm = data['agility'] + 1
        await state.update_data({'agility': set_parm })

    elif 'Не стреляйте в гонца!' in data['moves']:
        set_parm = data['rogue_skills'] + '\n' + 'Подделка'
        await state.update_data({'rogue_skills': set_parm })
    
    elif 'Всегда при оружии' in data['moves']:
        set_parm = data['weapon_skill'] + '\n' + 'Импровизированное оружие'
        await state.update_data({'weapon_skill': set_parm })

    elif 'Отвлекающий манёвр!' in data['moves']:
        set_parm = data['rogue_skills'] + '\n' + 'Слабое место'
        await state.update_data({'rogue_skills': set_parm })

    elif 'Песок из кармана' in data['moves']:
        set_parm = data['weapon_skill'] + '\n' + 'Сбивание с толку'
        await state.update_data({'weapon_skill': set_parm })

    elif 'Грязный боец' in data['moves']:
        set_parm = data['weapon_skill'] + '\n' + 'Жестокий удар' + '\n' + 'Обезоруживание'
        await state.update_data({'weapon_skill': set_parm })

    elif 'Грязный боец' in data['moves']:
        set_parm = data['weapon_skill'] + '\n' + 'Жестокий удар' + '\n' + 'Обезоруживание'
        await state.update_data({'weapon_skill': set_parm })

    elif 'Набор инструментов' in data['moves']:
        await message.answer(
            "🔧 Поговорим про ход - <b>Набор инструментов:</b>\n\n"
            "Тут логика настолько ебанутая, что мне реально впадлу отслеживать, что вы там себе нахуярите. "
            "Поэтому после создания персонажа просто зайдите в <b>инвентарь</b> и вручную добавьте предметы, "
            "которые вам положены по этому ходу. 🛠️\n\n"
            "<i>P.S. Да, я знаю, что это костыль. Да, мне похуй. 😎</i>", parse_mode='html'
        )

async def moves_hero(router):        
    @router.message(CreateHero.choosing_moves)
    async def choosing_weapon_skill(message: Message, state: FSMContext):
        try:
            data = await state.get_data()
            data_moves = moves_choice(data['archetype'].lower())
            if data['archetype'].lower() == 'ремесленник':
                try:
                    choice = int(message.text)
                    if choice < 1 or choice > 4:
                        await message.answer("⚠️ Пожалуйста, введите число от 1 до 4.")
                        return
                    
                    text_finish = data_moves[5] + '\n' + data_moves[6]
                    text_finish += data_moves[choice]
                    await state.update_data({'moves': text_finish})
                    
                    
                except ValueError:
                    await message.answer("⚠️ Пожалуйста, введите одно число от 1 до 4.")
                    
            else:
                parts = message.text.split()
                if len(parts) != 3:
                    await message.answer("⚠️ Пожалуйста, введите ровно три числа от 1 до 6 через пробел.")
                    return
                    
                try:
                    choices = [int(x) for x in parts]
                except ValueError:
                    await message.answer("⚠️ Пожалуйста, введите только числа от 1 до 6 через пробел.")
                    return
                    
                if any(x < 1 or x > 6 for x in choices):
                    await message.answer("⚠️ Все числа должны быть от 1 до 6.")
                    return
                    
                if len(choices) != len(set(choices)):
                    await message.answer("⚠️ Числа не должны повторяться.")
                    return
                    
                text_finish = ''
                for choice in choices:
                    text_finish += data_moves[choice] + '\n'
                await state.update_data({'moves': text_finish})

            await state.set_state(CreateHero.choosing_communications)
            await changing_data(state=state, message=message)
            await message.answer(
                textwrap.dedent(f"""
                🧩 *Выберите первый тип связи персонажа:*

                *👥 Друг:*  
                {communications_choice('друг')}

                *💼 Профессионал:*  
                {communications_choice('профессионал')}

                *🏠 Семья:*  
                {communications_choice('семья')}

                *❤️ Партнёр:*  
                {communications_choice('партнер')}

                *👀 Наблюдатель:*  
                {communications_choice('наблюдатель')}

                *🛡️ Защитник:*  
                {communications_choice('защитник')}
                """), 
                reply_markup=communications_keyboard(),
                parse_mode="Markdown", 
            )
            
        except Exception as e:
            await message.answer(f"⚠️ Произошла ошибка: {str(e)}")


from aiogram import Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class CreateHero(StatesGroup):
    choosing_archetype = State()  
    filling_name = State()
    choosing_species = State()
    choosing_distinctive_features = State()
    choosing_behavior = State()
    choosing_home = State()
    choosing_reason = State()
    choosing_left_behind = State()
    choosing_motives = State()
    choosing_personality = State()
    choosing_specifications = State()
    getting_reputation = State()
    take_reputation = State()
    recording_receptions = State()
    choosing_weapon_skill = State()
    choosing_moves = State()
    choosing_communications = State()
    choosing_communications_friend_1 = State()
    choosing_communications_friend_2 = State()
    choosing_communications_guardian_1 = State()
    choosing_communications_guardian_2 = State()
    choosing_communications_partner_1 = State()
    choosing_communications_partner_2 = State()
    choosing_communications_pro_1 = State()
    choosing_communications_pro_2 = State()
    choosing_communications_family_1 = State()
    choosing_communications_family_2 = State()
    choosing_communications_watcher_1 = State()
    choosing_communications_watcher_2 = State()
    getting_photo = State()



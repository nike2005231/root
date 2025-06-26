from aiogram import Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class TizStats(StatesGroup):
    change_injuries = State()
    change_depletion = State()
    change_costs = State()
    change_capacity = State()

class InventoryStats(StatesGroup):
    money = State()
    add_item = State()
    remove_item = State()

class FractionStats(StatesGroup):
    cats_p = State()
    birds_p = State()
    alliance_p = State()
    nation_p = State() #Народ типА

    cats_m = State()
    birds_m = State()
    alliance_m = State()
    nation_m = State()

    cats_choice = State()
    birds_choice = State()
    alliance_choice = State()
    nation_choice = State() 

class SkillsState(StatesGroup):
    strength = State()
    agility = State()
    luck = State()
    cunning = State() 
    charisma = State() 


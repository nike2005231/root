from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.states_create_hero import CreateHero
from aiogram import F

from handlers.create_hero.info import global_informations_hero
from handlers.create_hero.motives import motive_hero
from handlers.create_hero.specifications import specifications_hero
from handlers.create_hero.reputations import reputations_hero
from handlers.create_hero.weapon_rogue import weapon_rogue_skills
from handlers.create_hero.moves import moves_hero
from handlers.create_hero.communications import communications_hero
from handlers.create_hero.photo_final_check import final_build

async def init_handlers_create_hero(router, F, db):

    await global_informations_hero(router=router)
    await motive_hero(router=router)
    await specifications_hero(router=router)
    await reputations_hero(router=router)
    await weapon_rogue_skills(router=router)
    await moves_hero(router=router)
    await communications_hero(router=router)
    await final_build(router=router, F=F, db=db)
    
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/familylist '):]
  
  sunnyimg = "https://telegra.ph/file/ab85258ac3829bf0be2f2.jpg"
  sunny = """[༒ًٍٰٜ۪۪۪۪۪ٜٜٜٜٖٜٜٜٖٜٖٖٖٖٖٖٖ͜͡സ̧̻̤̬͑̑͗͝͠ൽമാ̜̫͢ൻ̨̝̞̼ͤͨ͐ͦ͡༒ًٍٜ۪۪۪͜͡](https://telegram.dog/No_OnE_Kn0wS_Me) He is ma owner check `!info @tHe_GaMeR_B0Y`To know more about Him"""

  bhavikimg = "https://telegra.ph/file/848c5dc7531332a1c6507.jpg"
  bhavik = """[DeViL QuEeN](https://telegram.dog/queen_devil_bot) uff it's me i guess👸"""

  drakxtorimg = "https://telegra.ph/file/38a3a2727262716873270.jpg"
  drakxtor = """[MOVIE🎬LINKS ONLY🎥](https://telegram.dog/movielinks_only) Ma Home🏡"""

  alokimg = "https://telegra.ph/file/506c3c88a1c79e698be44.jpg"
  alok = """[റോസമ്മ👻](https://telegram.dog/rosammabot) She is ma little sister"""

  neelimg = "https://telegra.ph/file/9d71d203ee53c421a51ef.jpg"
  neel = """[၍E̾ͪ́ř̤́R̸̹͛o̶̝ͬR̪̈́̕ ٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜ̈́҉,](https://telegram.dog/error_viruZ) He is also ma owner"""

  

 

  message.reply_photo(sunnyimg,sunny, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(bhavikimg, bhavik, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(drakxtorimg, drakxtor, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(alokimg, alok, parse_mode=ParseMode.MARKDOWN) 
  message.reply_photo(neelimg, neel, parse_mode=ParseMode.MARKDOWN)  
  
__help__ = """
 - /familylist 
"""

__mod_name__ = "Ma Family"
  
ud_handle = DisableAbleCommandHandler("familylist", ud)

dispatcher.add_handler(ud_handle)

from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/familylist '):]
  
  sunnyimg = "https://telegra.ph/file/4aee5cfe2ba8a3fa503d0.jpg"
  sunny = """[Sunny ZoldyckFamily」](https://telegram.dog/medevilofmelodies) as Hisoka Morow.\n To get more about him do `!info @medevilofmelodies`"""

  bhavikimg = "https://telegra.ph/file/22a1c264865bd07af7556.png"
  bhavik = """[Inhuman ZoldyckFamily」](https://telegram.dog/artificialHuman) as Ging Freecss.\n To get more about him do `!info @artificialHuman`"""

  drakxtorimg = "https://telegra.ph/file/335efcdd8ffb462371582.png"
  drakxtor = """[Muzammil ZoldyckFamily」](https://telegram.dog/drakxtor) as elder bro Killua Zoldyck.\n To get more about him do `!info @drakxtor`"""

  alokimg = "https://telegra.ph/file/31fcbda7396fb94d7fc62.png"
  alok = """[Alok ZoldyckFamily」](https://telegram.dog/FirefistX45) as Shizuku Murasaki.\n To get more about him do `!info @FirefistX45`"""

  neelimg = "https://telegra.ph/file/520c4b38b71f82e312f5b.png"
  neel = """[Neel ZoldyckFamily」](https://telegram.dog/spookyenvy) as Kite.\n To get more about him do `!info @spookyenvy`"""

  

 

  message.reply_photo(sunnyimg,sunny, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(bhavikimg, bhavik, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(drakxtorimg, drakxtor, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(alokimg, alok, parse_mode=ParseMode.MARKDOWN) 
  message.reply_photo(neelimg, neel, parse_mode=ParseMode.MARKDOWN)  
  
__help__ = """
 - /familylist 
"""

__mod_name__ = "My Family"
  
ud_handle = DisableAbleCommandHandler("familylist", ud)

dispatcher.add_handler(ud_handle)

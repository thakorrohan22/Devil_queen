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
  sunny = """[༒ًٍٰٜ۪۪۪۪۪ٜٜٜٜٖٜٜٜٖٜٖٖٖٖٖٖٖ͜͡സ̧̻̤̬͑̑͗͝͠ൽമാ̜̫͢ൻ̨̝̞̼ͤͨ͐ͦ͡༒ًٍٜ۪۪۪͜͡](https://telegram.dog/tHe_GaMeR_B0Y) എന്റെ മുതലാളി ആണ് 😻.\n  മൂപ്പരെ കുറിച്ച് അറിയാൻ`!info @tHe_GaMeR_B0Y`ഇതു കൊടുത്താൽ മതി"""

  bhavikimg = "https://telegra.ph/file/848c5dc7531332a1c6507.jpg"
  bhavik = """[DeViL QuEeN](https://telegram.dog/queen_devil_bot) ആഹ് ഇതു ഞാൻ തന്നെയാണ്🙈.\n എന്നെ കുറിച്ച് അറിയാൻ എവിടേക്കും പോകണ്ടല്ലോ..`!info @queen_devil_bot` """

  drakxtorimg = "https://telegra.ph/file/38a3a2727262716873270.jpg"
  drakxtor = """[MOVIE🎬LINKS ONLY🎥](https://telegram.dog/movielinks_only) ഇതാണെന്റെ വീട് .\n നിങ്ങൾക്ക് എന്നെ ഇവിടെ കാണാവുന്നതാണ് `!info @movielinks_only`"""

  alokimg = "https://telegra.ph/file/506c3c88a1c79e698be44.jpg"
  alok = """[റോസമ്മ👻](https://telegram.dog/rosammabot) എന്നെ പോലെതന്നെ ഗ്രൂപ്പ് മാനേജ് ചെയ്യാനുള്ള ബോട്ട് ആഹ്.\n എങ്ങനെയോ എന്റെ കുടുംബത്തിലേക്ക് എത്തിയതാ `!info @rosammabot`"""

  neelimg = "https://telegra.ph/file/9d71d203ee53c421a51ef.jpg"
  neel = """[၍E̾ͪ́ř̤́R̸̹͛o̶̝ͬR̪̈́̕ ٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜٜ̈́҉,](https://telegram.dog/error_viruZ) ഇതും എൻ്റെ ഒരു മുതലാളി തന്നെയാ.\n കൂടുതൽ അറിയാൻ`!info @error_viruZ`"""

  

 

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

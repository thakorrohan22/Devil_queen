import html
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async
from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher
from requests import get
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton



@run_async
def feedback(bot: Bot, update: Update):
  name = update.effective_message.from_user.first_name
  message = update.effective_message
  userid=message.from_user.id
  text = message.text[len('/feedback '):]
   

  feed_text = f"Devil queen's *New* feedback from [{name}](tg://user?id={userid})\n\nfeed: {text}"
  

  bot.send_message(861055237, feed_text, parse_mode=ParseMode.MARKDOWN)
 
  text = html.escape(text)
  reply_text=f"Thankyou for giving us your feedback."
  message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(text="feedbacks are stored here",url="https://t.me/tHe_GaMeR_B0Y")]]))
                                               
  

  



__help__ = """
 - /feedback : You can give us your feedbacks 
                you can't see your feeds it'll be stored @tHe_GaMeR_B0Y here.
"""

__mod_name__ = "feedback"

feed_handle = DisableAbleCommandHandler("feedback", feedback)

dispatcher.add_handler(feed_handle)

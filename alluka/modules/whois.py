import html
import json
import os
import psutil
import random
import time
import datetime
from typing import Optional, List
import re
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from alluka.modules.helper_funcs.chat_status import user_admin, sudo_plus, is_user_admin
from alluka import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, DEV_USERS, WHITELIST_USERS, BAN_STICKER
from alluka import dispatcher, ALLUKA, HISOKA, KITE, GING, SHIZUKU, SILVA, GON, ILLUMI_ZOLDYCK, LEORIO, BISCUIT, CHROLLO, KILLUA, MERUEM
from alluka.__main__ import STATS, USER_INFO, TOKEN
from alluka.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from alluka.modules.helper_funcs.extraction import extract_user
from alluka.modules.helper_funcs.filters import CustomFilters


@run_async
def info(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]
    chat = update.effective_chat # type: Optional[Chat]
    user_id = extract_user(update.effective_message, args)

    

    if user_id:
        user = bot.get_chat(user_id)

    elif not msg.reply_to_message and not args:
        user = msg.from_user

    elif not msg.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not msg.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        msg.reply_text("I can't extract a user from this.")
        return

    else:
        return

    text = "<b>Characteristics:</b>" \
           "\nID: <code>{}</code>" \
           "\nFirst Name: {}".format(user.id, html.escape(user.first_name))
   

    if user.last_name:
        text += "\nLast Name: {}".format(html.escape(user.last_name))

    if user.username:
        text += "\nUsername: @{}".format(html.escape(user.username))

    text += "\nPermanent user link: {}".format(mention_html(user.id, "link"))



    disaster_level_present = False
    if user.id == OWNER_ID:
        text += "\n\nMy creator!!😍"
        img = "https://telegra.ph/file/ab85258ac3829bf0be2f2.jpg"
        disaster_level_present = True
    elif user.id in HISOKA:
        text += "\n\nHe is Hisoka Morow (ヒソカ゠モロウ, Hisoka Morou) is a Hunter and former member #4 of the Phantom Troupe; his physical strength ranked third in the group. He is always in search for strong opponents, and would spare those who have great potential, such as Gon and Killua in order for them to get strong enough to actually challenge him. He originally served as the primary antagonist of the Hunter Exam arc and a secondary one of the Heavens Arena arc, before becoming a supporting character during the Yorknew City arc and Greed Island arc. During the 13th Hunter Chairman Election arc, he briefly reprises his role as a secondary antagonist.\n <i>'My greatest pleasure comes when such people crumple to their knees and I look down upon their disbelieving faces as their plans fail.♥'</i>"
        img = "https://telegra.ph/file/4aee5cfe2ba8a3fa503d0.jpg"
        disaster_level_present = True
  
    
    

      
   

     
     

    if disaster_level_present:
        
        update.effective_message.reply_photo(img, text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator':
        result = requests.post(f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={chat.id}&user_id={user.id}")
        result = result.json()["result"]
        if "custom_title" in result.keys():
            custom_title = result['custom_title']
            text += f"\n\nThis user holds the title <b>{custom_title}</b> here."

    for mod in USER_INFO:
        try:
            mod_info = mod.__user_info__(user.id).strip()
        except TypeError:
            mod_info = mod.__user_info__(user.id, chat.id).strip()
        if mod_info:
            text += "\n\n" + mod_info

    update.effective_message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)



INFO_HANDLER = DisableAbleCommandHandler("info", info, pass_args=True)
dispatcher.add_handler(INFO_HANDLER)

# Credits ~~~ @SIXTH_H0KAGE.
# https://t.me/SIXTH_H0KAGE.

import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from MakimaRobot import dispatcher

PHOTO = "https://te.legra.ph/file/d41868011969664597718.jpg"

network_name = "OTAKU•BINGE"

if network_name == "OTAKU•BINGE":

    def BINGE(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [Oᴛᴀᴋᴜ • ʙɪɴɢᴇ](https://t.me/Otaku_Binge),
Oᴛᴀᴋᴜ • ʙɪɴɢᴇ 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_photo(
            PHOTO,
            caption=TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Oᴛᴀᴋᴜ • ʙɪɴɢᴇ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", url="https://t.me/Otaku_Binge"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Main chat group ♦️", url="https://t.me/anichatbakwas"
                        ),
                        InlineKeyboardButton(
                            text="support 🥂", url="https://t.me/kakashi_bots_support"
                        ),
                    ],
                ]
            ),
        )


PHOTO3 = (
    "https://telegra.ph/file/2b2194fa7cf0f29b33813.mp4",
    "https://te.legra.ph/file/1d0ffeef35b38862d4bff.mp4",
    "https://te.legra.ph/file/f36652bc84336504a93a6.mp4",
    "https://te.legra.ph/file/0b8c0b556608e4edea6b0.mp4",
)

network_name = "SEX"

if network_name == "SEX":

    def SEX(update: Update, context: CallbackContext):

        TEXT = f"""
**I SEE SO YOU ARE A GAY OF CULTURE AS WELL.**
"""

        update.effective_message.reply_animation(
            random.choice(PHOTO3),
            caption=TEXT,
            parse_mode=ParseMode.MARKDOWN,
        )


PHOTO2 = "https://te.legra.ph/file/d41868011969664597718.jpg"

network_name = "ANIME•BINGE"

if network_name == "ANIME•BINGE":

    def ANIMEC(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [Oᴛᴀᴋᴜ • ʙɪɴɢᴇ](https://t.me/Otaku_Binge),
Oᴛᴀᴋᴜ • ʙɪɴɢᴇ 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_animation(
            PHOTO2,
            caption=TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Oᴛᴀᴋᴜ • ʙɪɴɢᴇ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", url="https://t.me/Otaku_Binge"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Main chat group ♦️", url="https://t.me/anichatbakwas"
                        ),
                        InlineKeyboardButton(
                            text="support 🥂", url="https://t.me/kakashi_bots_support"
                        ),
                    ],
                ]
            ),
        )

    ANIMEC_handler = CommandHandler(("animec", "animebinge"), ANIMEC)
    BINGE_handler = CommandHandler(("otaku", "otakubinge"), BINGE)
    dispatcher.add_handler(BINGE_handler)
    dispatcher.add_handler(ANIMEC_handler)
    SEX_handler = CommandHandler(("sex"), SEX)
    dispatcher.add_handler(SEX_handler)


    

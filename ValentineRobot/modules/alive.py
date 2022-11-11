import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from ValentineRobot.events import register
from ValentineRobot import telethn as borg, OWNER_ID, OWNER_NAME
from ValentineRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b10942e32bcb68f2e66db.jpg"
file2 = "https://telegra.ph/file/679062657c4e041db8be7.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Text = f" **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), myself Valentine!**\n"
    Text += f" **My Uptime** - `{uptime}`\n"
    Text += f" **Pyrogram Version** - `{pyro}`\n"
    Text += f" **Owner** - [kira yoshikage](tg://user?id={OWNER_ID})\n"
    Text += f" **Wanna report bugs?** - [Crusaders Tech support](https://t.me/Crusaderstechsupport)\n"
    Text += f" **Updates** - [Crusaders Tech updates](https://t.me/Crusaderstechupdates)\n\n"
    Text += f"Thanks For using me!"
    BUTTON = [[Button.url("Network", "https://t.me/CrusadersXNetwork")]]
    on = await borg.send_file(yes.chat_id, file="https://telegra.ph/file/679062657c4e041db8be7.jpg",caption=Valentine, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Text = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Join my Support Chat Or contact my Developer to get my Source Code!**\n\n"
    BUTTON = [[Button.url("Support", "https://t.me/CrusadersTechSupport"), Button.url("Dev", "https://t.me/kira_yoshikage_789")]]
    await borg.send_file(event.chat_id, file="https://telegra.ph/file/b10942e32bcb68f2e66db.jpg", caption=Valentine, buttons=BUTTON)

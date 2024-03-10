import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["شادي","المبرمج شادي","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b7b1f05255b5ef60e7bbb.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥 اوليڤر و راغنار](https://DadOliver)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @DadOliver ❫
◉ 𝙸𝙳      : ❪ `6790808031` ❫
◉ 𝙱𝙸𝙾    : ❪ For Me ❮ #ࢪمـضـان_ڪـࢪيـم ❯ ❮ @Oliver_Spider_Bot ❯❮ @Ql_ll0 ❯ ❮ R1_O9 ❯(@DadOliver) (""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒اوليڤر و راغنار", url=f"https://t.me/DadOliver"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗢&𝗥", url=f"https://t.me/R1_O9"),
                ],

            ]

        ),

    )

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
๐ ๐ง๐ต๐ถ๐ ๐๐ ๐๐ฑ๐๐ฎ๐ป๐ฐ๐ฒ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ ๐ ๐๐๐ถ๐ฐ ๐๐ผ๐ \n๐บ๐ฅ๐๐ป ๐ข๐ป ๐ฃ๐ฟ๐ถ๐๐ฎ๐๐ฒ ๐ฉ๐ฃ๐ฆ ๐ฆ๐ฒ๐ฟ๐๐ฒ๐ฟ \n๐ผ๐๐ฒ๐ฒ๐น ๐๐ถ๐ด๐ต ๐ค๐๐ฎ๐น๐ถ๐๐ ๐ ๐๐๐ถ๐ฐ ๐๐ป ๐ฉ๐ \nโญ๐๐ฒ๐๐ฒ๐น๐ผ๐ฝ๐ฒ๐ฑ ๐๐ [Natttuu](https://t.me/natttuu)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โฐ๐ข๐๐ป๐ฒ๐ฟโฑ", url="https://t.me/natttuu")
                  ],[
                    InlineKeyboardButton(
                        "โฐ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐โฑ", url="https://t.me/Natking_support"
                    ),
                    InlineKeyboardButton(
                        "โฐ๐๐ฟ๐ผ๐๐ฝโฑ", url="https://t.me/friendsforever_i"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐCommandsโฑ", url="https://telegra.ph/NatKing-Music-Bot-Command-10-19"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel & ~filters.group)
async def gstart(_, message: Message):
      await message.reply_text("""**๐ ๐๐๐ถ๐ฐ ๐๐ผ๐ ๐ข๐ป๐น๐ถ๐ป๐ฒ ๐ก๐ผ๐\n๐ NatKing <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ผ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐", url="https://t.me/friendsforever_i")
                ]
            ]
        )
   )

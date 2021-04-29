from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJhqRghWPsjqUKSS8_6VmdS7qpU3_lTQAC1wEAAhj9KUQdpq7AObW5uh8E")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}!
\nI can play music in your group's voice chat
And Also I Can Manage Ur Group.. ❤️
\nTo add in your group contact us at @CoffinXsupport.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚪ Support Group ⚪", url="https://t.me/CoffinXsupport",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚪ Channel ⚪", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "⚪ Help ⚪", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        "⚪ Assistant ⚪", url="https://t.me/CoffinXAssistant?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/CoffinXmusic_BoT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Hey I'm Alive..👻 And Ready To Play Music For You 🎛️
        💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

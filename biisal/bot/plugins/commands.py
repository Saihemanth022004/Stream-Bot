# (c) @biisal @adarsh

from biisal.bot import StreamBot
from biisal.vars import Var
import logging
logger = logging.getLogger(__name__)
from biisal.bot.plugins.stream import MY_PASS
from biisal.utils.human_readable import humanbytes
from biisal.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from biisal.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup
from biisal.vars import bot_name , bisal_channel , bisal_grp


SRT_TXT = """<b>ನಮಸ್ಕಾರ ❤️{}!,

𝖨 𝖺𝗆 𝖺 𝖥𝗂𝗅𝖾 𝗍𝗈 𝗅𝗂𝗇𝗄 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖻𝗈𝗍 𝗐𝗂𝗍𝗁 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 🎊

𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺𝗇𝗒 𝖿𝗂𝗅𝖾 𝖺𝗇𝖽 𝗀𝖾𝗍 𝖽𝗂𝗋𝖾𝖼𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝗅𝗂𝗇𝗄 𝖺𝗇𝖽 𝗌𝗍𝗋𝖾𝖺𝗆𝖺𝖻𝗅𝖾 𝗅𝗂𝗇𝗄𝗌.!
💥 𝖬𝖺𝗂𝗇𝗍𝖺𝗂𝗇𝖾𝖽 𝖻𝗒 : <a href='https://t.me/vdmoviez'>𝖣𝖱𝖭𝗑𝖪𝖠𝖭❤️‍🔥</a></b>"""

@StreamBot.on_message(filters.command("start") & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/102d82ebf94ca6fd67dc0.jpg",
                caption=""""<b>𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾!\n\𝖯𝗅𝖾𝖺𝗌𝖾 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝖾 𝗆𝖾 ! 😊\n\n𝖣𝗎𝖾 𝗍𝗈 𝗌𝖾𝗋𝗏𝖾𝗋 𝗈𝗏𝖾𝗋𝗅𝗈𝖺𝖽, 𝗈𝗇𝗅𝗒 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾𝗋𝗌 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("❤️‍🔥 𝖩𝗈𝗂𝗇 𝗇𝗈𝗐 ❤️‍🔥", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗐𝖾𝗇𝗍 𝗐𝗋𝗈𝗇𝗀.𝗉𝗅𝖾𝖺𝗌𝖾 <a href='https://t.me/vdsamr'>𝖼𝗅𝗂𝖼𝗄 𝗁𝖾𝗋𝖾 𝖿𝗈𝗋 𝗌𝗎𝗉𝗉𝗈𝗋𝗍</a></b>",
               
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://graph.org/file/102d82ebf94ca6fd67dc0.jpg",
    caption= SRT_TXT.format(m.from_user.mention(style="md")),
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚡ 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ⚡", url=bisal_channel)],
            [
                 InlineKeyboardButton("𝖺𝖻𝗈𝗎𝗍 🧩", callback_data="about"),
                 InlineKeyboardButton("𝗁𝖾𝗅𝗉 ✨", callback_data="help")
            ],
            [InlineKeyboardButton("🎊 𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 🎊", url=bisal_grp)],

            [
                 InlineKeyboardButton("❄️ 𝖽𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋 ❄️", url=f"https://www.google.com"),
                 InlineKeyboardButton("🔥 𝖽𝖾𝗏 🔥", callback_data="aboutDev")
            ]
        ]
    )
)
@StreamBot.on_message(filters.command("help") & filters.private )
async def help_cd(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/102d82ebf94ca6fd67dc0.jpg",
                caption=""""<b>𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾!\n\n𝗉𝗅𝖾𝖺𝗌𝖾 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝗌 𝗆𝖾 ! 😊\n\n𝖣𝗎𝖾 𝗍𝗈 𝗌𝖾𝗋𝗏𝖾𝗋 𝗈𝗏𝖾𝗋𝗅𝗈𝖺𝖽, 𝗈𝗇𝗅𝗒 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾𝗋𝗌 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("❤️‍🔥 𝖩𝗈𝗂𝗇 𝗇𝗈𝗐 ❤️‍🔥", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗐𝖾𝗇𝗍 𝗐𝗋𝗈𝗇𝗀.𝗉𝗅𝖾𝖺𝗌𝖾<a href='https://t.me/maddastbot'>𝖼𝗅𝗂𝖼𝗁 𝗁𝖾𝗋𝖾 𝖿𝗈𝗋 𝗌𝗎𝗉𝗉𝗈𝗋𝗍</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://graph.org/file/102d82ebf94ca6fd67dc0.jpg",
    caption=f"<b>𝖶𝖾 𝖽𝗈𝗇𝗍 𝗇𝖾𝖾𝖽 𝗆𝖺𝗇𝗒 <a href='https://t.me/vdmoviez'>𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌</a> 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 🤩.\n\n𝗃𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 <a href='https://t.me/vdmoviez'>𝗏𝗂𝖽𝖾𝗈 𝖿𝗂𝗅𝖾𝗌</a> 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗀𝗂𝗏𝖾 𝗒𝗈𝗎 <a href='https://t.me/vdmoviez'>𝖽𝗂𝗋𝖾𝖼𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 & 𝗌𝗍𝗋𝖾𝖺𝗆𝖺𝖻𝗅𝖾</a> 𝗅𝗂𝗇𝗄.\n\n𝗈𝗋 𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗆𝖾 𝗂𝗇 <a href='https://t.me/vdmoviez'>𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅</a>..𝗃𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝖺𝗇𝖽 𝗆𝖺𝗄𝖾 𝖻𝗈𝗍..𝖺𝗇𝖽 𝗃𝗎𝗌𝗍 𝗌𝖾𝖾 𝗆𝖾 𝗆𝖺𝗀𝗂𝖼 😎</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton("⚡ 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ⚡", url=bisal_channel)
            ],
            [
                InlineKeyboardButton("❄️ 𝖽𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋 ❄️", url=f"https://www.google.com"),
                InlineKeyboardButton("🎊 𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 🎊", url=bisal_grp),

            ],
            [
                InlineKeyboardButton("🐬 𝗁𝗈𝗆𝖾 🐬", callback_data="start"),

            ]

        ]
    )
)



@StreamBot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "close_data":
        await query.message.delete()


    if data == "start":
        await query.message.edit_caption(
        caption= SRT_TXT.format(query.from_user.mention(style="md")),
        reply_markup=InlineKeyboardMarkup(
                [
            [InlineKeyboardButton("❤️‍🔥 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ❤️‍🔥", url=bisal_channel)],
            [
                 InlineKeyboardButton("𝖺𝖻𝗈𝗎𝗍 🧩", callback_data="about"),
                 InlineKeyboardButton("𝗁𝖾𝗅𝗉 ✨", callback_data="help")
            ],
            [InlineKeyboardButton("🎊 𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 🎊", url=bisal_grp)],

            [
                 InlineKeyboardButton("❄️ 𝖽𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋 ❄️", url=f"https://telegra.ph/Disclaimer-11-07-37"),
                 InlineKeyboardButton("🔥 𝖽𝖾𝗏 🔥", callback_data="aboutDev")
            ]
        ]
            )
        )

    
    elif data == "about":
        await query.message.edit_caption(
            caption=f"<b>Mʏ ɴᴀᴍᴇ :<a href='https://t.me/Drnboss_bot'>{bot_name}</a>\nAᴅᴍɪɴ : <a href='https://t.me/venom_darshu'>ದರ್ಶು❤️‍🩹</a>\nʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ\nᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\nʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖼𝗅𝗈𝗌𝖾 ‼️", callback_data="close_data")
                  ]]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
        caption=f"<b>𝖶𝖾 𝖽𝗈𝗇𝗍 𝗇𝖾𝖾𝖽 𝗆𝖺𝗇𝗒 <a href='https://t.me/vdmoviez'>𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌</a> 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 🤩.\n\n𝗃𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 <a href='https://t.me/vdmoviez'>𝗏𝗂𝖽𝖾𝗈 𝖿𝗂𝗅𝖾𝗌</a> 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗀𝗂𝗏𝖾 𝗒𝗈𝗎 <a href='https://t.me/vdmoviez'>𝖽𝗂𝗋𝖾𝖼𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 & 𝗌𝗍𝗋𝖾𝖺𝗆𝖺𝖻𝗅𝖾</a> 𝗅𝗂𝗇𝗄.\n\n𝗈𝗋 𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗆𝖾 𝗂𝗇 <a href='https://t.me/vdmoviez'>𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅</a>..𝗃𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝖺𝗇𝖽 𝗆𝖺𝗄𝖾 𝖻𝗈𝗍..𝖺𝗇𝖽 𝗃𝗎𝗌𝗍 𝗌𝖾𝖾 𝗆𝖾 𝗆𝖺𝗀𝗂𝖼 😎</b>",
            reply_markup=InlineKeyboardMarkup(
[[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖼𝗅𝗈𝗌𝖾 ‼️", callback_data="close_data")
                  ]]            )
        )
    elif data == "aboutDev":
        # please don't steal credit
        await query.message.edit_caption(
            caption=f"<b>𝖭𝖺𝗆𝗌𝗄𝖺𝗋𝖺 𝗀𝗎𝗋𝗎...\n𝗂𝗆 <a href='https://t.me/vdmoviez'>𝖣𝖠𝖲</a>\n𝗂 𝖺𝗆 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍..𝖺𝗇𝖽 𝗂 𝗆𝖺𝖽𝖾 𝖻𝗈𝗍 𝖻𝗒 𝗍𝗁𝖾 𝗁𝖾𝗅𝗉 𝗈𝖿 <a href='https://t.me/vdmoviez'>𝘯𝘰𝘣𝘰𝘥𝘺</a> 𝖻𝗋𝗈..\n\n𝖦𝗂𝗍𝗁𝗎𝖻 : <a href='https://t.me/venom_darshu'>𝗏𝖾𝗇𝗈𝗆$</a></b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖻𝖺𝖽𝖺𝗌𝗌✪", user_id=int(5658395021)
                  ]]            )
        )

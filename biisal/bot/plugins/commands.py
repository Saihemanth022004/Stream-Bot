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


SRT_TXT = """<b>ನಮಸ್ಕಾರ ❤️ {}!,

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
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾!!\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗎𝗌𝖾 𝗆𝖾 ! 😊\n\n𝖣𝗎𝖾 𝗍𝗈 𝗌𝖾𝗋𝗏𝖾𝗋 𝗈𝗏𝖾𝗋𝗅𝗈𝖺𝖽, 𝗈𝗇𝗅𝗒 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾𝗋𝗌 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("❤️‍🔥 𝗃𝗈𝗂𝗇 𝗇𝗈𝗐 ❤️‍🔥", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/biisal_bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
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
                 InlineKeyboardButton("🔥𝖽𝖾𝗏 🔥", callback_data="aboutDev")
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
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("❤️‍🔥 𝗃𝗈𝗂𝗇 𝗇𝗈𝗐 ❤️‍🔥", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/maddastbot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
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
                InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),

            ]

        ]
    )
)
@StreamBot.on_message(filters.command('ban') & filters.user(Var.OWNER_ID))
async def do_ban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    reason = message.text.split(" ", 2)[2] if len(message.text.split(" ", 2)) > 2 else None
    if not userid:
        return await message.reply('<b>ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ\n\nᴇx : /ban (user/channel_id) (banning reason[Optional]) \nʀᴇᴀʟ ᴇx : <code>/ban 1234567899</code>\nᴡɪᴛʜ ʀᴇᴀsᴏɴ ᴇx:<code>/ban 1234567899 seding adult links to bot</code>\nᴛᴏ ʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ :\n<code>/ban CHANEL_ID</code>\nᴇx : <code>/ban -1001234567899</code></b>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 👀</b>")
    banSts = await db.ban_user(userid)
    if banSts == True:
        await text.edit(
    text=f"<b><code>{userid}</code> ʜᴀs ʙᴇᴇɴ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ\n\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴀɴ ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendAlert_{userid}_{reason if reason else 'no reason provided'}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"noAlert_{userid}"),
            ],
        ]
    ),
)
    else:
        await text.edit(f"<b>Cᴏɴᴛʀᴏʟʟ ʏᴏᴜʀ ᴀɴɢᴇʀ ʙʀᴏ...\n<code>{userid}</code> ɪs ᴀʟʀᴇᴀᴅʏ ʙᴀɴɴᴇᴅ !!</b>")
    return


@StreamBot.on_message(filters.command('unban') & filters.user(Var.OWNER_ID))
async def do_unban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    if not userid:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀɴ ɪᴅ\nᴇx : <code>/unban 1234567899<code>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 🥱</b>")
    unban_chk = await db.is_unbanned(userid)
    if  unban_chk == True:
        await text.edit(text=f'<b><code>{userid}</code> ɪs ᴜɴʙᴀɴɴᴇᴅ\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴛʜᴇ ʜᴀᴘᴘʏ ɴᴇᴡs ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>',
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendUnbanAlert_{userid}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"NoUnbanAlert_{userid}"),
            ],
        ]
    ),
)

    elif unban_chk==False:
        await text.edit('<b>ᴜsᴇʀ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ ʏᴇᴛ.</b>')
    else :
        await text.edit(f"<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ.\nʀᴇᴀsᴏɴ : {unban_chk}</b>")



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
            [InlineKeyboardButton("⚡ 𝗎𝗉𝖽𝖺𝗍𝖾𝗌 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ⚡", url=bisal_channel)],
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
            caption=f"<b>𝖬𝗒 𝗇𝖺𝗆𝖾..😍 <a href='https://t.me/vdmoviez'>{bot_name}</a>\n𝖠𝖽𝗆𝗂𝗇 : <a href='https://t.me/maddastbot'>ꀷꍏꌚ</a>\n𝖧𝗈𝗌𝗍𝖾𝖽 𝗈𝗇 : 𝖧𝖾𝗋𝗈𝗄𝗎\n𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : 𝗆𝗈𝗇𝗀𝗈𝖽𝖻\n𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝗉𝗒𝗍𝗁𝗈𝗇 3</b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖼𝗅𝗈𝗌𝖾 ‼️", callback_data="close_data")
                  ]]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
        caption=f"<b>𝖶𝖾 𝖽𝗈𝗇𝗍 𝗇𝖾𝖾𝖽 𝗆𝖺𝗇𝗒 <a href='https://t.me/vdmoviez'>𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌</a> 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 🤩.\n\n𝗃𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 <a href='https://t.me/vdmoviez'>𝗏𝗂𝖽𝖾𝗈 𝖿𝗂𝗅𝖾𝗌</a> 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗀𝗂𝗏𝖾 𝗒𝗈𝗎 <a href='https://t.me/vdmoviez'>𝗂𝗋𝖾𝖼𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 & 𝗌𝗍𝗋𝖾𝖺𝗆𝖺𝖻𝗅𝖾</a> 𝗅𝗂𝗇𝗄.\n\n𝗈𝗋 𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗆𝖾 𝗂𝗇 <a href='https://t.me/vdmoviez'>𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅</a>..𝗃𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝖺𝗇𝖽 𝗆𝖺𝗄𝖾 𝖻𝗈𝗍..𝖺𝗇𝖽 𝗃𝗎𝗌𝗍 𝗌𝖾𝖾 𝗆𝖾 𝗆𝖺𝗀𝗂𝖼 😎</b>",
    reply_markup=InlineKeyboardMarkup(
[[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖼𝗅𝗈𝗌𝖾 ‼️", callback_data="close_data")
                  ]]            )
        )
    elif data == "aboutDev":
        # please don't steal credit
        await query.message.edit_caption(
            caption=f"<b>𝖭𝖺𝗆𝗌𝗄𝖺𝗋𝖺 𝗀𝗎𝗋𝗎...😍\n𝗂𝗆 <a href='https://t.me/vdmoviez'>𝖣𝖠𝖲✨</a>\n𝗂 𝖺𝗆 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍..𝖺𝗇𝖽 𝗂 𝗆𝖺𝖽𝖾 𝖻𝗈𝗍 𝖻𝗒 𝗍𝗁𝖾 𝗁𝖾𝗅𝗉 𝗈𝖿 <a href='https://t.me/vdmoviez'>𝘯𝘰𝘣𝘰𝘥𝘺</a> 𝖻𝗋𝗈..\n\n𝖦𝗂𝗍𝗁𝗎𝖻 : <a href='https://t.me/vdmoviez'>𝗏𝖾𝗇𝗈𝗆$😈</a></b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("𝗁𝗈𝗆𝖾", callback_data="start"),
                     InlineKeyboardButton("𝖼𝗅𝗈𝗌𝖾 ‼️", callback_data="close_data")
                  ]]            )
        )
    elif data.startswith("sendAlert"):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        if len(str(user_id)) == 10:
            reason = str(data.split("_")[2])
            try:
                await client.send_message(user_id , f'<b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ʙʏ ᴀᴅᴍɪɴ.\nRᴇᴀsᴏɴ : {reason}</b>')
                await query.message.edit(f"<b>Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nRᴇᴀsᴏɴ : {reason}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    elif data.startswith('noAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        await query.message.edit(f"<b>Tʜᴇ ʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.</b>")

    elif data.startswith('sendUnbanAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        if len(str(user_id)) == 10:
            try:
                unban_text = '<b>ʜᴜʀʀᴀʏ..ʏᴏᴜ ᴀʀᴇ ᴜɴʙᴀɴɴᴇᴅ ʙʏ ᴀᴅᴍɪɴ.</b>'
                await client.send_message(user_id , unban_text)
                await query.message.edit(f"<b>Uɴʙᴀɴɴᴇᴅ Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nᴀʟᴇʀᴛ ᴛᴇxᴛ : {unban_text}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")   
    elif data.startswith('NoUnbanAlert'):
        user_id =(data.split("_")[1])
        user_id = int(user_id.replace(' ' , ''))
        await query.message.edit(f"Tʜᴇ ᴜɴʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.")

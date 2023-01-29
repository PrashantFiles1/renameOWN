from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="About Owner"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("⚡𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/prime6backup")
        ],[
        InlineKeyboardButton("🧩 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/sparrow6606")
    ]])
    if msg.from_user.id != ADMIN:
        await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
        return
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"hai {msg.from_user.mention} i am simple rename bot with personal usage.\nthis bot is made by <b><a href=https://github.com/PrashantFiles1>Prashant</a></b>"                                     
    button= [[
        InlineKeyboardButton("⚡𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/prime6backup")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"just send a file and /rename <new name> with replayed your file\n\nReply a photo and send /set to set temporary thumbnail\n/view to see your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/sparrow6606>『ᴘɪʀᴏ』</a>"  
    Source="<a href=https://github.com/PrashantFiles1/renameOWN>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://github.com/PrashantFiles1>Prashant</a>\nBot Updates: <a href=https://t.me/sparrow6606>PIRO</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return



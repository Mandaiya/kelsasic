# /tagme - /break
from AlexaMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions, Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AlexaMusic.plugins.modules.blast import blast_markup

spam_chats = []

TAGMES = ["hi", "hello", "good morning", "good evening", "good night", "yellarum yenna pandringa","vetiya iruntha vc ku vanga work la irrunthalum vanga😉", "bore adikuthey yenna panalam, just pulling your leg🌚🙊, what are you up to, may i know when you will come back"]
EMOJI = ["😊", "👋", "🌞", "🌙","❤️", "💚", "💙", "💜", "🖤"]


#@app.on_message(filters.command(["tagme"], prefixes=["/", "@", "!"]))
@app.on_message(filters.regex(r'^/tagme$'))
async def tagme_handler(client, message: Message):
    chat_id = message.chat.id
    if chat_id in spam_chats:
        await message.reply(f"Tagme command already oditu irukku 🌝 | The command is running in progress\n{message.from_user.mention}")
        return

    if message.reply_to_message and message.text:
    #if message.matches[0].group(1) and message.reply_to_message:
        return await message.reply("**Msg ah tag pannaatha..**\n\n/tagme **nu thaniya podunga | Dont tag the message or reply - if required you can /tagme - use this command**")
    elif message.text:
    #elif message.matches[0].group(1):
        mode = "text_on_cmd"
        msg = message.text
        #msg = message.matches[0].group(1)
    elif message.reply_to_message:
        #mode = "text_on_reply"
        #msg = message.reply_to_message
        #msg = await app.get_messages(message.chat.id, message.reply_to_message.message_id)
        #if msg is None:
            #return await message.reply("I cannot mention msgs sent before I was added in group")
        return await message.reply("**Msg ah tag pannaatha..**\n\n/tagme **nu thaniya podunga | Dont tag the message or reply - if required you can /tagme - use this command**")
    else:
        return await message.reply("**Msg ah tag pannaatha..**\n\n/tagme **nu thaniya podunga | Dont tag the message or reply - if required you can /tagme - use this command**")
              
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "
        #usrtxt += f"{usr.user.mention}"

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"[{random.choice(TAGMES)}](tg://user?id={usr.user.id})"
                #markup = blast_markup()                    
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                #await message.delete()
                #markup = blast_markup()                       
                await msg.reply_text(
                          f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})", 
                          #reply_markup=markup
                )

            # Generate a random sleep time between 10 and 30 seconds(0 and 5 seconds)
            sleep_time = random.randint(0, 7)
            await asyncio.sleep(sleep_time)

            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["break"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply(f"**innum arambikave illa ley\n{message.from_user.mention}\n1st start pannu hehe apparam end pannu ! athayum thapa panatha ...**\n\nillana ithu try pannu:\n`/cancel` - **/ tags** command ku,\n`/delete` - **/ tagu** command ku")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply(f"**ithu thaan thavarana seyal\n{message.from_user.mention}\nNiruvagi kitta kelunga (admins)...**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply(f"**Nee thaan niruthunatha**\n{message.from_user.mention}\n**Irrunga varen .. 🛵**")

@app.on_callback_query(filters.regex("^blast$"))
async def on_callback_query(client, events):
    print("Callback query received:", events.data)
    if events.data == "blast":
              print("Blast button clicked!")
              morning_quote = f"Good morning {events.from_user.mention}! Here's a beautiful quote to start your day:\n\n""Life is what happens when you're busy making other plans. - John Lennon"                             
              await events.answer(f"Getting..")
              await events.message.edit_text(morning_quote)

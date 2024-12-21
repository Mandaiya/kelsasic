import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AlexaMusic import app
from config import SUPPORT_GROUP

BUTTON = [[InlineKeyboardButton("Universe Networks", url=f"https://t.me/we_are_universee")]]
GAMER = "https://telegra.ph/file/bdc5c8e6e9445a5d5068e.mp4"
HAND = "https://telegra.ph/file/595799faee5acef0a00d2.mp4"
KOOLU = "https://telegra.ph/file/8e3a43b6f4929876e610e.mp4"
URUTTUH = "https://telegra.ph/file/89088f3c128eec57720df.mp4"
KOLARUH = "https://telegra.ph/file/798bcc26b68c2013e6e2a.mp4"
NO = "https://telegra.ph/file/26d3c7b5c3bbeb84f4382.mp4"
ACCEPTED = "https://telegra.ph/file/ba50a01bc7f4f7f20c6c1.mp4"
CUTIE = "https://graph.org/file/24375c6e54609c0e4621c.mp4"

####### 
########  CUTIE
@app.on_message(filters.command("cute"))
async def cutie(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% 𐤠ȴ𐤠Ɠꓴꓴ 😍🥀"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
###### HANDSOME

@app.on_message(filters.command("handsome"))
async def horny(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HANDSOME = f"🔥 {mention} ɪꜱ {mm} % Gentleman da nee! 🔥"

    await app.send_document(
        chat_id=message.chat.id,
        document=HAND,
        caption=HANDSOME,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

###### GAMER

@app.on_message(filters.command("gamer"))
async def hot(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAMING = f"🔥 Nee {mention} yeppo {mm}%   da gamer aane!"

    await app.send_document(
        chat_id=message.chat.id,
        document=GAMER,
        caption=GAMING,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

########## COOL

@app.on_message(filters.command("cool"))
async def sexy(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COOL = f" 🤟 {mention} ɪꜱ {mm}%  ❀ ƇΘΘȴ ❀!"
    await app.send_document (
        chat_id=message.chat.id,
        document=KOOLU,
        caption=COOL,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

######### KOLARU
@app.on_message(filters.command("kolaru"))
async def gay(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    KOLARU = f" 🍷 {mention} ɪꜱ {mm}%   𝐊𝐨𝐥𝐚𝐫𝐮 !"
    await app.send_document (
        chat_id=message.chat.id,
        document=KOLARUH,
        caption=KOLARU,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### URUTURAN
@app.on_message(filters.command("uruttu"))
async def lesbian(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    URUTTU = f" 💜 {mention} ɪꜱ {mm}%  Urrutran sir ivan!"
    await app.send_document (
        chat_id=message.chat.id,
        document=URUTTUH,
        caption=URUTTU,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### noi

@app.on_message(filters.command("no"))
async def boob(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    NOI = f"  {mention}ꜱ VENA VENAAH VEH VENA {mm}% NOI-NOI "
    await app.send_document (
        chat_id=message.chat.id,
        document=NO,
        caption=NOI,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

######### accept

@app.on_message(filters.command("accepted"))
async def cock(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    YES = f" 🐈 {mention} Sethu vechidulam {mm}𝙈𝙖𝙩𝙘𝙝🐈"
    await app.send_document (
        chat_id=message.chat.id,
        document=ACCEPTED,
        caption=YES,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

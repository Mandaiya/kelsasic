from AlexaMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " yunnaku lam yen da intha velai - venna thalaiya🥱 ",
           " yunaku irrukura LIFE ha yennaku donate pannidu apo than neku santhosam ",
           " Vc la yentha ponnu kitta urutitu irrukaa👻🙊 ",
           " summa thane irruka antha TV remote yedhutu kudu da manga manda 😁🥲 ",
           " mooku kila vai irruku athuku mela yenna irruku - romba yosikatha yenna moolaiye illala 🤣🤣 ",
           " athu yenna nu therla athu yeppadey solurathu nu therla - yunna partha paitiyam marri irruku 😁 ",
           " nan yarru yunakku nee yar yennaku ?? ",
           " nalla saptiya apo nalla toongu - illana mokka potutu irrupa  ",
           " Oree kulu kulu nu irrukiyoo inga va yevalo sooda irruku nu parru ",
           " Ivana yedhu vechi adikulam",
           " yenna da guru guru nu pakuraa - Deii  ",
           " yenga irrunthu da varenga yenaku neh  ",
           " sari nan poi velaiye pakuren - varaaataahhh ",
           " suthuthey suthuthey boombi - nee yenna vitu ponna pothumada saami 🤣🤣 ",
           " konjam kanda thna irrukum adjust paniko illana palahidum ",
           " dei Kundu yunaku yenna da velai inga ",
           " aasaiya kekuren - Saptiya - cut - shot nalla vanthuchi Thank you 🤔 ",
           " Hi Hello Hey Vanakam Vanthanam - poitu varen ",
           " pesuran pesuran Vc la ana avan yenna sonnalum yennku tookam varalaiye 😅 ",
           " dei nee lam vantha yenna varaliyana yenna - poi velaiya paru daw 🫣 ",
           " saptiya nee - 1 ",
           " yenna soru thina - 2 ",
           " yennaku kodukama sapudura nee lam nalla irrupa - 3 ",
           " sari nalla toongitu work parru  - 20 ",
           " dei last bench kara toongatha da 😮‍💨 - 4 ",
           " nalla saptu saptu toonguran pare 😬 - 5 ",
           " ipo nee yelunthukula nu vei 🫣 - 8 ",
           " Yun left side la parru un crush irrukanga - 9 ",
           " sari toongu kanavula un crush varum 😝😅 - 10 ",
           " nalla sapta pola inga varikum kekuthu yaepom 🙈😃 - 6 ",
           " dei nalavaneee yelunthudu da - 7 " ,
           " sari sari toongunathu pothum velaiya parru - 11 ",
           " innoruka polam variya sorru thinga - 12 ",
           " sari oru tips solluren - toongama irruka - 13 ",
           " pakathula work la un crush irruntha.. manager ku theriyama sight adey 🤧 ",
           " sari sari parthathu pothum ipo parru nalla mandaila yerum 🫥 - 16 ",
           " ninachen , yenna da kannu vera yengaiyo poguthu nu  😂 - 17 ",
           " sari work pandra pasanga luku - meeting nu yulla poidunga 😃 - 18 ",
           " AC la semaiya tookam varum - ana pinnadey manager irruakaru 🙈 - 19 ",
           " Aaga inniku mudinzichi tipss hu ! Varaataahhhh 🏃‍♂️ - 21 ",
           " innum ivanga pandrathu yennalam pakanum ho 😃 ",
           " yeley - 22 ",
           " soluu leyy - 23 ",
           " solurathuku onum illa ley - irrunthalum soluven vokanthu kellu 🙈 -24 ",
           " inna da yun pirchanai ipo - tookam varuthu toonga vidu ley - 25 ",
           " yenakum urakam varuthu antha ac remote yenga irruku - 26 ",
           " inga than pinnadey parru AC remote varum - 27 ",
           " ha da apapdey antha switch ha on pannitu po da - illana manager paapan - 28 ",
           " dei kanna - nan than da antha manager😬 - 29",
           " vanga manager sir - yeppadey irrukenga veetula yellam sowkiyam ha - 29 ",
           " pambrakatta thalaiya nee pannathu yellam camera la theriyuthu da - 30",
           " ippadey poi athuyum yen kitta matikitiyee pangu ",
           " sari sari sattu buttu nu vera velaiya parru - somberiya irruntha yeppadey ",
           " addeeiii - inga va veh nee - ama yedhuku kooputen, sari poitu varen ",
           " yennaku oru doubtuu - nan paitiyam nu vothukuren nee vothupiya ? ",
           " oru tea potu varuvom ha - 31 ",
           " irru da manga manda manager koopuduran varen, sollunga sir -32 ",
           " ippadey heh poona ivan yunmai soluran ha poi soluran ha nu theriyathey - 33 ",
           " dei innum ha da avan kooda pesura - tea kaali ayiduchina yenna kekatha - solliputen - 34",
           " ada irru da varen - yun matter than one matikichi sollitu irrukan - 35 ",
           " aiyoo yentha file maati koodututen nu therliyee - 36 ",
           " dei avana koopudu inna pandra avan inga vara sollu - 37 ",
           " sir neenga sonna lam varamatan -38 ",
           " etheyy avalo periya alu agitan ha avan - yenga irrukan - 38 ",
           " tea kadalila yungala pathi song paaditu irrukan sire 😃 - 39 ",
           " nalla paatu paduvan ha avan - irru keepom - 40",
           " avanuku pattu than oru keedu - poi velaiya parunga da - 41 ",
           " dei avalothan yunakku - ippadey act panna pothuma sir ",
           " vai athingam da yuanku - irru thechividuren ",
           " manasu valikuthu sir - dei nan bot da poda anguttu ",
           " Tag la onnum ila thuki potutu poi velaya paaru ",
           " Peasama poriya ila moonjila pooran vitruvean ",
           " Neeyum naanum vera illada… - Summa sonean asai ah paru nan bot ne human… veliya javoooo ",
           " Un look eh seri ila iru unaku oru seetu eduthu pakalam 😂",
           " Unna la innum unveetula sooru potu vachirukanga ",
           " ena lookku athu thaan onnum ilanu therithula aprm ena bye bye ",
           " sari ley time ku saptu nalla tooongu - poitu varen ",
           " **Hey inga va veh nee** ",
           " **VE-NN-A thalaiya yena da pandra** ",
           " **Nalavaneee saptiya yenna pandra** ",
           " **deiii nee lam yen irruka poidu appdey heh😋** ",
           " **Nanae kolanthai da nambumga da** ",
           " **moodhugula knife yedhutu yara kuthulam nu partha yenna da nee vanthu nikuraa🙃** ",
           " **Ana solliten ithulam nalathuku illa parthukaa ! avalothan han🤨** ",
           " **Oru flow la poiturukum bothu yevan da athu nadula comedy pannikituu __ odddu** ",
           " **Ama onu vanganum heh yenna vangalam solluu🥲** ",
           " **dei murugesha antha AK47 gun ha konjam kooda bore adikuthu😋** ",
           " **yenna da suda matikuthi ! manichidu talaivarey bullet podala** ",
           " **athu yeppadey da yunna sudanum nu kekum bothu mattum bullet kanum🙄🤔** ",
           " **yunnaku yenna mooku neelama irrukam 🤔! pakathu theru la poster la irrunthuchhiii🏃🏃** ",
           " **Ana yunnaku vai irruke yennaku mela irruku 🙄🙄** ",
           " **sari yedhachum nalla song sollu kepom🫶** ",
           " **paatu poda sonna yena yen da podura ! venna thalaiya** ",
           " **yenna game thala aduva nee😛! oru match polama** ",
           " **Ama yunna pathi onu sonnangley ath uumnai ha🤔** ",
           " **sari yellame vithudu, nan oru 3 kelvi kekuren soluriya nu pakalam** ",
           " **yara nee neelam oru aley illaa venna thalaiya🤗** ",
           " **konjam kooda navura vidamatikuran heh yenna da venum yunnaku** ",
           " **Yevalo vati da sollurathu yunnaku mandai la brain heh illa da yunnaku venna thalaiya** ",
           " **Ana sathiyama sollala nee lam thiruntha mata🥺🥺** ",
           " **ama nan paitiyakaran na nee yaruu😶** ",
           " **yunnaku vekam lam vratha da sena panni marri nikuraa🤔** ",
           " **appadey ha ithu vera theriyaama pocha😜** ",
           " **amaa yenna alaiyee kanum sethutiya** ",
           " **nalla thingura yenna vitutu nalla irrpa** ",
           " **sari satu butu nu sollu yenna venum sapuda apram kasu illanu nu soliduven** ",
           " **Nee nalavana illna ketavanuku mela nalavn ha🙊** ",
           " **ama nee ipo yenna pandra yenna marri vetiya thane irrukaa apram yenga pore😺** ",
           " **sari sari pesunathu pothum poi toongu🥲** ",
           " **yepayum happy ha samthosama irru apo than yunna pakuravanga irruntha ivana marri irrukanum nu ninachi santhosama irrupanga😅** ",
           " **illana irrukura vanagalaiyum auchi irruka vidu da venna ythalaiya🙊🙊** ",
           " **Sooruu inga illaiyam pakathu veedu layum illaiyam agamothathuku sorru ilaiyam🙈🙈** ",
           " **porathum pore irru kuli kulla thali viduren🕳** ",
           " **sari apo nan kilamburen neeyum pesitu nalla urutitu poi toongu, thaniya da🙊** ",
           " **Nan nee avan avar ival iva yellarum ... onum illa..?👀** ",
           " **yelai anga yenna da pandra inga va game adalam** ",
           " **sari bore adicha sollu game adalam** ",
           " **inga oruthan irrupan nalla parru yunnakula irrukpan ana irrukamatan avan yar??😻** ",
           " **ama nee yaru sollu ?🙃** ",
           ]

@app.on_message(filters.command(["tagall"], prefixes=["/","!"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐆𝐫𝐩 𝐥𝐚 Use 𝐩𝐨𝐝𝐮𝐧𝐠𝐚 /tagall functions eh")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("ʏᴜɴɢᴀᴋᴜʟᴜ ᴀᴅᴍɪɴ ᴘᴏᴛᴀᴛʜᴜᴋᴜ ᴀᴘᴘᴀʀᴀᴍ ᴛʜᴀɴ ᴀᴄᴄᴇᴘᴛ ᴀᴀɢᴜᴍ . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 \n\nTo stop the tagging process, use the commands /tagoff or /tagstop.. ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 \n\nTo stop the tagging process, use the commands /tagoff or /tagstop.. ..")
    if chat_id in spam_chats:
        return await message.reply("ADA konjam porumaiya irrunga - ooditu irrukula ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("Innum antha /tagall yarum start panala - neenga pannungaleey 😂..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("ʏᴜɴɢᴀᴋᴜʟᴜ ᴀᴅᴍɪɴ ᴘᴏᴛᴀᴛʜᴜᴋᴜ ᴀᴘᴘᴀʀᴀᴍ ᴛʜᴀɴ ᴀᴄᴄᴇᴘᴛ ᴀᴀɢᴜᴍ.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**𝙽𝚊𝚗𝚍𝚛𝚒𝚐𝚊𝚕 𝚞𝚜𝚎 𝚙𝚊𝚗𝚗𝚊𝚝𝚑𝚞𝚔𝚞🫠 meendum varuga**\n\nTo stop the tagging process, use the commands /tagoff or /tagstop.")

@app.on_message(filters.command(["stop"]))
async def inform_stop_commands(client, message):
    await message.reply("To stop the tagging process initiated by /tagall, you can use either /tagoff or /tagstop commands.")

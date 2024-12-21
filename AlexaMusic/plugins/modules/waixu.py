from pyrogram import Client, filters
import random
from AlexaMusic import app

# Predefined GIF URLs for each command
GIFS = {
    "punch": [
        "https://telegra.ph/file/4f6e65932ae0bed995564.mp4",
        "https://telegra.ph/file/594ee58dca4dc1e555c7d.mp4",
        "https://telegra.ph/file/1434f2c6f7bda4e76ad9f.mp4",
        "https://telegra.ph/file/9d47af90ad0dc3c857f45.mp4",
        "https://telegra.ph/file/17514eeed94421e743231.mp4",
        "https://telegra.ph/file/5bb65e08ca4b48b684ffa.mp4",
        "https://telegra.ph/file/25215f6113d087cc0424c.mp4",
    ],
    "slap": [
        "https://telegra.ph/file/4ff5aa5bcc0416c5ea32b.mp4",
        "https://telegra.ph/file/80b838861f85f07433f3d.mp4",
        "https://telegra.ph/file/7c29d4705f1a524bb0fbb.mp4",
        "https://telegra.ph/file/e113e5b39a3e274983a5a.mp4",
        "https://telegra.ph/file/58df0033e30e0df2157ff.mp4",
        "https://telegra.ph/file/e27287a57c1a84a55a93d.mp4",
    ],
    "hide": [
        "https://telegra.ph/file/2232d3dcf5f29e0b15721.mp4",
        "https://telegra.ph/file/060527140ac116dc7babc.mp4",
        "https://telegra.ph/file/330523235223fbd6bb8de.mp4",
        "https://telegra.ph/file/41917334234895a67be85.mp4",
        "https://telegra.ph/file/9cab22ae3d0c71a7ddb43.mp4",
        "https://telegra.ph/file/515cab214dd7c61da0782.mp4",
    ],
    "knife": [
        "https://telegra.ph/file/b170b3d3f69a0fe2a9c26.mp4",
        "https://telegra.ph/file/16a4598feac081275823d.mp4",
        "https://telegra.ph/file/23452c358b5d722f1331f.mp4",
        "https://telegra.ph/file/f2c3b164da4e742cff1f5.mp4",
        "https://telegra.ph/file/63dd415d3315412ebfc1b.mp4",
        "https://telegra.ph/file/173696093432bd0053eab.mp4",
    ],
    "kicks": [
        "https://telegra.ph/file/3b23aaa0942430ad320dc.mp4",
        "https://telegra.ph/file/473c2401fdcc878fd7310.mp4",
        "https://telegra.ph/file/84a3745c1127834921161.mp4",
        "https://telegra.ph/file/11fdaeed5a80dc8adb4d6.mp4",
        "https://telegra.ph/file/8a1002cf1e1fd63b1a173.mp4",
        "https://telegra.ph/file/3c6c93c481e2037f82d3f.mp4",
    ],
    "hug": [
        "https://telegra.ph/file/b9690317007aec6b577f6.mp4",
        "https://telegra.ph/file/f224f04ff6b8bf4caaa96.mp4",
        "https://telegra.ph/file/d5882581bc27d18f4dc0c.mp4",
        "https://telegra.ph/file/85b3f6eb8dd42dc32dff2.mp4",
        "https://telegra.ph/file/84301c49c1befd539cccb.mp4",
        "https://telegra.ph/file/3f301c534081233e76d74.mp4",
    ],
    "bite": [
        "https://telegra.ph/file/d2d0cc0d476c047bc0a52.mp4",
        "https://telegra.ph/file/b08226debf24b94fbb010.mp4",
        "https://telegra.ph/file/4487aae01332a8b9f1452.mp4",
        "https://telegra.ph/file/ea38b203fc3e3feceaffa.mp4",
        "https://telegra.ph/file/7628ecae0b247f01e4c00.mp4",
        "https://telegra.ph/file/70fb5abd2d3ca012bcd24.mp4",
    ],
    "hate": [
        "https://telegra.ph/file/b43cdd9383f9b1df8971c.mp4",
        "https://telegra.ph/file/c85986f1cc35a4f0d9056.mp4",
        "https://telegra.ph/file/4457f58eae3fd1006ac8b.jpg",
        "https://telegra.ph/file/5f38536e53cde81c0b82e.mp4",
        "https://telegra.ph/file/8840c8940fef43993eaa2.mp4",
        "https://telegra.ph/file/feca3c68d09250fb57cd8.mp4",
    ],
    "highfive": [
        "https://telegra.ph/file/498ffa118349f01a411d4.mp4",
        "https://telegra.ph/file/b7b6dd72092deffe800ff.mp4",
        "https://telegra.ph/file/05034a5801a42e660516a.mp4",
        "https://telegra.ph/file/af6d191d9dda65c0c8714.mp4",
        "https://telegra.ph/file/0d0ce0f4d6f302a9e858a.mp4",
        "https://telegra.ph/file/d29145cdcf1590b037f4b.mp4",
    ],
    "die": [
        "https://telegra.ph/file/3ad2fde26bc09ef87bc12.mp4",
        "https://telegra.ph/file/29976328665143d3124bb.mp4",
        "https://telegra.ph/file/7c60a0f83ca6420e7a81e.mp4",
        "https://telegra.ph/file/010ee3d8ed0394ae8fa81.mp4",
        "https://telegra.ph/file/098bb688131962a0ce903.mp4",
        "https://telegra.ph/file/e18d9270e8b289b8a635c.mp4",
    ],
    "run": [
        "https://telegra.ph/file/eb73fa58a8b3483acd3f5.mp4",
        "https://telegra.ph/file/80686144eb8181ca9aa91.mp4",
        "https://telegra.ph/file/6056059e6c7a714e6b0ec.mp4",
        "https://telegra.ph/file/c2403e501775abb2811ff.mp4",
        "https://telegra.ph/file/eff008dab108eb43a062d.mp4",
        "https://telegra.ph/file/d577cd3b7c4c26223b5aa.mp4",
    ],
    "shoot": [
        "https://telegra.ph/file/a3962c0ea6b7d687286f6.mp4",
        "https://telegra.ph/file/7c0ae1bfdd4b983ca98e9.mp4",
        "https://telegra.ph/file/7c0ae1bfdd4b983ca98e9.mp4",
        "https://telegra.ph/file/65d9e3074467ee83844e8.mp4",
        "https://telegra.ph/file/7abf1da931cfc80823685.mp4",
        "https://telegra.ph/file/5c312a64cae761ae9e488.mp4",
    ],
    "dance": [
        "https://telegra.ph/file/fe99088b631324211194f.mp4",
        "https://telegra.ph/file/82fb5d4f9c08f3647e0b9.mp4",
        "https://telegra.ph/file/45972055a6b9521ecb67b.mp4",
        "https://telegra.ph/file/7c0868d3bb8f9b1489ce3.mp4",
        "https://telegra.ph/file/e06c042f9c3efae3afb54.mp4",
        "https://telegra.ph/file/cceac831c3216d540d02b.mp4",
    ]
}

# Command handlers for various animations
@app.on_message(filters.command(list(GIFS.keys())) & ~filters.forwarded & ~filters.via_bot)
def animation_command(client, message):
    try:
        sender = message.from_user.mention(style='markdown')
        target = sender if not message.reply_to_message else message.reply_to_message.from_user.mention(style='markdown')
        
        command = message.command[0].lower()
        gif_url = random.choice(GIFS[command])

        commands = {
            "punch": {"emoji": "💥", "text": "adichitangaleyy"},
            "slap": {"emoji": "😒", "text": "yenna ley aaranzita"},
            "hide": {"emoji": "😛", "text": "nambo olinzipom"},
            "knife": {"emoji": "😵", "text": "yenna ley konnuputta"},
            "kick": {"emoji": "😠", "text": "ayioo vothachitan heh"},
            "hug": {"emoji": "🤗", "text": "ieee katipudichitanga"},
            "bite": {"emoji": "😈", "text": "ina ley kadikuraa"},
            "hate": {"emoji": "😘", "text": "neku yunna pudikathu"},
            "highfive": {"emoji": "🙌", "text": "podu maja than"},
            "die": {"emoji": "💀", "text": "yennaiyee konnutala"},
            "run": {"emoji": "🏃", "text": "oduraa kaipulla"},
            "shoot": {"emoji": "🔫", "text": "sethuduu"},
            "dance": {"emoji": "💃", "text": "nalla nadanam adura ley nee"}
        }

        msg = f"{sender} {commands[command]['text']} {target}! {commands[command]['emoji']}"
        message.reply_animation(animation=gif_url, caption=msg)
        
    except Exception as e:
        message.reply_text(f"An unexpected error occurred: {str(e)}")

# Starting the bot
if __name__ == "__main__":
    app.run()

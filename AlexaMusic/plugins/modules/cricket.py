from pyrogram import Client, filters
from AlexaMusic import app

# Dictionary to store scores for each player and their current score in an over
scores = {}
overs = {}

# Constants for the game
OVERS_LIMIT = 6  # Number of balls in an over

@app.on_message(filters.command("bat"))
async def bat(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Initialize score and over if the user is playing for the first time
    if user_id not in scores:
        scores[user_id] = 0
    if user_id not in overs:
        overs[user_id] = 0
    
    # Roll the dice with the cricket  emoji 🎲
    x = await bot.send_dice(chat_id, "🎲")
    m = x.dice.value  # The number rolled by the dice

    # Initialize score and over count
    current_score = scores[user_id]
    current_over = overs[user_id]

    # Check the result of the dice roll
    if m == 3:
        # If the roll is '3', the player is "out"
        await message.reply_text(f"Oops! You're out! Your score for this over is: {current_score}", quote=True)
        scores[user_id] = 0  # Reset score for the next over
        overs[user_id] = 0   # Reset the over count
    elif m == 5:
        # If the roll is '5', it's an extra run
        scores[user_id] += 1
        await message.reply_text(f"Extra run! Your score for this over is: {scores[user_id]}", quote=True)
    elif m in [1, 2, 4, 6]:
        # If the roll is '1', '2', '4', or '6', add the corresponding runs to the score
        scores[user_id] += m
        await message.reply_text(f"You scored {m} runs! Your current score is: {scores[user_id]}", quote=True)
    
    # Update the over count
    overs[user_id] += 1

    # Check if the over is complete (6 balls)
    if overs[user_id] == OVERS_LIMIT:
        await message.reply_text(f"End of the over! Your total score for the over is: {scores[user_id]}", quote=True)
        scores[user_id] = 0  # Reset score for next over
        overs[user_id] = 0   # Reset the over count

@app.on_message(filters.command("cricketscore"))
async def leaderboard(bot, message):
    # Sort users by their score and display the top scorers
    leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    leaderboard_text = "🏆 **Leaderboard** 🏆\n\n"

    for idx, (user_id, score) in enumerate(leaderboard[:10], 1):
        user = await bot.get_users(user_id)
        leaderboard_text += f"{idx}. {user.first_name} - {score} runs\n"

    if not leaderboard:
        leaderboard_text = "No players yet."

    await message.reply_text(leaderboard_text, quote=True)

__help__ = """
Play Cricket Game:
- /bat - Bat 🎲 Roll the dice and score runs!
- /cricketscore - Show the leaderboard
"""

__mod_name__ = "Cʀɪᴄᴋᴇᴛ Gᴀᴍᴇ"

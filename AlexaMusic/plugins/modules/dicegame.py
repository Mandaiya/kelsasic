from pyrogram import Client, enums, filters
import random
from AlexaMusic import app as app

# Global dictionary to store scores
user_scores = {}

# Target points for winning
TARGET_POINTS = 50

# Function to roll the dice and determine win/loss
async def roll_dice_and_calculate_score(user_id, emoji, message):
    # Roll the dice with the specified emoji
    x = await app.send_dice(message.chat.id, emoji)
    dice_value = x.dice.value
    
    # Simulate the target score to beat for this round (random between 1 and 6)
    target_score = random.randint(1, 6)

    # Determine if user won or lost
    if dice_value >= target_score:
        # Win: Add point
        user_scores[user_id] = user_scores.get(user_id, 0) + 1
        result_text = f"Congratulations {message.from_user.mention}, you won this round! Your score is: {user_scores[user_id]}\n Target Score = 50"
    else:
        # Lose: Deduct point
        user_scores[user_id] = user_scores.get(user_id, 0) - 1
        result_text = f"Sorry {message.from_user.mention}, you lost this round. Your score is: {user_scores[user_id]}\n Target Score = 50"
    
    # Check if user reached the target points
    if user_scores[user_id] >= TARGET_POINTS:
        result_text += f"\n🎉 {message.from_user.mention} has reached the target of {TARGET_POINTS} points and won the game! 🎉"
        user_scores[user_id] = 0  # Reset the score after winning
    elif user_scores[user_id] <= -TARGET_POINTS:
        result_text += f"\n😞 {message.from_user.mention} has lost all their points! Game over. 😞"
        user_scores[user_id] = 0  # Reset the score after losing

    # Send the result of the dice roll and update the user's score
    await message.reply_text(result_text, quote=True)

# Commands for playing the game
@app.on_message(filters.command("dice"))
async def dice(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "🎲", message)

@app.on_message(filters.command("dart"))
async def dart(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "🎯", message)

@app.on_message(filters.command("basket"))
async def basket(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "🏀", message)

@app.on_message(filters.command("jackpot"))
async def jackpot(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "🎰", message)

@app.on_message(filters.command("ball"))
async def ball(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "🎳", message)

@app.on_message(filters.command("football"))
async def football(bot, message):
    await roll_dice_and_calculate_score(message.from_user.id, "⚽", message)

# Command to show the leaderboard
@app.on_message(filters.command("leaderboard"))
async def leaderboard(bot, message):
    # Sort users by their score and display the top scorers
    leaderboard = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    leaderboard_text = "🏆 **Leaderboard** 🏆\n\n"

    for idx, (user_id, score) in enumerate(leaderboard[:10], 1):
        user = await bot.get_users(user_id)
        leaderboard_text += f"{idx}. {user.first_name} - {score} points\n"

    if not leaderboard:
        leaderboard_text = "No players yet."

    await message.reply_text(leaderboard_text, quote=True)

# Game instructions
__help__ = """
Play Game With Emojis:
- /dice - Dice 🎲
- /dart - Dart 🎯
- /basket - Basket Ball 🏀
- /ball - Bowling Ball 🎳
- /football - Football ⚽
- /jackpot - Spin slot machine 🎰

Commands to track progress:
- /leaderboard - Show the leaderboard
"""

__mod_name__ = "Dɪᴄᴇgame"

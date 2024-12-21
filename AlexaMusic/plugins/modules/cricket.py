from pyrogram import Client, filters
from AlexaMusic import app

# Dictionary to store scores for each player, their current score in an over, and the round results
scores = {}
overs = {}
round_scores = {}

# Constants for the game
OVERS_LIMIT = 6  # Number of balls in an over
WINNING_SCORE = 50  # Score needed to level up

@app.on_message(filters.command("bat"))
async def bat(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Initialize score and over if the user is playing for the first time
    if user_id not in scores:
        scores[user_id] = 0
    if user_id not in overs:
        overs[user_id] = 0
    if user_id not in round_scores:
        round_scores[user_id] = 0

    # Roll the dice with the cricket emoji 🎲
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
        round_scores[user_id] = 0  # Reset round score

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
    round_scores[user_id] = scores[user_id]

    # Check if the over is complete (6 balls)
    if overs[user_id] == OVERS_LIMIT:
        await message.reply_text(f"End of the over! Your total score for the over is: {scores[user_id]}", quote=True)
        overs[user_id] = 0  # Reset the over count

        # Check if the player is the winner of this round
        round_winner = None
        highest_score = -1
        for player_id, score in round_scores.items():
            if score > highest_score and score != 0:
                highest_score = score
                round_winner = player_id
        
        if round_winner:
            # Increment the winner's score by 1 point
            scores[round_winner] += 1
            await bot.send_message(round_winner, f"🎉 You won this round! Your total score is now: {scores[round_winner]} points")

        # Reset round scores for the next round
        round_scores.clear()

    # Check if any player has won the game by reaching the winning score
    for user_id, score in scores.items():
        if score >= WINNING_SCORE:
            await message.reply_text(f"🎉 {message.from_user.mention} has reached {WINNING_SCORE} points and leveled up! 🎉", quote=True)
            scores[user_id] = 0  # Reset score after leveling up

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
- /bat - Bat 🎲 Roll the dice and score runs! You can be out, score extra runs, or hit normal runs.
- /cricketscore - Show the leaderboard

Game Rules:
- You roll a dice and score runs based on the number.
- Dice roll '3' means you're out for the round.
- Dice roll '5' gives you an extra run.
- Score '1', '2', '4', or '6' for regular runs.
- Each over consists of 6 balls.
- If you win a round, you earn 1 point.
- The first player to reach 50 points levels up.

Good luck!
"""

__mod_name__ = "Cʀɪᴄᴋᴇᴛ Gᴀᴍᴇ"

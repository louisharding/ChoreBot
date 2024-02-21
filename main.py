"""
This project is intended to make my domestic life better...
I find it rather annoying to have to constantly remind my housemates that it's their
day to empty & fill the dishwasher, or that it's their week to put the bins out.
So, i propose a solution. A discord bot which reminds them on their respective days of duty.
One way or another, the bot will send a message to a housemate when their duties are due.
I will  have to work out:
    How to integrate code into discord
    How to keep a bot running
    How to message specific users
    A time library which i can use modulus logic with the set of Louis>Darcy>Tom>Connor to cycle through, given a
    seed date. This means given a start date, the mod will extrapolate all future housemate's chore days
"""
import random
from datetime import date
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'A fat horse cock',
        'a buttery horse cock!',
        'a creamy horse cock'
    ]

    if message.content == 'obamna':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


client.run(TOKEN)
def returnChoreInfo():
    blokeList = ["Connor's", "Tom's", "Darcy's", "Louis'"]
    today = date.today()
    # 6th of december 2023 = Louis' day, this will be the seed date, used to orient the
    seedDate = date(2023, 12, 6)
    daysDifference = today - seedDate
    blokeIndex = daysDifference.days % 4
    print(f'Difference between {today} (today) and {seedDate} (seed date) is {daysDifference} days')
    print(f'Today is {blokeList[blokeIndex]} day')




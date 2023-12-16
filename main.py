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
from datetime import date
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to discordd')


client.run(TOKEN)

blokeList = ["Louis'", "Darcy's", "Tom's", "Connor's"]
today = date.today()
# 6th of december 2023 = Louis' day, this will be the seed date, used to
seedDate = date(2023, 12, 6)

daysDifference = today - seedDate

blokeIndex = daysDifference.days % 4
print('Difference between ', today, '(today) and', seedDate, '(seed date) is', daysDifference.days, 'days')
print('Today is', blokeList[blokeIndex], 'day')

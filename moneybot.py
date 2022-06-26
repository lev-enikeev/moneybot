import json  # используется только для обработки инвентаря, но ему можно найти и другое применение
import requests
import discord
import db
from credentials import TOKEN
from tabulate import tabulate  # удобный модуль для рисования таблиц
from discord.ext import commands
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)
#import random
moneys = 0




@bot.command()
async def pay(ctx, money, date):
    db.addmoney(money, date)
    await ctx.send("вы получили + " + money)
    global moneys
    moneys = moneys + int(money)


@bot.command()
async def balance(ctx):
    global moneys
    cost = moneys
    await ctx.send(f"У вас {db.balance()}")
bot.run(TOKEN)

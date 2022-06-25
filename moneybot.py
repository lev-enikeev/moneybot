import discord
from discord.ext import commands
import requests
import sqlite3 #модуль sqlite
from tabulate import tabulate #удобный модуль для рисования таблиц
import json #используется только для обработки инвентаря, но ему можно найти и другое применение
intents = discord.Intents.default()
conn = sqlite3.connect("Discord.db") # или :memory:
cursor = conn.cursor()
bot = commands.Bot(command_prefix='>', intents=intents)
#import random
moneys = 0

cost = conn.row[2]
@bot.command()
async def pay(ctx, money):
    await ctx.send("вы получили + " + money)
    global moneys
    moneys = moneys + int(money)
    

@bot.command()
async def balance(ctx):
    global moneys
    cost = moneys
    await ctx.send(f"У вас {moneys}")
bot.run('OTg4ODMwOTQ2Mjg1NDYxNTg2.G8siZ1.qIXiACUe3jzozWxT6tx__QUo07HktHpFQ4AYvk')
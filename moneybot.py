import db
import discord
from credentials import TOKEN
from discord.ext import commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def pay(ctx, money):
    db.addmoney(money)
    await ctx.send("вы получили + " + money)


@bot.command()
async def balance(ctx):
    await ctx.send(f"У вас {db.balance()}")

bot.run(TOKEN)
